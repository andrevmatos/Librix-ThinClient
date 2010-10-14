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
from random import choice
from PyQt4 import QtCore,QtGui

from ui.Ui_mainWindow import Ui_ThinClient
from ui.Ui_usersWidget import Ui_UsersWidget
from ui.Ui_editWidget import Ui_EditWidget
from ui.Ui_exportWidget import Ui_ExportWidget
from ui.Ui_tabItemWidget import Ui_tabWidget
from ui.Ui_profileSummary import Ui_Summary

TF = [True, False]

# Create a class for our main window
class Main(QtGui.QMainWindow):
	def __init__(self):
		""" Creates a Main() instance, and setup the mainWindow options
		@param self a Main() instance
		"""
		QtGui.QMainWindow.__init__(self)

		self.ui = Ui_ThinClient()
		self.ui.setupUi(self)

		# Demonstration users and profiles list
		_userDict = { 'profile': ''}
		self.users = {
			'andre': _userDict.copy(),
			'ivan': _userDict.copy(),
			'roberto': _userDict.copy(),
			'guilherme': _userDict.copy(),
			'david': _userDict.copy(),
			'carvalho': _userDict.copy()
		}

		self.new_profiles_count = 0
		self.profilesFalse = {
			'config': {
				'hardware': {
					'option 1': False,
					'option 2': False,
					'option 3': False,
					'option 4': False
				},
				'software': {
					'option 5': False,
					'option 6': False,
					'option 7': False,
					'option 8': False
				}
			}
		}
		self.profiles = {
			'Profile 1': {
				'config': {
					'hardware': {
						'option 1': choice(TF),
						'option 2': choice(TF),
						'option 3': choice(TF),
						'option 4': choice(TF)
					},
					'software': {
						'option 5': choice(TF),
						'option 6': choice(TF),
						'option 7': choice(TF),
						'option 8': choice(TF)
					}
				}
			},
			'Profile 2': {
				'config': {
					'hardware': {
						'option 1': choice(TF),
						'option 2': choice(TF),
						'option 3': choice(TF),
						'option 4': choice(TF)
					},
					'software': {
						'option 5': choice(TF),
						'option 6': choice(TF),
						'option 7': choice(TF),
						'option 8': choice(TF)
					}
				}
			},
			'Profile 3': {
				'config': {
					'hardware': {
						'option 1': choice(TF),
						'option 2': choice(TF),
						'option 3': choice(TF),
						'option 4': choice(TF)
					},
					'software': {
						'option 5': choice(TF),
						'option 6': choice(TF),
						'option 7': choice(TF),
						'option 8': choice(TF)
					}
				}
			}
		}

		self.setupWidgets()

	def _dragEnterEvent(self, event):
		""" Qt Event of Drag actions
		@param self a Main() instance
		@param event a QtGui.QDragEnterEvent object
		"""
		if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
			event.accept()
		else:
			event.ignore()

	def _profilesDropEvent(self, event):
		""" Qt Event of Drop actions on profiles tree of Users tab
		@param self a Main() instance
		@param event a QtGui.QDropEvent object
		"""
		_users = []
		if event.source() == self.Users.usersList:
			for U in event.source().selectedItems():
				_users.append(U.text())
		elif event.source() == self.Users.profilesTree:
			for U in event.source().selectedItems():
				if U.parent():
					_users.append(U.text(0))
		else:
			return
		_profile = self.Users.profilesTree.itemAt(event.pos()).text(0)
		self.addUser2Profile(_users, _profile)

	def _userDropEvent(self, event):
		""" Qt Event of Drop actions on users list of Users tab
		@param self a Main() instance
		@param event a QtGui.QDropEvent object
		"""
		if event.source() != self.Users.profilesTree:
			return
		_users = []
		for U in event.source().selectedItems():
			if U.parent():
				_users.append(U.text(0))
		self.delUser2Profile(_users)

	def populateLists(self):
		""" Create the lists and tree in self.Users.usersList, self.Users.profilesTree and self.Edit.profilesList
		@param self a Main() instance
		"""
		users = list(self.users.keys())
		users.sort()
		for i in users:
			QtGui.QListWidgetItem(QtGui.QIcon(":/user_icon/user.png"), i, self.Users.usersList)

		self.Users.usersList.setAcceptDrops(True)
		self.Users.usersList.dragEnterEvent = self._dragEnterEvent
		self.Users.usersList.dropEvent = self._userDropEvent
		self.Users.profilesTree.dragEnterEvent = self._dragEnterEvent
		self.Users.profilesTree.dropEvent = self._profilesDropEvent

		self.Users.profileSummaryFrame = self.makeProfileFrame()
		self.Users.summaryDock.setWidget(self.Users.profileSummaryFrame.widget)

		self.Edit.profileSummaryFrame = self.makeProfileFrame()
		self.Edit.verticalLayout_4.addWidget(self.Edit.profileSummaryFrame.widget)
		self.Edit.profilesList.previous = self.Edit.profileSummaryFrame.widget

		self.profilesRefresh()

		QtCore.QObject.connect(self.Users.profilesTree,
			QtCore.SIGNAL("currentItemChanged(QTreeWidgetItem *,QTreeWidgetItem *)"), self.activateUserProfileSummary)
		QtCore.QObject.connect(self.Edit.profilesList,
			QtCore.SIGNAL("currentItemChanged(QListWidgetItem *,QListWidgetItem *)"), self.activateEditProfileSummary)

	def activateUserProfileSummary(self, treeItem):
		""" Show summary when a Profile was selected on self.Users.profilesTree
		@param self a Main() instance
		@param listItem a QtGui.QTreeWidgetItem profile object
		"""
		if not treeItem: return
		if treeItem.parent():
			treeItem = treeItem.parent()
		self.setSummary(treeItem.text(0), self.Users.profileSummaryFrame)


	def activateEditProfileSummary(self, listItem):
		""" Show summary when a Profile was selected on self.Edit.profilesList
		@param self a Main() instance
		@param listItem a QtGui.QListWidgetItem profile object
		"""
		if not listItem: return
		if self.Edit.profilesList.previous != self.Edit.profileSummaryFrame.widget:
			self.Edit.profilesList.previous.hide()
			self.Edit.profileSummaryFrame.widget.show()
		self.setSummary(listItem.text(), self.Edit.profileSummaryFrame)

	def makeProfileFrame(self):
		""" Create and return a widget with formated text to summary of profile
		@param self a Main() instance
		"""
		_summary = Ui_Summary()
		_summary.widget = QtGui.QWidget()
		_summary.setupUi(_summary.widget)

		_summary._configsWidgets = {}

		return _summary

	def setSummary(self, _profile, _summary):
		""" Set the summary of _profile on _label
		@param self a Main() instance
		@param _profile a string containing the name of the profile
		@param _summary a Ui_Summary instance, with a .widget object where the configs will be set
		"""
		_summary._title.setText("<h2><b>Name: <font color=blue>{0}</font></h2>\n".format(_profile))

		# for each category, creates a QLabel and add the configurations
		_l = list(self.profiles[_profile]['config'].keys())
		_l.sort()
		for c in _l:
			_config = "<h4>{0}:</h4>\n".format(c)
			_m = list(self.profiles[_profile]['config'][c].keys())
			_m.sort()
			for i in _m:
				_config += "<h6> ➜ {0}: ".format(i)
				if self.profiles[_profile]['config'][c][i]:
					_config += "<font color=green><b>On</b></font></h6>\n"
				else:
					_config += "<font color=red><b>Off</b></font></h6>\n"
			if not c in _summary._configsWidgets:
				_summary._configsWidgets[c] = QtGui.QLabel()
				_summary.horizontalLayout.addWidget(_summary._configsWidgets[c])
			_summary._configsWidgets[c].setText(_config)


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

		self.populateLists()

		QtCore.QObject.connect(self.ui.listWidget,
			QtCore.SIGNAL("currentItemChanged(QListWidgetItem *,QListWidgetItem *)"), self.activateTab)
		QtCore.QObject.connect(self.Users.add,
			QtCore.SIGNAL("clicked()"), self.addUser2Profile)
		QtCore.QObject.connect(self.Users.remove,
			QtCore.SIGNAL("clicked()"), self.delUser2Profile)

		self.currentOptionsWidgets = self.Users.widget
		self.ui.listWidget.item(0).setSelected(True)


	def profilesRefresh(self):
		""" Repopulate self.Users.profilesTree
		@param self a Main() instance
		"""

		self.Users.profilesTree.clear()
		while self.Edit.profilesList.count():
			self.Edit.profilesList.takeItem(0)
		_profiles = list(self.profiles.keys())
		_profiles.sort()
		_icon = QtGui.QIcon(":/edit_icon/profiles.png")
		for p in _profiles:
			QtGui.QTreeWidgetItem(self.Users.profilesTree, [p]).setExpanded(True)
			QtGui.QListWidgetItem(_icon, p, self.Edit.profilesList)
		_users = list(self.users.keys())
		_users.sort()
		for u in _users:
			p = self.users[u]['profile']
			if not p: continue
			P = self.Users.profilesTree.findItems(p, QtCore.Qt.MatchExactly)[0]
			QtGui.QTreeWidgetItem(P, [u])

	def addUser2Profile(self, _users = [], _profile = ''):
		""" Get the user in the self.usersList and add it to self.profilesTree
		@param self a Main( instance
		@param _users a list of strings usernames to add to _profile
		@param _profile a string containing the destiny profile name
		"""
		if not _users:
			for U in self.Users.usersList.selectedItems():
				try:
					_users.append(U.text())
				except:
					if U.parent():
						_users.append(U.text(0))
		if not _profile:
			for i in self.Users.profilesTree.selectedItems():
				if not i.parent():
					_profile = i.text(0)
					break
		if not _profile and self.Users.profilesTree.selectedItems():
			_profile = self.Users.profilesTree.selectedItems()[0].text(0)
		if _profile in self.users:
			_profile = self.users[_profile]['profile']
		if not _profile:
			return

		for u in _users:
			self.users[u]['profile'] = _profile

		self.profilesRefresh()

	def delUser2Profile(self, *_users):
		""" Get the user in the self.usersList and add it to self.profilesTree
		@param self a Main() instance
		@param _users A list of strings usernames to remove from profiles
		"""
		if len(_users) == 0:
			_users = []
		elif len(_users) == 1:
			_users = _users[0]
		if not _users:
			for U in self.Users.profilesTree.selectedItems():
				if U.parent():
					_users.append(U.text(0))

		for U in _users:
			self.users[U]['profile'] = ''

		self.profilesRefresh()

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

		QtCore.QObject.connect(self.Edit.ToolBar.AddAction, QtCore.SIGNAL("triggered()"), self.addProfile)
		QtCore.QObject.connect(self.Edit.ToolBar.DeleteAction, QtCore.SIGNAL("triggered()"), self.delProfile)
		QtCore.QObject.connect(self.Edit.ToolBar.EditAction, QtCore.SIGNAL("triggered()"), self.editProfile)
		QtCore.QObject.connect(self.Edit.ToolBar.DuplicateAction, QtCore.SIGNAL("triggered()"), self.duplicateProfile)

	def addProfile(self):
		""" Creates a new profile
		@param self a Main() instance
		"""
		self.new_profiles_count += 1
		n = 'New Profile {0}'.format(self.new_profiles_count)
		self.profiles[n] = self.profilesFalse
		self.profilesRefresh()
		self.Edit.profilesList.findItems(n,
			QtCore.Qt.MatchExactly)[0].setSelected(True)
		self.activateEditProfileSummary(self.Edit.profilesList.findItems(n,
			QtCore.Qt.MatchExactly)[0])

	def delProfile(self):
		""" Delete a profile
		@param self a Main() instance
		"""
		_profile = self.Edit.profilesList.selectedItems()
		_p = list(self.profiles.keys())
		_p.sort()
		for p in _profile:
			try:
				p = p.text()
				k = _p.index(p)-1
				del self.profiles[p]
			except: pass
			for u in self.users:
				if self.users[u]['profile'] == p:
					self.users[u]['profile'] = ''
		self.profilesRefresh()
		_p = list(self.profiles.keys())
		_p.sort()
		self.Edit.profilesList.findItems(_p[k],
			QtCore.Qt.MatchExactly)[0].setSelected(True)
		self.activateEditProfileSummary(self.Edit.profilesList.findItems(_p[k],
			QtCore.Qt.MatchExactly)[0])

	def editProfile(self):
		""" Edit a profile
		@param self a Main() instance
		"""
		# TODO: implement edit profile function
		pass

	def duplicateProfile(self):
		""" Creates a new profile from a existing one
		@param self a Main() instance
		"""
		self.new_profiles_count += 1
		p = self.Edit.profilesList.selectedItems()[0].text()
		n = '{0}_{1}'.format(p, self.new_profiles_count)
		self.profiles[n] = self.profiles[p].copy()
		self.profilesRefresh()
		self.Edit.profilesList.findItems(n,
			QtCore.Qt.MatchExactly)[0].setSelected(True)
		self.activateEditProfileSummary(self.Edit.profilesList.findItems(n,
			QtCore.Qt.MatchExactly)[0])

	def makeListItemWidget(self, parentList, text, icon):
		""" Create a Widget to put as item in leftList
		@param self A Main() instance
		@param parentList QtGui.QListWidget object
		@param text String to use as title of tab
		@param icon QtGui.QIcon object, to use as icon of tab
		"""
		listItem = QtGui.QListWidgetItem(parentList)
		tabWidget = Ui_tabWidget()
		tabWidget.widget = QtGui.QWidget(parentList)
		tabWidget.setupUi(tabWidget.widget)

		listItem.setSizeHint(tabWidget.widget.size())

		tabWidget.iconLabel.setPixmap(icon.pixmap(QtCore.QSize(48, 48)))
		tabWidget.titleLabel.setText('<b>{0}</b>'.format(text))

		parentList.setItemWidget(listItem, tabWidget.widget)

		return listItem


def main():
	""" The program main loop """
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
