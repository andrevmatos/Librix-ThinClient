#!/usr/bin/env python3
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

from PyQt4 import uic

from distutils.core import setup
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean
from distutils.command.sdist import sdist

from os import walk,remove,system,stat
from os.path import dirname,basename,abspath,isdir,isfile,join,sep
from shutil import rmtree

class clean(_clean):
	def run(self):
		_clean.run(self)
		if isdir(join(".", "build")):
			rmtree(join(".", "build"))
			print("Removing", join(".", "build"))
		for D, d, F in walk('.'):
			if "__pycache__" in d:
				rmtree(join(D, "__pycache__"), ignore_errors=True)
				print("Removing", join(D, "__pycache__"))
			for f in F:
				if f.endswith(".pyc") or f.endswith(".pyo"):
					remove(join(D, f))
					print("Removing", f)

class build(_build):
	def run(self):
		#clean.run(self)
		_build.run(self)
		build_ui.run(self)
		build_ts.run(self)

class build_ts(_build):
	description = "Build and compile .ts translations files"
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		def _gen_pro_file(PRO, FORMS, SOURCES, TRANSLATIONS):
			SEP = ' '
			with open(PRO, 'w') as pro:
				if SOURCES:
					S = []
					for s in SOURCES:
						if abspath(dirname(s)).startswith(abspath(dirname(PRO))):
							S.append(s.replace(dirname(PRO)+sep, ""))
					pro.write("SOURCES = {0}\n".format(SEP.join(S)))
				if FORMS:
					F = []
					for f in FORMS:
						if abspath(dirname(f)).startswith(abspath(dirname(PRO))):
							F.append(f.replace(dirname(PRO)+sep, ""))
					pro.write("FORMS = {0}\n".format(SEP.join(F)))
				if TRANSLATIONS:
					T = []
					for t in TRANSLATIONS:
						if abspath(dirname(t)).startswith(abspath(dirname(PRO))):
							T.append(t.replace(dirname(PRO)+sep, ""))
					pro.write("TRANSLATIONS = {0}\n".format(SEP.join(T)))

		def _compile_ts(PRO):
			system("pylupdate4 {0}".format(PRO))
			system("lrelease {0}".format(PRO))

		PRO = []
		FORMS = []
		SOURCES = []
		TRANSLATIONS = []

		for D, d, F in walk('.'):
			for f in F:
				if f.endswith(".pro"):
					PRO.append(join(D, f))
				elif f.endswith(".ui"):
					FORMS.append(join(D, f))
				elif f.endswith(".py"):
					SOURCES.append(join(D, f))
				elif f.endswith(".ts"):
					TRANSLATIONS.append(join(D, f))

		for P in PRO:
			_gen_pro_file(P, FORMS, SOURCES, TRANSLATIONS)
			_compile_ts(P)

class build_ui(_build):
	description = "Compile UI and Resources files"
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		def uicompile(uifile, pyfile=None):
			if not pyfile:
				pyfile = join(dirname(uifile),
					'Ui_'+basename(uifile).replace('.ui', '.py'))

			if not isfile(pyfile) or stat(uifile).st_mtime > stat(pyfile).st_mtime:
				with open(uifile, 'r') as ui, open(pyfile, 'w') as py:
					uic.compileUi(ui, py, execute=True, indent=0, from_imports=True)

				fix_from_imports(pyfile)
				print("Compiling UI:", uifile, "=>", pyfile)

			with open(pyfile, 'r') as SRC, open(pyfile.replace("src",
				join(self.build_lib, "ltmt")), 'w') as BLD:
				BLD.write(SRC.read())

		def rccompile(rcfile, pyfile=None):
			if not pyfile:
				pyfile = rcfile.replace(".qrc", "_rc.py")

			if not isfile(pyfile) or stat(rcfile).st_mtime > stat(pyfile).st_mtime:
				system("pyrcc4 -py3 {0} -o {1}".format(rcfile, pyfile))
				print("Compiling Resource:", rcfile, "=>", pyfile)

			with open(pyfile, 'r') as S, open(pyfile.replace("src",
				join(self.build_lib, "ltmt")), 'w') as B:
				B.write(S.read())

		def fix_from_imports(filepath):
			with open(filepath, 'r') as f:
				L = f.readlines()
			RC = []
			for D, d, F in walk("src"):
				for f in F:
					if f.endswith("_rc.py"):
						RC.append(join(D.replace("src", "ltmt"), f))
			for l in range(len(L)):
				if L[l].startswith("from .") and L[l].endswith("_rc\n"):
					for i in RC:
						I = L[l].strip().split()[-1]
						if i.endswith(I+".py"):
							p = dirname(i).replace(sep, ".")
							break
					L[l] = "from {0} import {1}\n".format(p, I)
			with open(filepath, 'w') as f:
				f.write(''.join(L))

		for D, d, F in walk('src'):
			for f in F:
				if f.endswith(".ui"):
					uicompile(join(D, f))
				elif f.endswith(".qrc"):
					rccompile(join(D, f))

def gen_packages():
	P = []
	for D, d, F in walk("src"):
		for f in F:
			if f.endswith(".py") and D not in P:
				P.append(D)
				break
	p = []
	for i in P:
		if i.startswith("src"):
			p.append(i.replace("src", "ltmt", 1).replace(sep, "."))
	return(p)

setup(
	name="ltmt",
	version="0.0.98",
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
	package_data={"ltmt": [
		"ui/i18n/*.qm",
		"modules/disable_usb/udev/*.rules"
	]},
	packages=gen_packages(),
	cmdclass={
		"clean": clean,
		"build": build,
		"build_ts": build_ts,
		"build_ui": build_ui,
		"sdist": sdist,
	},
	data_files=[('/etc', ['thinclient.conf'])],
	scripts=["ltmt"]
)
