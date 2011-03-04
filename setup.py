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

from PyQt4 import uic
from distutils.core import setup, Command
from distutils.command import build, clean
import os
from os.path import dirname, abspath, isfile, join
from ltmt.defs import version

class clean_ts(clean):
	description = "Clear compiled translations file"
	user_options = []
	
	def initialize_options(self):
		pass
	
	def finalize_options(self):
		pass
	
	def run(self):
		for D, d, F in os.walk('.'):
			for f in F:
				if f.endswith(".qm") and \
				isfile(join(D, f.replace(".qm", ".ts"))):
					os.remove(join(D, f))

class build_ts(build):
	description = "Build and compile .ts translations files"
	user_options = []
	
	def _gen_pro_file(self, PRO, FORMS, SOURCES, TRANSLATIONS):
		SEP = ' '
		with open(PRO, 'w') as pro:
			if SOURCES:
				S = []
				for s in SOURCES:
					if abspath(dirname(s)).startswith(abspath(dirname(PRO))):
						S.append(s)
				pro.write("SOURCES = {0}\n".format(SEP.join(S)))
			if FORMS:
				F = []
				for f in FORMS:
					if abspath(dirname(f)).startswith(abspath(dirname(PRO))):
						F.append(f)
				pro.write("FORMS = {0}\n".format(SEP.join(FORMS)))
			if TRANSLATIONS:
				T = []
				for t in TRANSLATIONS:
					if abspath(dirname(t)).startswith(abspath(dirname(PRO))):
						T.append(t)
				pro.write("TRANSLATIONS = {0}\n".format(SEP.join(TRANSLATIONS)))
	
	def _compile_ts(self, PRO):
		os.system("pylupdate4 {0}".format(PRO))
		os.system("lrelease {0}".format(PRO))
	
	def initialize_options(self):
		pass
		
	def finalize_options(self):
		pass
	
	def run(self):
		PRO = []
		FORMS = []
		SOURCES = []
		TRANSLATIONS = []
		
		for D, d, F in os.walk('.'):
			for f in F:
				if f.endswith(".pro"):
					PRO.append(os.path.join(D, f))
				elif f.endswith(".ui"):
					FORMS.append(os.path.join(D, f))
				elif f.endswith(".py"):
					SOURCES.append(os.path.join(D, f))
				elif f.endswith(".ts"):
					TRANSLATIONS.append(os.path.join(D, f))
		
		for P in PRO:
			self._gen_pro_file(P, FORMS, SOURCES, TRANSLATIONS)
			self._compile_ts(P)

class clean_ui(clean):
	description = "Clean .py compiled from .ui files"
	user_options = []
	
	def initialize_options(self):
		pass
	
	def finalize_options(self):
		pass
	
	def run(self):
		for D, d, F in os.walk('.'):
			for f in F:
				if f.endswith(".ui") and \
				isfile(join(D, "Ui_"+f.replace(".ui", ".py"))):
					os.remove(join(D, "Ui_"+f.replace(".ui", ".py")))

class build_ui(build):
	description = "Compile UI and Resources files"
	user_options = []
	
	def initialize_options(self):
		pass
	
	def finalize_options(self):
		pass
	
	
	def uicompile(dirpath, filename):
		uifile = os.path.join(dirpath, filename)
		pyfile = os.path.join(dirpath, 'Ui_' + filename.replace('.ui', '.py'))
	
		with open(uifile, 'r') as ui, open(pyfile, 'w') as py:
			uic.compileUi(ui, py, execute=True, indent=0, from_imports=True)
	
		return(uifile, pyfile)
	
	def rccompile(rcfile, pyfile=None):
		"""Compile resources
	
		@return	a tuple containing dirpath and pyfile
		"""
		if not pyfile:
			pyfile = rcfile.replace(".qrc", "_rc.py")
	
		os.system("pyrcc4 -py3 {0} -o {1}".format(rcfile, pyfile))
	

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
	classifiers=[
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License (GPL)"
		"Development Status :: 1 - Beta",
		"Operating System :: POSIX",
		"Intended Audience :: Sys Admins"
	],
	package_dir={'ltmt': 'src'},
	packages=[
		"ltmt",
		"ltmt.lib",
		"ltmt.daemon",
		"ltmt.ui",
		"ltmt.ui.icons",
		"ltmt.ui.common",
		"ltmt.ui.help",
		"ltmt.ui.users",
		"ltmt.ui.users.add_user",
		"ltmt.ui.export",
		"ltmt.ui.export.targets",
		"ltmt.ui.export.ssh_export",
		"ltmt.ui.editkeys",
		"ltmt.ui.edit",
		"ltmt.modules",
		"ltmt.modules.app_permissions",
		"ltmt.modules.app_permissions.ui",
		"ltmt.modules.app_permissions.ui.icons",
		"ltmt.modules.disable_usb",
		"ltmt.modules.autostart",
		"ltmt.modules.autostart.ui",
		"ltmt.modules.autostart.ui.icons",
	],
)
