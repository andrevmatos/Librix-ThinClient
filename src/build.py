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

import os
import sys
import subprocess
from PyQt4 import uic

def uicompile(dirpath, filename):
	uifile = os.path.join(dirpath, filename)
	pyfile = os.path.join(dirpath, 'Ui_' + filename.replace('.ui', '.py'))

	with open(uifile, 'r') as ui, open(pyfile, 'w') as py:
		uic.compileUi(ui, py, execute=True, indent=0, from_imports=True)

	return(uifile, pyfile)

def resourcecompile(dirpath, filename):
	""" Compile resources

	@return	a tuple containing dirpath and pyfile
	"""
	rcfile = os.path.join(dirpath, filename)
	pyfile = os.path.join(dirpath, filename.replace('.qrc', '_rc.py'))

	S = subprocess.Popen("pyrcc4 -py3 {0} -o {1}".format(rcfile, pyfile), shell=True)
	S.wait()

	return(dirpath, pyfile.split('/')[-1]) # return dirpath and py filename

def fix_from_imports(filepath, resources):

	with open(filepath, 'r') as f:
		cont = f.read()
	for r in resources:
		path = '.'.join(resources[r].split('/')[1:])
		path = path if path else '.'
		cont = cont.replace('from . import {0}'.format(r),
			'from {0} import {1}'.format(path, r))
	with open(filepath, 'w') as f:
		f.write(cont)

def main(dir='.'):
	""" UI and resources compiler """
	resources = {}

	for dirpath, dirnames, filenames in os.walk(dir):
		for f in filenames:
			if '.qrc' in f:
				r = resourcecompile(dirpath, f)
				resources[r[1].split('.')[0]] = r[0]
				print("# Resource Compile:", f, '=>', r[1])
	for dirpath, dirnames, filenames in os.walk(dir):
		for f in filenames:
			if '.ui' in f:
				u = uicompile(dirpath, f)
				fix_from_imports(u[1], resources)
				print("# UI Compile:", f, "=>", u[1])

if __name__ == '__main__':
	main()
	exit(0)
