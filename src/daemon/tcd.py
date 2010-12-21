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

import sys
import os
from hashlib import sha512

from PyQt4.QtCore import *
from lib.daemon import Daemon

from lib.config import LTCConfigParser

pidfile = '/var/run/thinclient.pid'
configfile = 'thinclient.conf'

class LibrixTCDaemon(QObject):
	"""This class provides the main daemon for Librix Thin Client"""
	def __init__(self):
		"""Instantiate LibrixTCDaemon class and exec init routines

		@param	self		A LibrixTCDaemon instance
		"""
		QObject.__init__(self)

		self.configparser = LTCConfigParser()
		self.configparser.readConfigFile(configfile)

		self.checkFileTimer = QTimer(self)
		self.connect(self.checkFileTimer,
			SIGNAL("timeout()"), self.checkConfigFile)
		self.checkFileTimer.start(5000)

	def checkConfigFile(self):
		"""Check if configfile was modifyed and reload it

		Check if timestamp of configfile is different of self.configparser
		If yes, check if sha512sum is different
		If yes, reload configs
		@param	self		A LibrixTCDaemon instance
		"""
		if os.stat(configfile).st_mtime != self.configparser.st_mtime:
			with open(configfile, 'r') as f:
				hash = sha512(f.read()).hexdigest()
			if hash != self.configparser.hash:
				self.configparser.readConfigFile(configfile)
				self.emit(SIGNAL("refreshConfigs()"))


class DaemonLauncher(Daemon):
	"""Start daemon mode and init LibrixTCDaemon"""
	def run(self):
		"""The program main loop"""
		self.app = QCoreApplication(sys.argv)
		self.daemon = LibrixTCDaemon()
		sys.exit(self.app.exec_())

def main():
	daemon = DaemonLauncher(pidfile)
	daemon.start()

if __name__ == '__main__':
	main()
