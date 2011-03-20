#!/usr/bin/env python3
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with librix-thinclient.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui

from ltmt.ui.keygen.Ui_openKey import Ui_OpenKey

class OpenKey(QtGui.QDialog):
	"""Show a SSH key into a textLine dialog"""
	def __init__(self, text='', title='Key', parent=None):
		"""Init method
		
		@param	self			A OpenKey instance
		@param	text			A string to show
		@param	parent		A parent QtGui.QWidget
		"""
		self.parent = parent
		self.text = text
		self.clipboard = QtGui.QApplication.clipboard()
		
		QtGui.QDialog.__init__(self)
		self.ui = Ui_OpenKey()
		self.ui.setupUi(self)
		self.ui.textEdit.setFontFamily('monospace')
		
		self.ui.textEdit.setText(text)
		self.setWindowTitle(title)
	
	def copy(self):
		"""Copy current text do clipboard"""
		self.clipboard.setText(self.ui.textEdit.toPlainText())
		self.ui.copyButton.setText(self.tr("Copied!"))
