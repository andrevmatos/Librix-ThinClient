#!/usr/bin/env python3
#
#
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

import string
import os
import re
from random import choice
from hashlib import sha512
import time

def passwdGen(size=8):
	"""Generates a password (random letters and digits string) of size lenght

	@param	size		The string lenght
	"""
	return(''.join([choice(string.ascii_letters + string.digits)\
		for i in range(size)]))

def sha512sum(filepath):
	"""Generates a sha512 hex digest of filepath

	@param	filepath	A filepath string
	"""
	with open(filepath, 'r') as f:
		return(sha512(f.read().encode('utf-8')).hexdigest())

class DesktopParser():
	"""Parse a .desktop file"""
	def __init__(self, file):
		"""Init method

		@param	self		A DesktopParser instance
		@param	file		A file name to parse
		"""
		assert os.path.isfile(file), "File \"{0}\" not found".format(file)
		self._file = open(file, 'r')

	def get(self, key):
		"""Get value of key from file

		@param	self		A DesktopParser instance
		@param	key			A key value
		@return				The value of key, None if key not in file
		"""
		r = re.compile(r'\s*{0} ?= ?'.format(key), re.I)
		self._file.seek(0)
		for l in self._file:
			if re.match(r, l):
				return(re.sub(r, '', l).strip())
		return(None)

