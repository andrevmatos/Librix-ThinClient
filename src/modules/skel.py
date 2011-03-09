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

from PyQt4.QtCore import QLocale

class Module(object):
	"""Super class for LTMT modules"""
	def __init__(self):
		"""Init method"""

		self._locale = QLocale.system().name()
		self._user = None
		self._config = None

	def prettyname(self):
		"""Return module's pretty name"""
		pass

	def description(self):
		"""Return module's description"""
		pass

	def configurable(self):
		"""Return True if module is configurable"""
		pass

	def category(self):
		"""Return module's category"""
		pass

	def setConfig(self, config=None, user=None):
		"""Set config and user (optional) in module"""
		pass

	def getConfig(self):
		"""Return module's current configuration"""
		pass

	def config(self, parent=None):
		"""Run module's configuration dialog"""
		pass

	def start(self):
		"""Start routine"""
		pass

	def stop(self):
		"""Stop routine"""
