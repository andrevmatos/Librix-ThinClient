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

		# Demonstration users list
		_userDict = {'listItem': None, 'treeItem': None, 'profileItem': None, 'profile': ''}
		self._users = {'andre': dict(_userDict), 'ivan': dict(_userDict), 'roberto': dict(_userDict), 'guilherme': dict(_userDict), 'david': dict(_userDict), 'carvalho': dict(_userDict)}
		self._profiles = {'Profile 1': [], 'Profile 2': [], 'Profile 3': []}

		self.setupWidgets()

	def _dragEnterEvent(self, event):
		if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
			#event._data = self.
			event.accept()
		else:
			event.ignore()

	def _profilesDropEvent(self, event):
		if event.source() != self.Users.usersList:
			return
		self.addUser2Profile(event.source().selectedItems(), self.Users.profilesTree.itemAt(event.pos()))

	def _userDropEvent(self, event):
		if event.source() != self.Users.profilesTree:
			return
		self.delUser2Profile(event.source().selectedItems())

	def setupWidgets(self):
		""" Execute the options widgets configuration
		@param self a Main() instance
		"""
		# TODO: implement qt translate, instead of pure strings
		# User widget configuration routines
		self.Users = Ui_UsersWidget()
		self.Users.widget = QtGui.QWidget()
		self.Users.setupUi(self.Users.widget)
		self.Users.Tab = self.makeListItemWidget(self.ui.listWidget, 'Users', QtGui.QIcon(":/user_icon/system-users.png"))
		self.ui.horizontalLayout.addWidget(self.Users.widget)
		self.Users.widget.hide()

		# Edit widget configuration routines
		self.Edit = Ui_EditWidget()
		self.Edit.widget = QtGui.QWidget()
		self.Edit.setupUi(self.Edit.widget)
		self.Edit.Tab = self.makeListItemWidget(self.ui.listWidget, 'Edit Profiles', QtGui.QIcon(":/edit_icon/document-edit.png"))
		self.makeProfilesToolBar()
		self.ui.horizontalLayout.addWidget(self.Edit.widget)
		self.Edit.widget.hide()

		# Export widget configuration routines
		self.Export = Ui_ExportWidget()
		self.Export.widget = QtGui.QWidget()
		self.Export.setupUi(self.Export.widget)
		self.Export.Tab = self.makeListItemWidget(self.ui.listWidget, 'Import/Export', QtGui.QIcon(":/export_icon/fork.png"))
		self.ui.horizontalLayout.addWidget(self.Export.widget)
		self.Export.widget.hide()

		_users = list(self._users.keys())
		_users.sort()
		for i in _users:
			self._users[i]['listItem'] = QtGui.QListWidgetItem(QtGui.QIcon(":/user_icon/user.png"), i, self.Users.usersList)

		_profiles = list(self._profiles)
		_profiles.sort()
		for i in _profiles:
			self._profiles[i].append(QtGui.QTreeWidgetItem(self.Users.profilesTree, [i]))
			self._profiles[i][0].setExpanded(True)

		self.Users.usersList.setAcceptDrops(True)
		self.Users.usersList.dragEnterEvent = self._dragEnterEvent
		self.Users.usersList.dropEvent = self._userDropEvent
		self.Users.profilesTree.dragEnterEvent = self._dragEnterEvent
		self.Users.profilesTree.dropEvent = self._profilesDropEvent

		QtCore.QObject.connect(self.ui.listWidget,
			QtCore.SIGNAL("currentItemChanged(QListWidgetItem *,QListWidgetItem *)"), self.activateTab)
		QtCore.QObject.connect(self.Users.add,
			QtCore.SIGNAL("clicked()"), self.addUser2Profile)
		QtCore.QObject.connect(self.Users.remove,
			QtCore.SIGNAL("clicked()"), self.delUser2Profile)

		self.currentOptionsWidgets = self.Users.widget
		self.ui.listWidget.item(0).setSelected(True)

	def addUser2Profile(self, _User = None, _profile = None):
		""" Get the user in the self.usersList and add it to self.profilesTree
		@param self a Main( instance
		@param _User a list of QtGui.QListWidgetItem or QtGui.QTreeWidgetItem users items
		@param _profile a root QtGui.QTreeWidgetItem (It'll take the first selected root, if not given)
		"""
		_user = []
		if not _User:
			_User = self.Users.usersList.selectedItems()
		for U in _User:
			try:
				_user.append(U.text())
			except:
				_user.append(U.text(0))
		if not _profile:
			for i in self.Users.profilesTree.selectedItems():
				if not i.parent():
					_profile = i
					break
		for u in _user:
			if _profile.parent():
				_profile = _profile.parent()
			if self._users[u]['treeItem']:
				self._users[u]['profileItem'].removeChild(self._users[u]['treeItem'])
				self._users[u]['treeItem'] = None
				self._users[u]['profileItem'] = None
				self._users[u]['profile'] = ''
			self._users[u]['treeItem'] = QtGui.QTreeWidgetItem(_profile, [u])
			self._users[u]['profileItem'] = _profile
			self._users[u]['profile'] = _profile.text(0)

	def delUser2Profile(self, _User = None):
		""" Get the user in the self.usersList and add it to self.profilesTree
		@param self a Main() instance
		@param _User a QtGui.QTreeWidgetItem list of non root elements. Will pass the roots
		"""
		if not _User:
			_User = self.Users.profilesTree.selectedItems()
		for U in _User:
			U.text(0)
			if not U.parent():
				continue
			else:
				u = U.text(0)
			if self._users[u]['treeItem']:
				self._users[u]['profileItem'].removeChild(self._users[u]['treeItem'])
				self._users[u]['treeItem'] = None
				self._users[u]['profileItem'] = None
				self._users[u]['profile'] = ''

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

		self.Edit.ToolBar.addSeparator()

		self.Edit.ToolBar.EditAction = QtGui.QAction(QtGui.QIcon(":/profileAction/document-edit.png"),
		"Edit Profile", self.Edit.ToolBar)
		self.Edit.ToolBar.addAction(self.Edit.ToolBar.EditAction)
		self.Edit.ToolBar.DuplicateAction = QtGui.QAction(QtGui.QIcon(":/profileAction/document-edit-verify.png"),
		"Duplicate Profile", self.Edit.ToolBar)
		self.Edit.ToolBar.addAction(self.Edit.ToolBar.DuplicateAction)
		self.Edit.horizontalLayout_2.addWidget(self.Edit.ToolBar)

	def makeListItemWidget(self, parentList, text, icon):
		""" Create a Widget to put as item in leftList
		@param self A Main() instance
		@param parentList QtGui.QListWidget object
		@param text String to use as title of tab
		@param icon QtGui.QIcon object, to use as icon of tab
		"""
		_listItem = QtGui.QListWidgetItem(parentList)
		_listItemWidget = QtGui.QWidget(parentList)
		_vboxLayout = QtGui.QVBoxLayout(_listItemWidget)

		_sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		_sizePolicy.setHorizontalStretch(0)
		_sizePolicy.setVerticalStretch(0)
		_sizePolicy.setHeightForWidth(_listItemWidget.sizePolicy().hasHeightForWidth())

		_sizePolicyM = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
		_sizePolicyM.setHorizontalStretch(0)
		_sizePolicyM.setVerticalStretch(0)
		_sizePolicyM.setHeightForWidth(_listItemWidget.sizePolicy().hasHeightForWidth())

		_listItem.setSizeHint(QtCore.QSize(0, 78))
		_listItemWidget.setMinimumSize(QtCore.QSize(0, 78))

		_listItemWidget.setSizePolicy(_sizePolicy)
		_listItemWidget.setLayoutDirection(QtCore.Qt.LeftToRight)

		_iconLabel = QtGui.QLabel(_listItemWidget)
		_iconLabel.setMaximumSize(QtCore.QSize(300, 48))
		_iconLabel.setAlignment(QtCore.Qt.AlignCenter)
		_iconLabel.setPixmap(icon.pixmap(QtCore.QSize(48, 48)))
		_iconLabel.setSizePolicy(_sizePolicyM)
		_vboxLayout.addWidget(_iconLabel)

		_nameLabel = QtGui.QLabel('<b>{0}</b>'.format(text), _listItemWidget)
		_nameLabel.setMaximumSize(300, 20)
		_nameLabel.setAlignment(QtCore.Qt.AlignCenter)
		_nameLabel.setSizePolicy(_sizePolicyM)
		_vboxLayout.addWidget(_nameLabel)

		parentList.setItemWidget(_listItem, _listItemWidget)

		return _listItem


def main():
	""" The program main loop """
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
