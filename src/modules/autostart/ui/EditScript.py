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

from PyQt4 import QtGui
from .Ui_editScript import Ui_EditScript

class EditScript(QtGui.QDialog):
	"""Show a configuration dialog for autoexec module"""
	def __init__(self, script, parent=None):
		"""Init method

		@param	self		A EditScript instance
		@param	script		A string containing script
		@param	parent		A Parent QtGui.QWidget derivated object
		"""
		self.parent = parent

		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_EditScript()
		self.ui.setupUi(self)

		self.ui.textEdit.setPlainText(script)

	def exec_(self):
		"""Reimplement QtGui.QDialog.exec_ method

		Returns a string with edited script, or None if canceled
		@param	self		A EditScript instance
		"""
		r = QtGui.QDialog.exec_(self)
		t = self.ui.textEdit.toPlainText().strip()
		if r and t:
			return(t)
		else:
			return(None)
