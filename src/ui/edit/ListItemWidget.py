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

from ui.edit.Ui_listItemWidget import Ui_listItemWidget

class ListItemWidget(QtGui.QWidget):
	"""Creates the QListWidgetItem widget of a module into cateogory"""
	def __init__(self, prettyname, description, configurable, parent=None):
		"""Instantiate a ListItemWidget widget

		containing a option in category
		@param	self		A ListItemWidget instance
		@param	prettyname	A string containing pretty name of module
		@param	description	A string containing rich text description
		@param	configurable	Bool. True if module is configurable
		@param	activated	Bool. Initial state of module
		@param	parent		Parent QtGui.QListWidget
		"""
		self.prettyname = prettyname
		self.description = description
		self.configurable = configurable
		self.activated = None
		self.expanded = False

		self.parent = parent

		self.listItem = QtGui.QListWidgetItem(parent)

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_listItemWidget()
		self.ui.setupUi(self)

		self.ui.expandedWid.hide()

		self.ui.prettyLabel.setText(prettyname)
		self.ui.prettyLabel_2.setText(prettyname)
		self.ui.descriptionText.setText(description)

		self.parent.setItemWidget(self.listItem, self)
		#self.listItem.setSizeHint(self.size())
		self.setExpanded(False)

	def setActivated(self, activated):
		"""Set this module activated or not

		@param	self		A ListItemWidget instance
		@param	activated	Bool
		"""
		self.activated = activated

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

