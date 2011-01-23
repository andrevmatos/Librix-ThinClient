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

from PyQt4 import QtGui,QtCore

from ui.edit.Ui_configProfileEdit import Ui_configsWidget

class ConfigProfileEdit(QtGui.QWidget):
	"""Creates the config page of a category in profile"""
	def __init__(self, configparser, category, parent=None):
		"""Instantiate a ConfigProfileEdit widget

		containing category options
		@param	self		A ConfigProfileEdit instance
		@param	configparser			A LTCConfigParser instance
		@param	category	A string containing the category name
		@param	parent		Parent QtGui.QWidget
		"""
		self.configparser = configparser
		self.category = category
		self.parent = parent

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_configsWidget()
		self.ui.setupUi(self)

		self.buttons = {}

		for o in configparser.getOptionsList(category):
			self.buttons[o] = QtGui.QPushButton(o, self)
			self.buttons[o].setCheckable(True)
			self.ui.ConfigVerticalLayout.addWidget(self.buttons[o])
			self.connect(self.buttons[o], QtCore.SIGNAL("clicked()"), self.buttonToggled)

		#self.buttonToggled()

	def buttonToggled(self):
		for b in self.buttons:
			if self.buttons[b].isChecked():
				self.buttons[b].setStyleSheet("background-color: rgb(140, 255, 140);")
			else:
				self.buttons[b].setStyleSheet("background-color: rgb(255, 140, 140);")
