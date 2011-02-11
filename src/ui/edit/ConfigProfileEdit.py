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

from ui.edit.Ui_configProfileEdit import Ui_configsWidget
from ui.edit.ListItemWidget import ListItemWidget

class ConfigProfileEdit(QtGui.QWidget):
	"""Creates the config tab of a category in profile"""
	def __init__(self, configparser, moduleparser, category, parent=None):
		"""Instantiate a ConfigProfileEdit widget

		containing category options
		@param	self		A ConfigProfileEdit instance
		@param	configparser	A LTCConfigParser instance
		@param	category	A string containing the category name
		@param	parent		Parent QtGui.QWidget
		"""
		self.moduleparser = moduleparser
		self.configparser = configparser
		self.category = category
		self.parent = parent

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_configsWidget()
		self.ui.setupUi(self)

		self.modules_widgets = {}

		for m in moduleparser.getModulesList(category):
			self.modules_widgets[m] = ListItemWidget(
				m, moduleparser, self.ui.listWidget)

	def setProfile(self, profile):
		"""Set modules options according with profile's config

		@param	self		A ConfigProfileEdit instance
		@param	profile		A string containing profile's name
		"""
		for m in self.modules_widgets:
			if self.moduleparser.getModuleConfigurable(m):
				self.moduleparser.setModuleConfig(m,
					self.configparser.getConfig(profile, m))
			self.modules_widgets[m].setActivated(
				self.configparser.getOption(profile, m))
