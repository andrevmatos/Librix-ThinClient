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

from ltmt.ui.edit.Ui_listItemWidget import Ui_listItemWidget

class ListItemWidget(QtGui.QWidget):
	"""Creates the QListWidgetItem widget of a module into cateogory"""
	def __init__(self, module, moduleparser, parent=None):
		"""Instantiate a ListItemWidget widget

		containing a option in category
		@param	self		A ListItemWidget instance
		@param	module		String containing module name
		@param	moduleparser	A LTCModuleParser instance
		@param	parent		Parent QtGui.QListWidget
		"""
		self.expanded = False
		self.module = module
		self.parent = parent
		self.moduleparser = moduleparser
		self.listItem = QtGui.QListWidgetItem(parent)

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_listItemWidget()
		self.ui.setupUi(self)

		self.ui.prettyLabel.setText(moduleparser.getModulePrettyName(module))
		self.ui.prettyLabel_2.setText(moduleparser.getModulePrettyName(module))
		self.ui.descriptionText.setHtml(
			moduleparser.getModuleDescription(module))

		if not moduleparser.getModuleConfigurable(module):
			self.ui.configureButton.setEnabled(False)
		else:
			self.ui.configureButton.clicked.connect(self.config)

		self.parent.setItemWidget(self.listItem, self)
		self.setExpanded(False)

	def setActivated(self, activated=None):
		"""Set this module activated or not

		@param	self		A ListItemWidget instance
		@param	activated	Bool
		"""
		# if None, toggle
		if activated is None:
			activated = not self.activated

		self.activated = activated

		# Refresh description, that may contain current config infos
		self.ui.descriptionText.setHtml(
			self.moduleparser.getModuleDescription(self.module))

		self.ui.toggleButtonCol.setChecked(activated)
		self.ui.toggleButtonExp.setChecked(activated)
		if activated:
			self.ui.toggleButtonExp.setText(self.tr("Activated"))
			self.ui.toggleButtonExp.setIcon(QtGui.QIcon(":/edit_icon/ok.png"))
			self.ui.toggleButtonCol.setIcon(QtGui.QIcon(":/edit_icon/ok.png"))
		else:
			self.ui.toggleButtonExp.setText(self.tr("Deactivated"))
			self.ui.toggleButtonExp.setIcon(QtGui.QIcon(":/edit_icon/close.png"))
			self.ui.toggleButtonCol.setIcon(QtGui.QIcon(":/edit_icon/close.png"))

	def setExpanded(self, value=None):
		"""Set if a item is expanded or not

		Expand are set hiding self.ui.collapsedWid and showing
		self.ui.expandedWid. This widgets have fixed vertical sizePolicy set.
		@param	self		A ListItemWidget instance
		@param	value		Bool. If true, set item expanded
		"""
		# If None, toggle
		if value == None:
			value = not self.expanded

		if value:
			self.listItem.setSelected(True)
			self.ui.collapsedWid.hide()
			self.ui.expandedWid.show()
			self.listItem.setSizeHint(self.ui.expandedWid.size())
		else:
			self.ui.expandedWid.hide()
			self.ui.collapsedWid.show()
			self.listItem.setSizeHint(self.ui.collapsedWid.size())

		self.expanded = value

	def config(self):
		"""Show module's configuration dialog

		@param	self		A LTCModuleParser instance
		"""
		self.moduleparser.configModule(self.module, self.parent)
		self.setActivated(self.activated)


