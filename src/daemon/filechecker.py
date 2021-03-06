#!/usr/bin/env python3
#
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

import os
from PyQt4.QtCore import QThread,pyqtSignal

from ltmt.lib.utils import sha512sum
import subprocess

from ltmt.defs import configfile
authorized_keys = '~/.ssh/authorized_keys'

class FileChecker(QThread):
	"""Check if configfile was modifyed and reload it"""

	# Signal emited when configfile is readed
	reload = pyqtSignal()

	def __init__(self, configparser, moduleparser):
		"""Thread init routine

		@param	self		A FileChecker instance
		@param	configparser	A LTCConfigParser instance
		"""
		QThread.__init__(self)

		self.configparser = configparser
		self.moduleparser = moduleparser

		self.reload.connect(self.writePubKeys)
		self.reload.connect(self.syncUsers)

		self.reload.emit()

	def writePubKeys(self):
		"""Install pubkeys in configfile on authorized keys file

		Called when checkFile.reload signal is emited
		@param	self		A LTCModuleParser instance
		"""
		print("__writing pubKeys")
		with open(os.path.expanduser(authorized_keys), 'w') as kf:
			kf.write('\n'.join(self.configparser.getKeys()))

	def getHostUsersList(self):
		"""Return a list of all usernames in system

		@param	self		A FileChecker instance
		@return			List of usernames string
		"""
		users = []
		try:
			with open("/etc/passwd", 'r') as pw:
				for l in pw:
					L = l.split(':')
					if len(L) == 7:
						users.append(L[0])
		except:
			pass
		return(users)

	def syncUsers(self):
		"""Add users to host account

		@param	self		A FileChecker instance
		"""

		for u in self.configparser.getUsersList():
			if self.configparser.getUserS(u) and not \
				u in self.getHostUsersList():
				print("__ ### ADD USER", u)

				opt = self.configparser.getUserSync(u)
				l = "useradd"
				if opt["uid"]: l += " -u {0}".format(opt["uid"])
				if opt["init_group"] == u or opt["init_group"] == str(opt["uid"]):
					l += " -U"
				elif opt["init_group"]:
					l += " -g {0}".format(opt["init_group"])
				if opt["groups"]: l += " -G {0}".format(','.join(opt["groups"]))
				if opt["home"]: l += " -m -d {0}".format(opt["home"])
				if opt["shell"]: l += " -s {0}".format(opt["shell"])

				l +=  " {0}".format(u)

				p = subprocess.Popen(l, shell=True)
				p.wait()

				# set shadow password hash
				l = "usermod -p '{0}' {1}".format(opt["passwd"], u)
				p = subprocess.Popen(l, shell=True)
				p.wait()

	def run(self):
		"""Thread main routine

		Check if timestamp of configfile is different of self.configparser
		If yes, check if sha512sum is different
		If yes, reload configs
		@param	self		A FileChecker instance
		"""
		if not os.path.isfile(configfile): return

		if os.stat(configfile).st_mtime != self.configparser.st_mtime:
			hash = sha512sum(configfile)
			if hash != self.configparser.hash:
				print("__ refreshConfigFile")
				self.configparser.readConfigFile()
				self.reload.emit()
