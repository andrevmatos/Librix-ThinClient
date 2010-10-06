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

import sys
from PyQt4 import QtCore,QtGui

from ui.mainWindow import Ui_ThinClient
from ui.usersWidget import Ui_UsersWidget
from ui.editWidget import Ui_EditWidget
from ui.exportWidget import Ui_ExportWidget

# Create a class for our main window
class Main(QtGui.QMainWindow):
	def __init__(self):
		""" Creates a Main() instance, and setup the mainWindow options
		@param self a Main() instance
		"""
		QtGui.QMainWindow.__init__(self)

		self.ui = Ui_ThinClient()
		self.ui.setupUi(self)

		self.Users = Ui_UsersWidget()
		self.Users.widget = QtGui.QWidget()
		self.Users.setupUi(self.Users.widget)

		self.Edit = Ui_EditWidget()
		self.Edit.widget = QtGui.QWidget()
		self.Edit.setupUi(self.Edit.widget)
		self.makeProfilesToolBar()

		self.Export = Ui_ExportWidget()
		self.Export.widget = QtGui.QWidget()
		self.Export.setupUi(self.Export.widget)

		self.Users.Tab = self.makeListItemWidget(self.ui.listWidget, 'Users', QtGui.QIcon(":/user_icon/system-users.png"))
		self.Edit.Tab = self.makeListItemWidget(self.ui.listWidget, 'Edit Profiles', QtGui.QIcon(":/edit_icon/document-edit.png"))
		self.Export.Tab = self.makeListItemWidget(self.ui.listWidget, 'Import/Export', QtGui.QIcon(":/export_icon/fork.png"))

		self.ui.horizontalLayout.addWidget(self.Users.widget)
		self.Users.widget.hide()
		self.ui.horizontalLayout.addWidget(self.Edit.widget)
		self.Edit.widget.hide()
		self.ui.horizontalLayout.addWidget(self.Export.widget)
		self.Export.widget.hide()

		self.currentOptionsWidgets = self.Users.widget

		QtCore.QObject.connect(self.ui.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.activateTab)

		self.ui.listWidget.item(0).setSelected(1)
		self.activateTab(self.Users.Tab)

	def activateTab(self, listItem):
		""" Hide the current widget on main window and show the widget of selected Tab
		@param self A Main() instance
		@param listItem A QtGui.QListWidgetItem object
		"""
		self.currentOptionsWidgets.hide()
		if listItem == self.Users.Tab:
			self.Users.widget.show()
			self.currentOptionsWidgets = self.Users.widget
		elif listItem == self.Edit.Tab:
			self.Edit.widget.show()
			self.currentOptionsWidgets = self.Edit.widget
		elif listItem == self.Export.Tab:
			self.Export.widget.show()
			self.currentOptionsWidgets = self.Export.widget

	def makeProfilesToolBar(self):
		""" Make Profiles Edit toolbar
		@param self A Main() instance
		"""
		self.Edit.ToolBar = QtGui.QToolBar("Edit Profile", None)
		self.Edit.ToolBar.AddAction = QtGui.QAction(QtGui.QIcon(":/profileAction/document-new.png"),
			"New Profile", self.Edit.ToolBar)
		self.Edit.ToolBar.addAction(self.Edit.ToolBar.AddAction)
		self.Edit.ToolBar.DeleteAction = QtGui.QAction(QtGui.QIcon(":/profileAction/document-close.png"),
		"Delete Profile", self.Edit.ToolBar)
		self.Edit.ToolBar.addAction(self.Edit.ToolBar.DeleteAction)
		self.Edit.ToolBar.EditAction = QtGui.QAction(QtGui.QIcon(":/profileAction/document-edit.png"),
		"Edit Profile", self.Edit.ToolBar)
		self.Edit.ToolBar.addAction(self.Edit.ToolBar.EditAction)
		self.Edit.ToolBar.DuplicateAction = QtGui.QAction(QtGui.QIcon(":/profileAction/document-edit-verify.png"),
		"Duplicate Profile", self.Edit.ToolBar)
		self.Edit.ToolBar.addAction(self.Edit.ToolBar.DuplicateAction)
		self.Edit.horizontalLayout_2.addWidget(self.Edit.ToolBar)

	def makeListItemWidget(self, parentList, text, icon):
		""" Create a Widget to put into itens in leftList
		@param self A Main() instance
		@param parentList QtGui.QListWidget object
		@param text String to use as title of tab
		@param icon QtGui.QIcon object, to use as icon of tab
		"""
		listItem = QtGui.QListWidgetItem(parentList)
		listItemWidget = QtGui.QWidget(parentList)
		vboxLayout = QtGui.QVBoxLayout(listItemWidget)

		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(listItemWidget.sizePolicy().hasHeightForWidth())

		sizePolicyM = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
		sizePolicyM.setHorizontalStretch(0)
		sizePolicyM.setVerticalStretch(0)
		sizePolicyM.setHeightForWidth(listItemWidget.sizePolicy().hasHeightForWidth())

		listItem.setSizeHint(QtCore.QSize(0, 78))
		listItemWidget.setMinimumSize(QtCore.QSize(0, 78))

		listItemWidget.setSizePolicy(sizePolicy)
		listItemWidget.setLayoutDirection(QtCore.Qt.LeftToRight)

		iconLabel = QtGui.QLabel(listItemWidget)
		iconLabel.setMaximumSize(QtCore.QSize(300, 48))
		iconLabel.setAlignment(QtCore.Qt.AlignCenter)
		iconLabel.setPixmap(icon.pixmap(QtCore.QSize(48, 48)))
		iconLabel.setSizePolicy(sizePolicyM)
		vboxLayout.addWidget(iconLabel)

		nameLabel = QtGui.QLabel('<b>'+text, listItemWidget)
		nameLabel.setMaximumSize(300, 20)
		nameLabel.setAlignment(QtCore.Qt.AlignCenter)
		nameLabel.setSizePolicy(sizePolicyM)
		vboxLayout.addWidget(nameLabel)

		parentList.setItemWidget(listItem, listItemWidget)

		return listItem


def main():
	""" The program main loop """
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
