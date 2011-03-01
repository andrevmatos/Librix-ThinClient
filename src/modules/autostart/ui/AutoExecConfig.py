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
from lxml import etree as ET
from .Ui_autoExecConfig import Ui_AutoExecConfig
from .EditScript import EditScript

class AutoExecConfig(QtGui.QDialog):
	"""Show a configuration dialog for autoexec module"""
	def __init__(self, config, parent=None):
		"""Init method

		@param	self		A AutoExecConfig instance
		@param	config		A lxml.etree Element object
		@param	parent		A Parent QtGui.QWidget derivated object
		"""
		self.parent = parent
		self.config=config

		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_AutoExecConfig()
		self.ui.setupUi(self)

		if config is not None:
			for i in config.findall("command"):
				QtGui.QListWidgetItem(i.text, self.ui.listWidget)

	def editCommand(self):
		"""Edit selected command

		@param	self		A AutoExecConfig instance
		"""
		for c in self.ui.listWidget.selectedItems():
			s = EditScript(c.text(), self).exec_()
			if s: c.setText(s)

	def newCommand(self):
		"""Add and edit a new command

		@param	self		A AutoExecConfig instance
		"""
		l = QtGui.QListWidgetItem('', self.ui.listWidget)
		l.setSelected(True)
		self.editCommand()

	def delCommand(self):
		"""Delete an command from command list

		@param	self		A AutoExecConfig instance
		"""
		i = None
		for c in range(self.ui.listWidget.count()):
			if self.ui.listWidget.item(c).isSelected():
				i = c
				break
		self.ui.listWidget.takeItem(i)

	def exec_(self):
		"""Reimplement QtGui.QDialog.exec_ method

		Returns a lxml.etree Element object containing configuration
		@param	self		A AutoExecConfig instance
		@return				A lxml.etree Element object
		"""
		r = QtGui.QDialog.exec_(self)
		if r:
			root = ET.Element("root")
			for c in range(self.ui.listWidget.count()):
				ET.SubElement(root, "command").text = \
					self.ui.listWidget.item(c).text()
			return(root)
		else:
			return(None)


