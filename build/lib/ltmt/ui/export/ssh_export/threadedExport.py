#!/usr/bin/env python3
#
#
#
# This file is part of librix-thinclient.
#
# librix-thinclient is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# librix-thinclient is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with librix-thinclient.  If not, see <http://www.gnu.org/licenses/>.

#import os
import subprocess
import socket

from PyQt4.QtCore import QThread,pyqtSignal

from ltmt.defs import rsyncdirs, rsyncexclude

class ThreadedExport(QThread):
	"""Create a QThread that scp files to a list of targets"""

	# Custom signals: param: destiny
	startedSCP = pyqtSignal(str)
	requestPasswd = pyqtSignal(str)
	finishedSCP = pyqtSignal(str)
	errorSCP = pyqtSignal(str)

	def __init__(self, files, privkey, targets):
		"""Init method

		@param	self		A ThreadedExport instance
		@param	files		A list of files to send
		@param	privkey		A SSH private key file with read access
		@param	targets		A list of strings containing targets address
		"""
		self.files = files
		self.privkey = privkey
		self.targets = targets
		self.password = None

		QThread.__init__(self)

	def start(self):
		"""Reimplemented method QThread.start

		@param	self		A ThreadedExport instance
		"""
		self.pause = False
		QThread.start(self)

	def make_copy(self, target):
		"""Actually do SCP export

		@param	self		A ThreadedExport instance
		@param	target		Destiny IP
		@return				Int. 0 if Success. 1 if password. Error code else.
		"""
		ssh_opts = ('-o "StrictHostKeyChecking no" -o '+
			'"NumberOfPasswordPrompts 1" -o "PasswordAuthentication no" '+
			'-i "{0}"'.format(self.privkey))

		# SCP
		if self.password:
			# Use expect to pass password to scp
			p = subprocess.Popen(('expect -c \'spawn scp -p {0} {1} root@{2}:/etc'+
				' ; expect "*?assword:" ; send "{3}\\n" ; expect eof ; '+
				'catch wait result ; exit [lindex $result 3 ]\'').format(
				ssh_opts, ' '.join(self.files), target, self.password),
				shell=True, stdin=subprocess.PIPE,
				stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			p = subprocess.Popen(('scp -B -p {0} {1} root@{2}:/etc').format(ssh_opts,
				' '.join(self.files), target), shell=True, stdin=subprocess.PIPE,
				stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		r = p.wait()
		if r == 1:
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect((target, 22))
			except:
				r = 99
			finally:
				sock.close()

		if r or not 'rsync' in self.files:
			return(r)

		# RSYNC
		if rsyncexclude:
			exc = '--exclude={'+','.join(rsyncexclude)+'}'
		else:
			exc = ''
		if self.password:
			# Use expect to pass password to scp
			q = subprocess.Popen(('expect -c \'spawn rsync -avRP -e "ssh -l '+
				'root {0}" {1} {2} {3}:/'+
				' ; expect "*?assword:" ; send "{4}\\n" ; expect eof ; '+
				'catch wait result ; exit [lindex $result 3 ]\'').format(
				ssh_opts, exc, ' '.format(rsyncdirs), target, self.password),
				shell=True, stdin=subprocess.PIPE,
				stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			q = subprocess.Popen(('rsync -avRP -e "ssh -l root -o '+
				'\'BatchMode yes\' {0}" {1} {2} {3}:/').format(ssh_opts, exc,
				' '.format(rsyncdirs), target), shell=True,
				stdin=subprocess.PIPE, stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)

		s = q.wait()

		return(s)


	def run(self):
		"""Main thread method

		Actually exec scp routines in files in list, to targets hosts,
		using privkey
		@param	self		A ThreadedExport instance
		"""
		while self.targets and not self.pause:
			# Take next target
			t = self.targets.pop(0)

			self.startedSCP.emit(t)
			r = self.make_copy(t)

			if r == 0:
				print("__ host finished", t)
				self.finishedSCP.emit(t)
			elif r == 1:
				print("__ host password request", t)
				self.requestPasswd.emit(t)
				# reinsert target on list, and pause thread
				self.targets.insert(0, t)
				self.pause = True
			else:
				print("__ host error", t, "=", r)
				self.errorSCP.emit(t)

		if self.pause:
			print("__thread PAUSING!!")
		else:
			print("__thread FINISHING!!")
