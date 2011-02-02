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
import os

from ui.export.Ui_exportWidget import Ui_ExportWidget
from ui.common.LeftMenuItem import LeftMenuItem
from ui.export.addTargets import AddTargets
from ui.export.scanTargets import ScanTargets

class ExportPage(QtGui.QWidget):
	"""Creates the main Export page"""
	def __init__(self, configparser, moduleparser, leftList, parent=None):
		"""Instantiate a ExportPage object

		@param	self		A ExportPage instance
		@param	configparser			A LTCConfigParser instance
		@param	leftList	The leftMenu QListWidget, to create the tab
		@param	parent		A QtGui.QWidget parent object
		"""
		self.moduleparser = moduleparser
		self.configparser = configparser
		self.leftList = leftList
		self.parent = parent

		self.targets = []

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_ExportWidget()
		self.ui.setupUi(self)

		self.tab = LeftMenuItem(leftList, self.tr("Export"),
			QtGui.QIcon(":/export_icon/fork.png"))

		self.fscompleter = QtGui.QCompleter(self)
		self.fscompleter.setModel(QtGui.QDirModel(self.fscompleter))
		self.ui.privKeyPath.setCompleter(self.fscompleter)

		self.checkPrivKeyFile(self.ui.privKeyPath.text())

	def browsePrivKeyFile(self):
		"""Browse files and set ui.pathLineEdit with given path

		@param  self            A ExportPage instance
		"""
		filepath = QtGui.QFileDialog.getOpenFileName(self, self.tr("Import File"),
			os.path.expanduser('~root/.ssh'))
		if filepath:
			self.ui.privKeyPath.setText(filepath)

	def checkPrivKeyFile(self, path):
		"""Verify if path on self.ui.pathLineEdit exists

		and set lineedit text color as red and apply button disabled if not
		@param	self		A ExportPage instance
		@param	path		A filepath string
		"""
		if os.path.isfile(path):
			# Set lineedit text color to default
			self.ui.privKeyPath.setStyleSheet("")
			# Set Apply button enabled
			for b in self.ui.buttonBox.buttons():
				if self.ui.buttonBox.standardButton(b)\
					== QtGui.QDialogButtonBox.Apply:
					b.setEnabled(True)
		else:
			# Set lineedit text color as red
			self.ui.privKeyPath.setStyleSheet("color: red;")
			# Set Apply button disabled
			for b in self.ui.buttonBox.buttons():
				if self.ui.buttonBox.standardButton(b)\
					== QtGui.QDialogButtonBox.Apply:
					b.setEnabled(False)

	def addTargetsClicked(self):
		"""Launch dialog to add targets to scan list

		@param	self		A ExportPage instance
		"""
		addTargetsDialog = AddTargets(self)
		scanTargetsDialog = ScanTargets(self)

		targets = addTargetsDialog.exec_()
		targets = scanTargetsDialog.exec_(targets)

		self.targets.extend(targets)
		self.refreshTargets()

	def removeTargetsClicked(self):
		"""Remove selected targets from targets list

		@param	self		A ExportPage instance
		"""
		for i in self.ui.treeWidget.selectedItems():
			if i.isSelected():
				try: self.targets.remove(i.text(0))
				except Exception as e: print("This must not been happened:", e)
		self.refreshTargets()

	def refreshTargets(self):
		print("__refreshed")
		self.ui.treeWidget.clear()
		for i in self.targets:
			QtGui.QTreeWidgetItem(self.ui.treeWidget, [i, "Online"])

