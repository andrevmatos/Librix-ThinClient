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
from ui.export.Ui_exportWidget import Ui_ExportWidget
from ui.utils.LeftMenuItem import LeftMenuItem

from ui.export.localTab import LocalTab

class ExportPage(QtGui.QWidget, LocalTab):
	"""Creates the main Export page"""
	def __init__(self, tcd, leftList, parent=None):
		"""Instantiate a ExportPage object

		@param	self		A ExportPage instance
		@param	tcd			A librix_tcd instance
		@param	leftList	The leftMenu QListWidget, to create the tab
		@param	parent		A QtGui.QWidget parent object
		"""
		self.tcd = tcd
		self.leftList = leftList
		self.parent = parent

		self.defaultconfigdir = "/etc"

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_ExportWidget()
		self.ui.setupUi(self)

		self.tab = LeftMenuItem(leftList, 'Import/Export',
			QtGui.QIcon(":/export_icon/fork.png"))

		self.fscompleter = QtGui.QCompleter(self)
		self.fscompleter.setModel(QtGui.QDirModel(self.fscompleter))
		self.ui.pathLineEdit.setCompleter(self.fscompleter)

		self.localImportCheckFile(self.ui.pathLineEdit.text())
		self.localExportCheckFile(self.ui.pathLineEdit_2.text())
