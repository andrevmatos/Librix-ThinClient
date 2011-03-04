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

from distutils.core import setup
from ltmt.defs import version

setup(
	name="LTMT",
	version=version,
	license="GPL",
	author="Librix Dev Team",
	author_email="tutooprog@las.ic.unicamp.br",
	url="http://librixdev.las.ic.unicamp.br",
	description="Librix ThinClient Management Tool",
	long_description="""\
Librix ThinClient Management Tool
---------------------------------

A configuration tool for Librix-powered thinclients.
This tool is capable to set profiles of permissions and users to this profiles.
Then, a daemon part of LTMT will be responsible to read a XML configfile, 
generated and edited by GUI configuration interface, and apply the modular
permission to system, according with user that was logged in.

This version requires Python 3.1 or later.
""",
	packages=["ltmt"],
	classifiers=[
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License (GPL)"
		"Development Status :: 1 - Beta",
		"Operating System :: POSIX",
		"Intended Audience :: Sys Admins"
	]
)
