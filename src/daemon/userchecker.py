﻿#!/usr/bin/env python3
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
from PyQt4.QtCore import SIGNAL, QThread

class UserChecker(QThread):
	"""Check if a user in configfile is logged and apply rules"""
	def __init__(self, configparser, moduleparser):
		"""Thread init routine

		@param	self		A UserChecker instance
		@param	configparser	A LTCConfigParser instance
		"""
		QThread.__init__(self)

		self.configparser = configparser
		self.moduleparser = moduleparser

		self.currentuser = None

	def run(self):
		"""Thread main routine

		Check if some user in self.configparser.getUsersList() is in logged
		users list. If yes, apply configurations
		@param	self		A UserChecker instance
		"""
		#print('__run UserChecker', end=' ')
		with os.popen('users') as U:
			loggedUsers = list(set(U.read().strip().split()))
			loggedUsers.sort()

		if self.currentuser:
			if self.currentuser not in loggedUsers:
				for o in self.moduleparser.getModulesList():
					self.moduleparser.stopModule(o)
				self.currentuser = None
		else:
			for u in self.configparser.getUsersList():
				if u in loggedUsers:
					p = self.configparser.getUserProfile(u)
					for o in self.moduleparser.getModulesList():
						# Atention: modules would be responsible
						# by check if itself is already started or stoped
						if self.configparser.getOption(p, o):
							self.moduleparser.startModule(o)
						else:
							self.moduleparser.stopModule(o)
					self.currentuser = u
		#print('__end UserChecker')