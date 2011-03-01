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
#import os

from PyQt4.QtCore import QCoreApplication, SIGNAL, QObject, QTimer

from daemon.filechecker import FileChecker
from daemon.userchecker import UserChecker
#from lib.daemon import Daemon
from lib.config import LTCConfigParser
from lib.modules import LTCModuleParser
from lib.http import ThreadedServer

pidfile = '/var/run/thinclient.pid'
configfile = 'thinclient.conf'
http_port = 8088

class LibrixTCDaemon(QObject):
	"""This class provides the main daemon for Librix Thin Client"""
	def __init__(self):
		"""Instantiate LibrixTCDaemon class and exec init routines

		@param	self		A LibrixTCDaemon instance
		"""
		QObject.__init__(self)

		# Init LTCConfigParser
		self.configparser = LTCConfigParser()
		self.configparser.readConfigFile(configfile)

		# Init LTCModuleParser
		self.moduleparser = LTCModuleParser()

		# Start HTTP server
		self.httpserver = ThreadedServer(self.configparser, http_port)
		self.httpserver.start()

		# Init FileChecker instance and timer
		self.checkFile = FileChecker(self.configparser, self.moduleparser)
		self.checkFileTimer = QTimer(self)
		self.connect(self.checkFileTimer,
			SIGNAL("timeout()"), self.checkFile.start)

		# Init UserChecker instance and timer
		self.checkUsers = UserChecker(self.configparser, self.moduleparser)
		self.checkUsersTimer = QTimer(self)
		self.connect(self.checkUsersTimer,
			SIGNAL("timeout()"), self.checkUsers.start)

		self.checkFile.reload.connect(self.checkUsers.clearUser)

		# Start timers
		self.checkFileTimer.start(5000)
		self.checkUsersTimer.start(2000)

def run():
		"""The program main loop"""
		app = QCoreApplication(sys.argv)
		daemon = LibrixTCDaemon()
		sys.exit(app.exec_())

#def main():
#	daemon = Daemon(pidfile)
#	daemon.run = run
#	daemon.start()

if __name__ == '__main__':
	#main()
	run()

