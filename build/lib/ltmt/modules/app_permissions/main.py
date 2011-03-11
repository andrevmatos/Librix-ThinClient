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

# __mainclass__ should be a string with the name of the main module class,
# because this file can have more then one class
#__mainclass__ = "Test"

from PyQt4.QtCore import QLocale
import os
import lxml.etree as ET
from copy import deepcopy

from ltmt.modules.skel import Module

from .ui.AppPermissions import AppPermissions
from ltmt.lib.utils import DesktopParser

app_dir = "/usr/share/applications"

# Modes: app (.desktop files), bin (binary executables files)
modes = {'app': [0o600, 0o644], 'bin': [0o700, 0o755]}

class Main(Module):
	"""Applications Permissions module"""

	def __init__(self):
		"""Init module"""

		# self.th will be initiated as a QThread instance
		self.th = None

		# Init default config
		self.setConfig()

		self._locale = QLocale.system().name()

	def prettyname(self):
		"""Return module's pretty name

		@param	self		A Main module instance
		@return				A string containing description
		"""
		_prettyname = {
			'en_US': "Application Permissions",
			'pt_BR': "Permissões de Aplicativos",
		}
		_prettyname['default'] = _prettyname['en_US']

		l = self._locale if self._locale in _prettyname else 'default'

		return(_prettyname[l])

	def description(self):
		"""Return module's description

		@param	self		A Main module instance
		@return				A string containing description
		"""
		_description = {
			'en_US': ''.join(["Configure which applications will be available for ",
				"users, by changing permissions of named .desktop files into ",
				"/usr/share/applications and his corresponding executed binaries."]),
			'pt_BR': ''.join(["Configura quais aplicativos estarão disponíveis ",
				"para os usuários, modificando as permissões dos arquivos ",
				".desktop especificados, dentro de /usr/share/applications ",
				"e seus binários executados correspondentes"])
		}
		_description['default'] = _description['en_US']

		_descConfig = {
			'en_US': {
				"allow": "<br><b>Policy: </b><font color=green>Allow</font><br>"+
					"<b>Denyed Apps:</b> ",
				"deny": "<br><b>Policy: </b><font color=red>Deny</font><br>"+
					"<b>Denyed Apps:</b> ",
			},
			'pt_BR': {
				"allow": "<br><b>Política: </b><font color=green>Permitir</font>"+
					"<br><b>Aplicações Negadas:</b> ",
				"deny": "<br><b>Política: </b><font color=red>Negar</font>"+
					"<br><b>Aplicações Permitidas:</b> "
			}
		}
		_descConfig['default'] = _descConfig['en_US']

		l = self._locale if self._locale in _description else 'default'

		desc = _description[l]

		if self._config is not None:
			desc += _descConfig[l][self._config.find("policy").text]
			desc += ', '.join([a.text.replace(".desktop", "") for a in
				self._config.findall("entry[@type='app']")])

		return(desc)

	def configurable(self):
		"""Return if module is configurable

		@param	self		A Main module instance
		"""
		return(True)

	def category(self):
		"""Return module's category

		@param	self		A Main module instance
		"""
		return("software")

	def start(self):
		"""Start method"""
		if self._config.find("policy").text == 'allow':
			policy = True
		elif self._config.find("policy").text == 'deny':
			policy = False
		apps = [e.text for e in self._config.findall("entry[@type='app']")]
		for D, d, F in os.walk(app_dir):
			for f in F:
				if f.endswith(".desktop"):
					Exec = ''
					try:
						Exec = DesktopParser(os.path.join(D, f)).get('Exec')
						if Exec: Exec = Exec.split()[0]
					except Exception as e:
						print("__ app_permissions error:", e)
					for p in os.environ["PATH"].split(':'):
						b = os.path.join(p, Exec)
						if os.path.isfile(b):
							Exec = b
							break

					if f in apps:
						os.chmod(os.path.join(D, f), modes['app'][not policy])
						if Exec: os.chmod(Exec, modes['bin'][not policy])
					else:
						os.chmod(os.path.join(D, f), modes['app'][policy])
						if Exec: os.chmod(Exec, modes['bin'][policy])

	def stop(self):
		"""Stop method"""
		for D, d, F in os.walk(app_dir):
			for f in F:
				f = os.path.join(D, f)
				if f.endswith(".desktop"):
					Exec = ''
					try:
						Exec = DesktopParser(f).get('Exec')
						if Exec: Exec = Exec.split()[0]
					except:
						pass
					for p in os.environ["PATH"].split(':'):
						b = os.path.join(p, Exec)
						if os.path.isfile(b):
							Exec = b
							break

					os.chmod(f, modes['app'][1])
					if os.path.isfile(Exec): os.chmod(Exec, modes['bin'][1])

	def config(self, parent=None):
		"""Configuration dialog

		This method should show a dialog for configuration, and setConfig
		parent is a optional parameter passed by GUI, if a config GUI is needed
		@param	self		A Test module instance
		@param	parent		A QtGui.QWidget object, to config dialog
		"""
		app = AppPermissions(self.getConfig(), parent)
		# exec_ should return lxml.etree.Element object containing config
		c = app.exec_()
		if c is not None: self.setConfig(c)

	def setConfig(self, config=None, user=None):
		"""Set a given config on module

		@param	self		A Main instance
		@param	config		A lxml.etree.Element object
		@param	user		A optional username. Some modules requires it
		"""
		if config is not None and config.find("policy") is not None:
			self._config = deepcopy(config)
		else:
			# minimum settings require a root, with a 'policy' child
			self._config = ET.Element("root")
			ET.SubElement(self._config, "policy").text = "allow"

	def getConfig(self):
		"""Get a set config on module

		@param	self		A Main instance
		"""
		return(deepcopy(self._config))
