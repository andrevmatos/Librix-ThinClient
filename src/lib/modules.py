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

from PyQt4.QtCore import SIGNAL, QThread

class LTCModuleParser(object):
	"""Parse and compile information about Librix Thin Client modules"""
	def __init__(self):
		"""Instantiate LTCModuleParser class and exec init routines

		@param	self		A LTCModuleParser instance
		"""
		QThread.__init__(self)

		self.modules = {}
		self.parseModules()

	def parseModules(self):
		"""Import and parse modules

		@param	self		A LTCModuleParser instance
		"""
		from modules.__init__ import __all__ as modlist

		for m in modlist:
			# Attention with modules path
			exec("from modules.{0}.main import __mainclass__ as classname"\
				.format(m))
			exec("from modules.{0}.main import {1}".format(m, classname))
			self.modules[m] = exec("{0}()".format(classname))
			self.modules[m].th = QThread()
			del classname

	def getModulesList(self):
		"""Returns a list of all modules

		@param	self		A LTCModuleParser instance
		@return				A list of modules
		"""
		return(list(self.modules))

	def getModuleStatus(self, module, conf):
		"""Return true if module is active WITH conf

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		@param	conf		String containing config of module
		@return				Bool
		"""
		return(self.modules[module].status(conf))

	def startModule(self, module):
		"""Threaded method to start a module

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		"""
		self.modules[module].th.run = self.modules[module].start
		self.modules[module].th.start()

	def stopModule(self, module):
		"""Threaded method to stop a module

		@param	self		A LTCModuleParser instance
		@param	module		Module name
		"""
		self.modules[module].th.run = self.modules[module].stop
		self.modules[module].th.start()
