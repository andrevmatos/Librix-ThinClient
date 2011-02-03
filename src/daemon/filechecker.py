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

	refreshConfigs = pyqtSignal()

	def __init__(self, configparser, moduleparser):
		"""Thread init routine

		@param	self		A FileChecker instance
		@param	configparser	A LTCConfigParser instance
		"""
		QThread.__init__(self)

		self.configparser = configparser
		self.configfile = configparser.configfile

		self.moduleparser = moduleparser

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
				self.refreshConfigs.emit()
		print('__end FileChecker')
