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

from PyQt4.QtCore import QThread

class LTCModuleParser(object):
	"""Parse and compile information about Librix Thin Client modules"""
	def __init__(self):
		"""Instantiate LTCModuleParser class and exec init routines

		@param	self		A LTCModuleParser instance
		"""
		#QThread.__init__(self)

		self._modules = {}
		self.parseModules()

	def parseModules(self):
		"""Import and parse modules

		@param	self		A LTCModuleParser instance
		"""
		if 'Mod' in vars():
			del Mod
		import ltmt.modules as Mod

		for m in Mod.__all__:
			self._modules[m] = eval("Mod.{0}.Main()".format(m))
			self._modules[m].th = QThread()

	def getCategoriesList(self):
		"""Returns a list of all categories

		@param	self		A LTCModuleParser instance
		@return				A list of categories
		"""
		c = []
		for m in self._modules:
			if self.getModuleCategory(m) not in c:
				c.append(self.getModuleCategory(m))
		c.sort()
		return(c)

	def getModulesList(self, category=''):
		"""Returns a list of all modules in category

		If category is '', return all modules
		@param	self		A LTCModuleParser instance
		@param	category	A category name. If null, return all modules
		@return				A list of modules
		"""
		M = [m for m in self._modules \
			if not category or self.getModuleCategory(m) == category]
		M.sort()
		return(M)

	def getModulePrettyName(self, module):
		"""Get module pretty name

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		@return				A string containing module pretty name
		"""
		return(self._modules[module].prettyname())

	def getModuleDescription(self, module):
		"""Get module description

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		@return				A string containing module description
		"""
		return(self._modules[module].description())

	def getModuleConfigurable(self, module):
		"""Get if module has configuration dialog

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		@return				Bool. True if module is configurable
		"""
		return(self._modules[module].configurable())

	def getModuleCategory(self, module):
		"""Get module's category

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		@return				String containing category name
		"""
		return(self._modules[module].category())

	def setModuleConfig(self, module, config, user=None):
		"""Set given config in module

		@param	self		A LTCModuleParser instance
		@param	module		A module name
		@param	config		A lxml.etree.Element object
		@param	user		A optional username, for modules that requires it
		"""
		if not self.getModuleConfigurable(module):
			return
		self._modules[module].setConfig(config, user)

	def getModuleConfig(self, module):
		"""Get current config from module

		@param	self		A LTCModuleParser instance
		@param	module		A module name
		@return				A lxml.etree.Element object
		"""
		if not self.getModuleConfigurable(module):
			return(None)
		return(self._modules[module].getConfig())

	def configModule(self, module, parent=None):
		"""Exec configuration dialog for module

		@param	self		A LTCModuleParser instance
		@param	module		A module name
		@param	parent		Parent QtGui.QWidget object, passed to module's
							config method
		"""
		if not self.getModuleConfigurable(module):
			return
		self._modules[module].config(parent)

	def startModule(self, module):
		"""Threaded method to start a module

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		"""
		self._modules[module].th.run = self._modules[module].start
		self._modules[module].th.start()

	def stopModule(self, module):
		"""Threaded method to stop a module

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		"""
		self._modules[module].th.run = self._modules[module].stop
		self._modules[module].th.start()
