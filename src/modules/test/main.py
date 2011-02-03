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
#__mainclass__ = "Test"

class Main(object):
	"""Test module"""
	def __init__(self):
		"""Init module"""

		# self.prettyname should be a string containing a pretty name of module
		self.prettyname = "Test Module"
		# self.description should be a string containing a description of module
		self.description = "A test description\n\
Now, this dont want to mean something"
		# self.configurable should be a bool True if module has config options
		self.configurable = True
		# self.category should be a string containing category name of module
		self.category = 'software'

		# self.th will be a QThread instance
		self.th = None

		self.started = False

	def start(self, conf=None):
		"""Start module"""
		if not self.started:
			self.started = True
			print("__", self.prettyname, "started!")

	def stop(self, conf=None):
		"""Stop module"""
		if self.started:
			self.started = False
			print("__", self.prettyname, "stopped!")

	def status(self, conf=None):
		"""Return true if module is active WITH conf"""
		return(self.started)

	def config(self, config, parent=None):
		"""Config routine

		This must return a string to store, that contains the configuration
		needed by this module
		parent is a optional parameter passed by GUI, if a config GUI is needed
		@param	self		A Test module instance
		@param	config		A lxml.etree.Element object containing current config
		@param	parent		A QtGui.QWidget object, to config dialog
		@return				A lxml.etree.Element object to be stored
		"""
		pass
