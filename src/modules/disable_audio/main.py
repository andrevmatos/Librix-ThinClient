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
from os import stat, chmod, walk
from os.path import join

modes = [0o600, 0o660]

class Main():
	"""A LTMT module that provides a list of autostart commands"""
	def __init__(self):
		"""Init method

		@param	self		A Main module instance
		"""
		self._locale = QLocale.system().name()
		self._files = []

		audio_gid = self._get_audio_gid()

		for D, d, F in walk("/dev"):
			for f in F:
				f = join(D, f)
				try:
					if stat(f).st_gid == audio_gid:
						self._files.append(f)
				except:
					pass

	def prettyname(self):
		"""Return module's prettyname

		@param	self		A Main module instance
		@return				Module's prettyname string
		"""
		_prettyname = {
			'en_US': "Disable Audio",
			'pt_BR': "Desativar Audio"
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
			'en_US': ''.join(["Disable audio (in/out) for user logged in, "
				"by removing read/write permissions of /dev devices "
				"which are owned by \"audio\" group."]),
			'pt_BR': ''.join(["Desativa o audio (entrada/saida) para o "
				"usuário logado, removendo as permissões de leitura e escrita ",
				"dos dispositivos em /dev que pertencem ao grupo \"audio\"."])
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
		for f in self._files:
			chmod(f, modes[0])

	def stop(self):
		"""Stop method"""
		for f in self._files:
			chmod(f, modes[1])

	def _get_audio_gid(self):
		"""Return int GID of 'audio' group"""
		with open("/etc/group", "r") as G:
			for l in G:
				L = l.strip().split(':')
				if L and L[0] == "audio":
					return(int(L[2]))
