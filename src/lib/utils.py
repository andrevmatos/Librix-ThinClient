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

import string
from random import choice
from hashlib import sha512

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
