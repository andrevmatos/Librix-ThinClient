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
from tempfile import NamedTemporaryFile as tmpfile
from lxml import etree as ET

from os import chmod,listdir,remove,mkdir
from os.path import expanduser,join,isdir

from .ui.AutoExecConfig import AutoExecConfig

ae_prefix = 'autoexec_'
ae_suffix = '.sh'
ae_mode = 0o755

class Main():
	"""A LTMT module that provides a list of autostart commands"""
	def __init__(self):
		"""Init method

		@param	self		A Main module instance
		"""
		self._locale = QLocale.system().name()

		self._user = None
		self._config = None
		self._files = []

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
			desc += "\n<br><b>" + _descConf[l] + "</b>"
			for c in self._config.findall("command"):
				desc += "\n<hr><code>" +\
					c.text.replace('\n', '<br>') + "</code>"

		return(desc)

	def configurable(self):
		"""Return true if module is configurable

		@param	self		A Main module instance
		@return				Bool
		"""
		return(True)

	def category(self):
		"""Return true if module is configurable

		@param	self		A Main module instance
		@return				Bool
		"""
		return("software")

	def setConfig(self, config=None, user=None):
		"""Set config on module and user

		@param	self		A Main module instance
		@param	conf		A lxml.etree Element object
		@param	user		A username to apply config
		"""
		self._config = deepcopy(config)
		self._user = user

	def getConfig(self):
		"""Get current config of module

		@param	self		A Main module instance
		@return				A lxml.etree Element object
		"""
		if self._config is not None:
			return(self._config)
		else:
			return(ET.Element("root"))

	def start(self):
		"""Start method"""
		if not self._user:
			return

		
		if not isdir(expanduser(join('~'+self._user, ".config"))):
			mkdir(expanduser(join('~'+self._user, ".config")))
		if not isdir(expanduser(join('~'+self._user, ".config", "autostart"))):
			mkdir(expanduser(join('~'+self._user, ".config", "autostart")))

		self.stop()					# clean old autoexec scripts

		for c in self._config.findall("command"):
			f = tmpfile(prefix=ae_prefix, suffix=ae_suffix, delete=True,
				dir=expanduser(join('~'+self._user, '.config', 'autostart')))
			chmod(f.name, ae_mode)	# exec permission
			self._files.append(f)	# stores on self._files list
			text = "#!/bin/bash\n"
			text += c.text + "\n"
			text += "exit 0\n"
			f.write(text.encode())
			f.flush()				# synchronize

	def stop(self):
		"""Stop method"""
		# NamedTemporaryFile deletes file when it is closed
		while self._files:
			self._files.pop(0).close()
		# if a improperly shutdown occurred
		if self._user:
			for f in listdir(expanduser(join('~'+self._user, '.config',
				'autostart'))):
				if f.startswith(ae_prefix) and f.endswith(ae_suffix):
					remove(f)

	def config(self, parent=None):
		"""Config method"""
		dialog = AutoExecConfig(deepcopy(self._config), parent)
		r = dialog.exec_()
		if r is not None:
			self.setConfig(r, self._user)
