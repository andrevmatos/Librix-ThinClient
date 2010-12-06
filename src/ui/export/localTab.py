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

from PyQt4 import QtGui

class LocalTab:
	"""Methods that will be inherited by ExportPage"""

	def localImportBrowseFiles(self):
		"""Browse files and set ui.pathLineEdit with given path

		@param	self		A ExportPage instance
		"""
		filepath = QtGui.QFileDialog.getOpenFileName(self, "Import File",
			self.defaultconfigdir)
		if filepath:
			self.ui.pathLineEdit.setText(filepath)

	def localImportClickedButton(self, button):
		"""Parse localImport clicked buttons

		@param	self		A ExportPage instance
		@param	button		A QPushButton from QtGui.QDialogButtonBox
		"""

		# Reset button clicked. Reset pathLineEdit to default
		if self.ui.localImportButtonBox.standardButton(button) \
			== QtGui.QDialogButtonBox.Reset:
			self.ui.pathLineEdit.setText(
				os.path.join(self.defaultconfigdir, "thinclient.conf"))
		elif self.ui.localImportButtonBox.standardButton(button) \
			== QtGui.QDialogButtonBox.Apply:
			# TODO: file export methods

			pass

	def localImportCheckFile(self, path):
		"""Verify if path on self.ui.pathLineEdit exists

		and set lineedit text color as red and apply button disabled if not

		@param	self		A ExportPage instance
		@param	path		A filepath string
		"""
		if os.path.isfile(path):
			# Set lineedit text color to default
			self.ui.pathLineEdit.setStyleSheet("")
			# Set Apply button enabled
			for b in self.ui.localImportButtonBox.buttons():
				if self.ui.localImportButtonBox.standardButton(b)\
					== QtGui.QDialogButtonBox.Apply:
					b.setEnabled(True)
		else:
			# Set lineedit text color as red
			self.ui.pathLineEdit.setStyleSheet("color: red;")
			# Set Apply button disabled
			for b in self.ui.localImportButtonBox.buttons():
				if self.ui.localImportButtonBox.standardButton(b)\
					== QtGui.QDialogButtonBox.Apply:
					b.setEnabled(False)


	def localExportBrowseFiles(self):
		"""Browse files and set ui.pathLineEdit_2 with given path

		@param	self		A ExportPage instance
		"""
		filepath = QtGui.QFileDialog.getSaveFileName(self, "Export File",
			self.defaultconfigdir)
		if filepath:
			self.ui.pathLineEdit_2.setText(filepath)

	def localExportClickedButton(self, button):
		"""Parse localExport clicked buttons

		@param	self		A ExportPage instance
		@param	button		A QPushButton from QtGui.QDialogButtonBox
		"""

		# Reset button clicked. Reset pathLineEdit to default
		if self.ui.localExportButtonBox.standardButton(button) \
			== QtGui.QDialogButtonBox.Reset:
			self.ui.pathLineEdit_2.setText(
				os.path.join(self.defaultconfigdir, "thinclient.conf"))
		elif self.ui.localExportButtonBox.standardButton(button) \
			== QtGui.QDialogButtonBox.Save:
			# TODO: file import methods
			pass

	def localExportCheckFile(self, path):
		"""Verify if path on self.ui.pathLineEdit exists

		and set lineedit text color as red and apply button disabled if not

		@param	self		A ExportPage instance
		@param	path		A filepath string
		"""
		if not os.path.isfile(path):
			# Set lineedit text color to default
			self.ui.pathLineEdit_2.setStyleSheet("")
		else:
			# Set lineedit text color as red
			self.ui.pathLineEdit_2.setStyleSheet("color: red;")
