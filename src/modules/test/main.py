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

# __mainclass__ should be a string with the name of the main module class,
# because this file can have more then one class
__mainclass__ = "Test"

class Test(object):
	"""Test module"""
	def __init__(self):
		"""Init module"""

		# self.description should be a string containing a description of module
		self.description = """A test description

		Now, this dont want to mean something
		"""
		self.prettyname = "Test Module"
		self.configurable = True

		# self.th will be a QThread instance
		self.th = None
		pass

	def start(self, conf):
		"""Start module"""
		pass

	def stop(self, conf):
		"""Stop module"""
		pass

	def status(self, conf):
		"""Return true if module is active WITH conf"""
		pass

	def config(self, parent=None):
		"""Config routine

		This must return a string to store, that contains the configuration
		needed by this module
		parent is a optional parameter passed by GUI, if a config GUI is needed
		@param	self		A Test module instance
		@param	parent		A QtGui.QWidget object, to config dialog
		@return				A string to be stored
		"""
		pass
