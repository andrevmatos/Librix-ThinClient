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

import sys
from os.path import abspath, isfile

from PyQt4.QtCore import QCoreApplication, QTimer

from ltmt.daemon.filechecker import FileChecker
from ltmt.daemon.userchecker import UserChecker
from ltmt.lib.daemon import Daemon
from ltmt.lib.config import LTCConfigParser
from ltmt.lib.modules import LTCModuleParser
from ltmt.lib.http import ThreadedServer

from ltmt.defs import configfile, pidfile, http_port

daemon = None

class LibrixTCDaemon(QCoreApplication):
	"""This class provides the main daemon for Librix Thin Client"""
	def __init__(self):
		"""Instantiate LibrixTCDaemon class and exec init routines

		@param	self		A LibrixTCDaemon instance
		"""
		QCoreApplication.__init__(self, sys.argv)

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
		self.checkFileTimer.timeout.connect(self.checkFile.start)

		# Init UserChecker instance and timer
		self.checkUsers = UserChecker(self.configparser, self.moduleparser)
		self.checkUsersTimer = QTimer(self)
		self.checkUsersTimer.timeout.connect(self.checkUsers.start)

		# PID file checker
		self.checkPIDfileTimer = QTimer(self)
		self.checkPIDfileTimer.timeout.connect(self.checkPIDfile)

		self.checkFile.reload.connect(self.checkUsers.clearUser)

		# Start timers
		self.checkFileTimer.start(1000)
		self.checkUsersTimer.start(1000)
		self.checkPIDfileTimer.start(1000)

	def checkPIDfile(self):
		if not isfile(pidfile):
			self.stop()
			sys.exit(0)

	def stop(self):
		print("__STOPPING ALL")
		self.checkFileTimer.stop()
		self.checkUsersTimer.stop()
		for m in self.moduleparser.getModulesList():
			self.moduleparser.stopModule(m)

class TCDaemon(Daemon):
	def run(self):
		print("__run")
		app = LibrixTCDaemon()
		sys.exit(app.exec_())

def main(file=None):
	print("__main")
	global configfile, pidfile

	if file:
		configfile = file
	configfile = abspath(configfile)

	daemon = TCDaemon(pidfile)
	daemon.start()

if __name__ == '__main__':
	main()

