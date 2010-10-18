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
from ui.Ui_profileEdit import Ui_EditProfile
from ui.Ui_configProfileEdit import Ui_configsWidget

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
		self.profiles = {
			'Profile 1': {},
			'Profile 2': {},
			'Profile 3': {},
		}
		for p in self.profiles:
			for c in self.profilesFalse:
				self.profiles[p][c] = {}
				for o in self.profilesFalse[c]:
					self.profiles[p][c][o] = choice([False, True])

		self.setupWidgets()

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

		# Main connects
		QtCore.QObject.connect(self.ui.listWidget,
			QtCore.SIGNAL("currentItemChanged(QListWidgetItem *,QListWidgetItem *)"), self.activateTab)
		# Users tab connects
		QtCore.QObject.connect(self.Users.add,
			QtCore.SIGNAL("clicked()"), self.addUser2Profile)
		QtCore.QObject.connect(self.Users.remove,
			QtCore.SIGNAL("clicked()"), self.delUser2Profile)
		# Edit tab connects
		QtCore.QObject.connect(self.Edit.addButton, QtCore.SIGNAL("clicked()"), self.addProfile)
		QtCore.QObject.connect(self.Edit.delButton, QtCore.SIGNAL("clicked()"), self.delProfile)
		QtCore.QObject.connect(self.Edit.editButton, QtCore.SIGNAL("clicked()"), self.editProfile)
		QtCore.QObject.connect(self.Edit.duplicateButton, QtCore.SIGNAL("clicked()"), self.duplicateProfile)

		self.currentOptionsWidgets = self.Users.widget
		self.ui.listWidget.item(0).setSelected(True)


	def profilesRefresh(self):
		""" Repopulate self.Users.profilesTree
		@param self a Main() instance
		"""
		#TODO: merge populateLists and profilesRefresh

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
			try:
				P = self.Users.profilesTree.findItems(p, QtCore.Qt.MatchExactly)[0]
				QtGui.QTreeWidgetItem(P, [u])
			except: print("@@@@@@@@", p)

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
		self.Edit.current = self.Edit.profileSummaryFrame
		self.Edit.profileEdit = None

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
		if self.Edit.current.widget != self.Edit.profileSummaryFrame.widget:
			self.Edit.current.widget.hide()
			self.Edit.profileSummaryFrame.widget.show()
			self.Edit.current = self.Edit.profileSummaryFrame
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
		_l = list(self.profiles[_profile].keys())
		_l.sort()
		for c in _l:
			_config = "<h4>{0}:</h4>\n".format(c)
			_m = list(self.profiles[_profile][c].keys())
			_m.sort()
			for i in _m:
				_config += "<h6> ➜ {0}: ".format(i)
				if self.profiles[_profile][c][i]:
					_config += "<font color=green><b>On</b></font></h6>\n"
				else:
					_config += "<font color=red><b>Off</b></font></h6>\n"
			if not c in _summary._configsWidgets:
				_summary._configsWidgets[c] = QtGui.QLabel()
				_summary.horizontalLayout.addWidget(_summary._configsWidgets[c])
			_summary._configsWidgets[c].setText(_config)

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

	def addProfile(self):
		""" Creates a new profile
		@param self a Main() instance
		"""
		self.new_profiles_count += 1
		n = 'New Profile {0}'.format(self.new_profiles_count)
		title = QtGui.QInputDialog.getText(self.Edit.widget, "Profile Name",
			"Enter the new profile name:", text = n)[0]
		if not title:
			return
		self.profiles[title] = self.profilesFalse.copy()
		self.profilesRefresh()
		self.Edit.profilesList.findItems(title,
			QtCore.Qt.MatchExactly)[0].setSelected(True)
		self.activateEditProfileSummary(self.Edit.profilesList.findItems(title,
			QtCore.Qt.MatchExactly)[0])

	def delProfile(self):
		""" Delete a profile
		@param self a Main() instance
		"""
		_profile = self.Edit.profilesList.selectedItems()
		if not _profile:
			return
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
		_profile = self.Edit.profilesList.selectedItems()
		if _profile:
			_profile = _profile[0].text()
		else:
			return
		self.profileEdit(_profile)

	def duplicateProfile(self):
		""" Creates a new profile from a existing one
		@param self a Main() instance
		"""
		self.new_profiles_count += 1
		p = self.Edit.profilesList.selectedItems()
		if not p:
			return
		p = p[0].text()
		n = '{0}_{1}'.format(p, self.new_profiles_count)
		title = QtGui.QInputDialog.getText(self.Edit.widget, "Profile Name",
			"Enter the destination profile name:", text = n)[0]
		if not title:
			return
		self.profiles[title] = dict(self.profiles[p])
		self.profilesRefresh()
		self.Edit.profilesList.findItems(title,
			QtCore.Qt.MatchExactly)[0].setSelected(True)
		self.activateEditProfileSummary(self.Edit.profilesList.findItems(title,
			QtCore.Qt.MatchExactly)[0])

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


	def profileEdit(self, profile):
		""" Build the profile edit widget
		@param self a Main() instance
		@param profile a string containing the profile name
		"""

		if not self.Edit.profileEdit:
			self.Edit.profileEdit = Ui_EditProfile()
			self.Edit.profileEdit.widget = QtGui.QWidget()
			self.Edit.profileEdit.setupUi(self.Edit.profileEdit.widget)
			self.Edit.profileEdit.page.close()

			self.Edit.profileEdit.configs = {}
			self.Edit.verticalLayout_4.addWidget(self.Edit.profileEdit.widget)
			self.Edit.profileEdit.widget.hide()

		self.Edit.profileEdit.profile = profile
		self.Edit.profileEdit.profileName.setText(profile)
		while self.Edit.profileEdit.configToolBox.count():
			self.Edit.profileEdit.configToolBox.removeItem(0)

		for c in self.profiles[profile]:
			if not c in self.Edit.profileEdit.configs:
				self.Edit.profileEdit.configs[c] = {'config': None, 'buttons': []}
			else:
				for b in self.Edit.profileEdit.configs[c]['buttons']:
					b.close()
					self.Edit.profileEdit.configs[c]['buttons'].remove(b)
				self.Edit.profileEdit.configs[c]['config'].widget.close()
				self.Edit.profileEdit.configs[c] = {'config': None, 'buttons': []}

			self.Edit.profileEdit.configs[c]['config'] = Ui_configsWidget()
			self.Edit.profileEdit.configs[c]['config'].widget = QtGui.QWidget()
			self.Edit.profileEdit.configs[c]['config'].setupUi(self.Edit.profileEdit.configs[c]['config'].widget)

			_options = list(self.profiles[profile][c].keys())
			_options.sort()
			for o in _options:
				button = QtGui.QPushButton(o)
				button.setCheckable(True)
				if self.profiles[profile][c][o]:
					button.setChecked(True)
				self.Edit.profileEdit.configs[c]['buttons'].append(button)
				self.Edit.profileEdit.configs[c]['config'].ConfigVerticalLayout.addWidget(button)

			self.Edit.profileEdit.configToolBox.addItem(self.Edit.profileEdit.configs[c]['config'].widget, c)

		QtCore.QObject.connect(self.Edit.profileEdit.buttonBox, QtCore.SIGNAL("clicked(QAbstractButton *)"),
			self.readProfileConfig)

		if self.Edit.current != self.Edit.profileEdit:
			self.Edit.current.widget.hide()
			self.Edit.current = self.Edit.profileEdit
		self.Edit.profileEdit.widget.show()

	def readProfileConfig(self, button):
		""" Read and write (or not) configurations on editProfile
		@param self a Main() instance
		"""
		name = self.Edit.profileEdit.profile
		if not name in self.profiles:
			return
		if self.Edit.profileEdit.buttonBox.standardButton(button) == QtGui.QDialogButtonBox.Apply:
			if self.Edit.profileEdit.profileName.text() != name:
				newname = self.Edit.profileEdit.profileName.text()
				self.profiles[newname] = self.profiles[name].copy()
				del self.profiles[name]
				for u in self.users:
					if self.users[u]['profile'] == name:
						self.users[u]['profile'] = newname
				name = newname
			for c in self.Edit.profileEdit.configs:
				for b in self.Edit.profileEdit.configs[c]['buttons']:
					self.profiles[name][c][b.text()] = b.isChecked()

		self.profilesRefresh()
		self.Edit.profilesList.findItems(name,
			QtCore.Qt.MatchExactly)[0].setSelected(True)
		self.activateEditProfileSummary(self.Edit.profilesList.findItems(name,
			QtCore.Qt.MatchExactly)[0])


def main():
	""" The program main loop """
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
