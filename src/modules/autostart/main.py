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

from PyQt4.QtCore import QLocale

from copy import deepcopy

class Main():
	"""A LTMT module that provides a list of autostart commands"""
	def __init__(self):
		"""Init method

		@param	self		A Main module instance
		"""
		self._locale = QLocale.system().name()

	def prettyname(self):
		"""Return module's prettyname

		@param	self		A Main module instance
		@return				Module's prettyname string
		"""
		_prettyname = {
			'en_US': "Autostart",
			'pt_BR': "Inicialização Automática"
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
			'en_US': ''.join(["Set a list of commands ",
				"to be executed at user login."]),
			'pt_BR': ''.join(["Configura uma lista de comandos ",
				"a serem executados no login do usuário."])
		}
		_description['default'] = _description['en_US']

		_descConf = {
			'en_US': "Command List:",
			'pt_BR': "Lista de Comandos:"
		}

		l = self._locale if self._locale in _description else 'default'

		desc = _description[l]

		if self._config is not None:
			desc += "\n" + _descConf[l] + "\n"
			desc += '\n'.join([c.text for c in self._config.findall("command")])

		return(_description[l])

	def setConfig(self, conf=None, user=None):
		"""Set config on module and user

		@param	self		A Main module instance
		@param	conf		A lxml.etree Element object
		@param	user		A username to apply config
		"""
		self._config = deepcopy(conf)

	def getConfig(self):
		"""Get current config of module

		@param	self		A Main module instance
		@return				A lxml.etree Element object
		"""
		return(self._config)

