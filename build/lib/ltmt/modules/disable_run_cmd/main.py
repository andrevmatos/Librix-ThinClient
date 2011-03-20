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

from PyQt4.QtCore import QLocale
from configparser import ConfigParser
from os.path import expanduser,isfile

from ltmt.modules.skel import Module

class Main(Module):
	"""A LTMT module that disable KDE's Run Command (Alt+F2) functionality"""
	def __init__(self):
		"""Init method

		@param	self		A Main module instance
		"""
		self._locale = QLocale.system().name()
		self._files = []

	def prettyname(self):
		"""Return module's prettyname

		@param	self		A Main module instance
		@return				Module's prettyname string
		"""
		_prettyname = {
			'en_US': "Disable Run Command",
			'pt_BR': "Desativar Execução de Comandos"
		}
		_prettyname['default'] = _prettyname['en_US']

		l = self._locale if self._locale in _prettyname else 'default'

		return(_prettyname[l])

	def description(self):
		"""Return module's description

		@param	self		A Main module instance
		@return				Module's description string
		"""
		_description = {
			'en_US': ''.join(["Disable KDE's Run Command (krunner) ",
				"functionality, usually accessed by Alt+F2 key binding and ",
				"allow user to run arbitrary commands."]),
			'pt_BR': ''.join(["Desativa a funcionalidade Executar Comando do ",
				"KDE (krunner), normalmente acessada através do atalho Alt+F2, ",
				"e que permite ao usuário a execução de comandos arbitrários."])
		}
		_description['default'] = _description['en_US']

		l = self._locale if self._locale in _description else 'default'

		return(_description[l])

	def configurable(self):
		"""Return true if module is configurable

		@param	self		A Main module instance
		@return				Bool
		"""
		return(False)

	def category(self):
		"""Return true if module is configurable

		@param	self		A Main module instance
		@return				Bool
		"""
		return("software")

	def setConfig(self, config=None, user=None):
		"""Set config on module and user

		@param	self		A Main module instance
		@param	conf		No matter for this module
		@param	user		A username to apply config
		"""
		self._user = user

	def getConfig(self):
		"""No matter

		@param	self		A Main module instance
		@return				None
		"""
		return(None)

	def start(self):
		"""Start method"""

		p = ConfigParser()
		kdeglobals = ''
		if isfile(expanduser("~{0}/.kde4/share/config/kdeglobals")):
			kdeglobals = expanduser("~{0}/.kde4/share/config/kdeglobals")
		elif isfile(expanduser("~{0}/.kde/share/config/kdeglobals")):
			kdeglobals = expanduser("~{0}/.kde/share/config/kdeglobals")
		else:
			return

		p.read(kdeglobals)

		s = 'KDE Action Restrictions'
		if not p.has_section(s):
			p.add_section(s)
		p.set(s, "run_command", False)
		p.set(s, "shell_access", False)


	def stop(self):
		"""Stop method"""
		p = ConfigParser()
		kdeglobals = ''
		if isfile(expanduser("~{0}/.kde4/share/config/kdeglobals")):
			kdeglobals = expanduser("~{0}/.kde4/share/config/kdeglobals")
		elif isfile(expanduser("~{0}/.kde/share/config/kdeglobals")):
			kdeglobals = expanduser("~{0}/.kde/share/config/kdeglobals")
		else:
			return

		p.read(kdeglobals)

		s = 'KDE Action Restrictions'
		if not p.has_section(s):
			p.add_section(s)
		p.set(s, "run_command", True)
		p.set(s, "shell_access", True)
