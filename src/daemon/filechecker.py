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

import os
from PyQt4.QtCore import QThread,pyqtSignal
from lib.utils import sha512sum

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
		self.configfile = configparser.configfile

		self.moduleparser = moduleparser
		self.reload.connect(self.syncUsers)
	
	def getHostUsersList(self):
		"""Return a list of all usernames in system
		
		@param	self		A FileChecker instance
		@return			List of usernames string
		"""
		users = []
		with open("/etc/passwd", 'r') as pw:
			for l in pw:
				L = l.split(':')
				if len(L) == 7:
					users.append(L[0])
		return(users)
	
	def syncUsers(self):
		"""Add users to host account
		
		@param	self		A FileChecker instance
		"""
		for u in self.configparser.getUsersList():
			if self.configparser.getUserS(u) and not \
				u in self.getHostUsersList():
				opt = self.configparser.getUserSync(u)
				l = "useradd -D"
				if opt["uid"]: l += " -u {0}".format(opt["uid"])
				if opt["init_group"] == u or opt["init_group"] == str(opt["uid"]):
					l += " -U"
				elif opt["init_group"]:
					l += " -g {0}".format(opt["init_group"])
				if opt["groups"]: l += " -G {0}".format(','.join(opt["groups"]))
				
				

	def run(self):
		"""Thread main routine

		Check if timestamp of configfile is different of self.configparser
		If yes, check if sha512sum is different
		If yes, reload configs
		@param	self		A FileChecker instance
		"""
		print('__run FileChecker', end=' ')
		if os.stat(self.configfile).st_mtime != self.configparser.st_mtime:
			hash = sha512sum(self.configfile)
			if hash != self.configparser.hash:
				self.configparser.readConfigFile()
				self.reload.emit()
		print('__end FileChecker')
