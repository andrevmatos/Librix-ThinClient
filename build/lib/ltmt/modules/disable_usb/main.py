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
from os.path import dirname,basename,abspath,join
from os import remove

from ltmt.modules.skel import Module

disable_rule = join(dirname(abspath(__file__)), "udev",
	"10-disable_usb_storage.rules")
udev_rule = join("/etc/udev/rules.d", basename(disable_rule))

class Main(Module):
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
			'en_US': "Disable USB Storage",
			'pt_BR': "Desativar Dispositivos de Armazenamento USB"
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
			'en_US': ''.join(["Disable USB storage devices for user, ",
				"like pendrives, USB disk drivers, USB card readers, etc."]),
			'pt_BR': ''.join(["Desativa o uso de dispositivos de ",
				"armazenamento em massa USB, como pendrives, drivers de ",
				"disco USB, leitores de cartão USB, etc."])
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
		return("hardware")

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
		with open(disable_rule, 'r') as DR, open(udev_rule, 'w') as UR:
			UR.write(DR.read())

	def stop(self):
		"""Stop method"""
		try: remove(udev_rule)
		except: pass
