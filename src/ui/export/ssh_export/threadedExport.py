#!/usr/bin/env python3
#
#  Copyright (C) 2010 - Librix Dev Team
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

from PyQt4.QtCore import QThread,pyqtSignal

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

	def run(self):
		"""Main thread method

		Actually exec scp routines in files in list, to targets hosts,
		using privkey
		@param	self		A ThreadedExport instance
		"""
		while self.targets and not self.pause:
			# Take next target
			t = self.targets.pop(0)

			self.startedSCP(t)
			if self.password:
				# Use expect o pass password to scp
				p = subprocess.Popen(("expect -c 'spawn scp -o "+
					"\"StrictHostKeyChecking no\"  -i {0} {1} {2}; "+
					"expect \"*?assword:*\"; send \"{3}\r\"; expect eof'"
					).format(self.privkey, ' '.join(self.files), t,
					self.password), shell=True)
			else:
				p = subprocess.Popen(("scp -o \"PasswordAuthentication "+
					"no\" -o \"StrictHostKeyChecking no\" -i {0} "+
					"{1} {2}").format(self.privkey, ' '.join(self.files), t),
					shell=True)

			r = p.wait()
			# if got password error
			if r == 0:
				self.finishedSCP.emit(t)
			elif r == 1:
				self.requestPasswd.emit(t)
				# reinsert target on list, and pause thread
				self.targets.insert(0, t)
				return
			else:
				self.errorSCP.emit(t)
