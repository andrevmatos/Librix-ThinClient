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
from copy import deepcopy
from PyQt4 import QtCore,QtGui

from ui.Ui_mainWindow import Ui_ThinClient
from ui.Ui_usersWidget import Ui_UsersWidget
from ui.Ui_editWidget import Ui_EditWidget
from ui.Ui_exportWidget import Ui_ExportWidget
from ui.Ui_tabItemWidget import Ui_tabWidget
from ui.Ui_profileSummary import Ui_Summary
from ui.Ui_profileEdit import Ui_EditProfile
from ui.Ui_configProfileEdit import Ui_configsWidget

from backend.librix_tcd import LibrixTCD

# Create a class for our main window
class Main(QtGui.QMainWindow):
	def __init__(self):
		""" Creates a Main() instance, and setup the mainWindow options

		@param	self		A Main() instance
		"""
		QtGui.QMainWindow.__init__(self)

		# Setup main UI
		self.ui = Ui_ThinClient()
		self.ui.setupUi(self)

		# Init users and profiles package
		self.tcd = LibrixTCD()

		# Demonstration users and profiles list
		self.new_profiles_count = 0

		self.setupWidgets()

	def setupWidgets(self):
		""" Execute the options widgets configuration

		@param	self		A Main() instance
		"""
		# TODO: implement qt translate, instead of pure strings
		# User widget configuration routines
		self.Users = Ui_UsersWidget()
		self.Users.widget = QtGui.QWidget()
		self.Users.setupUi(self.Users.widget)
		self.Users.Tab = self.makeTabItem(self.ui.listWidget,
			'Users', QtGui.QIcon(":/user_icon/system-users.png"))
		self.ui.horizontalLayout.addWidget(self.Users.widget)
		self.Users.widget.hide()
			# Drag'nDrop actions
		self.Users.usersList.setAcceptDrops(True)
		self.Users.usersList.dragEnterEvent = self._dragEnterEvent
		self.Users.usersList.dropEvent = self._userDropEvent
		self.Users.profilesTree.dragEnterEvent = self._dragEnterEvent
		self.Users.profilesTree.dropEvent = self._profilesDropEvent
			# Profile summary in Users tab
		self.Users.profileSummaryFrame = self.makeProfileFrame()
		self.Users.summaryDock.setWidget(
			self.Users.profileSummaryFrame.widget)

		# Edit widget configuration routines
		self.Edit = Ui_EditWidget()
		self.Edit.widget = QtGui.QWidget()
		self.Edit.setupUi(self.Edit.widget)
		self.Edit.Tab = self.makeTabItem(
			self.ui.listWidget, 'Edit Profiles',
			QtGui.QIcon(":/edit_icon/document-edit.png"))
		self.ui.horizontalLayout.addWidget(self.Edit.widget)
		self.Edit.widget.hide()
			#Profile summary in Edit tab
		self.Edit.profileSummaryFrame = self.makeProfileFrame()
		self.Edit.verticalLayout_4.addWidget(
			self.Edit.profileSummaryFrame.widget)
		self.Edit.current = self.Edit.profileSummaryFrame
		self.Edit.profileEdit = None

		# Export widget configuration routines
		self.Export = Ui_ExportWidget()
		self.Export.widget = QtGui.QWidget()
		self.Export.setupUi(self.Export.widget)
		self.Export.Tab = self.makeTabItem(self.ui.listWidget,
			'Import/Export', QtGui.QIcon(":/export_icon/fork.png"))
		self.ui.horizontalLayout.addWidget(self.Export.widget)
		self.Export.widget.hide()

		# Main connects
		QtCore.QObject.connect(self.ui.listWidget, QtCore.SIGNAL(
			"currentItemChanged(QListWidgetItem *,QListWidgetItem *)"),
			self.activateTab)
		# Users tab connects
		QtCore.QObject.connect(self.Users.add,
			QtCore.SIGNAL("clicked()"), self.addUser2Profile)
		QtCore.QObject.connect(self.Users.remove,
			QtCore.SIGNAL("clicked()"), self.delUser2Profile)
		QtCore.QObject.connect(self.Users.profilesTree, QtCore.SIGNAL(
			"currentItemChanged(QTreeWidgetItem *, QTreeWidgetItem *)"),
			self.activateUserProfileSummary)
		# Edit tab connects
		QtCore.QObject.connect(self.Edit.addButton,
			QtCore.SIGNAL("clicked()"), self.addProfile)
		QtCore.QObject.connect(self.Edit.delButton,
			QtCore.SIGNAL("clicked()"), self.delProfile)
		QtCore.QObject.connect(self.Edit.editButton,
			QtCore.SIGNAL("clicked()"), self.editProfile)
		QtCore.QObject.connect(self.Edit.duplicateButton,
			QtCore.SIGNAL("clicked()"), self.duplicateProfile)
		QtCore.QObject.connect(self.Edit.profilesList,
			QtCore.SIGNAL("currentItemChanged(QListWidgetItem *,\
			QListWidgetItem *)"), self.activateEditProfileSummary)

		self.profilesRefresh()

		self.currentOptionsWidgets = self.Users.widget
		self.ui.listWidget.item(0).setSelected(True)


	def profilesRefresh(self):
		""" Repopulate self.Users.profilesTree

		@param	self		A Main() instance
		"""

		self.Users.profilesTree.clear()
		self.Users.usersList.clear()
		self.Edit.profilesList.clear()

		for p in self.tcd.getProfilesList():
			QtGui.QTreeWidgetItem(self.Users.profilesTree,
				[p]).setExpanded(True)
			QtGui.QListWidgetItem(
				QtGui.QIcon(":/edit_icon/profiles.png"),
				p, self.Edit.profilesList)

		for u in self.tcd.getUsersList():
			U = QtGui.QListWidgetItem(
				QtGui.QIcon(":/user_icon/user.png"),
				u, self.Users.usersList)
			U.setToolTip("Profile: <b>{0}</b>".format(self.tcd.getUserProfile(u)))
			p = self.tcd.getUserProfile(u)
			if not p: continue
			P = self.Users.profilesTree.findItems(p,
				QtCore.Qt.MatchExactly)[0]
			QtGui.QTreeWidgetItem(P, [u])


	def activateUserProfileSummary(self, treeItem):
		""" Show summary when a Profile was selected on profilesTree

		@param	self		A Main() instance
		@param	treeItem	A QtGui.QTreeWidgetItem profile object
		"""
		if not treeItem: return
		if treeItem.parent():
			treeItem = treeItem.parent()
		self.setSummary(treeItem.text(0),
			self.Users.profileSummaryFrame)


	def activateEditProfileSummary(self, profile):
		""" Show summary of a profile

		@param	self		A Main() instance
		@param	profile	A profile name string to show
						or a QtGui.QListWidgetItem
		"""
		if not profile:
			return
		if type(profile) == QtGui.QListWidgetItem:
			profile = profile.text()

		if self.Edit.current != self.Edit.profileSummaryFrame:
			self.Edit.current.widget.hide()
			self.Edit.current = self.Edit.profileSummaryFrame
			self.Edit.current.widget.show()
		self.setSummary(profile, self.Edit.profileSummaryFrame)

		self.Edit.profilesList.findItems(profile,
			QtCore.Qt.MatchExactly)[0].setSelected(True)

	def makeProfileFrame(self):
		""" Create and return a widget with formated text to summary

		@param	self		A Main() instance
		@return			A Ui_Summary() instance with a
						.widget widget object
		"""
		summary = Ui_Summary()
		summary.widget = QtGui.QWidget()
		summary.setupUi(summary.widget)

		summary.configsWidgets = {}

		return summary

	def setSummary(self, profile, summary):
		""" Set the summary of _profile on _label

		@param	self		A Main() instance
		@param profile	A string containing the name of the profile
		@param summary	A Ui_Summary instance, with a
										.widget object where the
										configs will be set
		"""
		summary.title.setText("<h2><b>Name: \
			<font color=blue>{0}</font></b></h2>\n".format(profile))

		# for each category, creates a QLabel and add the configurations
		for c in self.tcd.getProfileCategoriesList(profile):
			config = "<h4>{0}:</h4>\n".format(c)

			for o in self.tcd.getOptionsList(profile, c):
				config += "<h6> ➜ {0}: ".format(o)
				if self.tcd.getOption(profile, c, o):
					config += "<font color=green><b>On</b></font></h6>\n"
				else:
					config += "<font color=red><b>Off</b></font></h6>\n"
			if not c in summary.configsWidgets:
				summary.configsWidgets[c] = QtGui.QLabel()
				summary.horizontalLayout.addWidget(summary.configsWidgets[c])
			summary.configsWidgets[c].setText(config)


	def profileEdit(self, profile):
		""" Build the profile edit widget

		@param	self		A Main() instance
		@param	profile	A string containing the profile name
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

		for c in self.tcd.getProfileCategoriesList(profile):
			if not c in self.Edit.profileEdit.configs:
				self.Edit.profileEdit.configs[c] = {
					'config': None, 'buttons': []}
			else:
				for b in self.Edit.profileEdit.configs[c]['buttons']:
					b.close()
					self.Edit.profileEdit.configs[c]['buttons'].remove(b)
				self.Edit.profileEdit.configs[c]['config'].widget.close()
				self.Edit.profileEdit.configs[c] = {
					'config': None, 'buttons': []}

			self.Edit.profileEdit.configs[c]['config'] = Ui_configsWidget()
			self.Edit.profileEdit.configs[c]['config'].widget = QtGui.QWidget()
			self.Edit.profileEdit.configs[c]['config'].setupUi(
				self.Edit.profileEdit.configs[c]['config'].widget)

			for o in self.tcd.getOptionsList(profile, c):
				button = QtGui.QPushButton(o)
				button.option = o
				button.setCheckable(True)
				if self.tcd.getOption(profile, c, o):
					button.setChecked(True)
				self.Edit.profileEdit.configs[c]['buttons'].append(button)
				self.Edit.profileEdit.configs[c]['config'
					].ConfigVerticalLayout.addWidget(button)

			self.Edit.profileEdit.configToolBox.addItem(
				self.Edit.profileEdit.configs[c]['config'].widget, c)

		QtCore.QObject.connect(self.Edit.profileEdit.buttonBox,
			QtCore.SIGNAL("clicked(QAbstractButton *)"), self.readProfileConfig)

		if self.Edit.current != self.Edit.profileEdit:
			self.Edit.current.widget.hide()
			self.Edit.current = self.Edit.profileEdit
		self.Edit.profileEdit.widget.show()

	def readProfileConfig(self, button):
		""" Read and write (or not) configurations on editProfile

		@param	self		A Main() instance
		"""
		name = self.Edit.profileEdit.profile
		if not name in self.tcd.getProfilesList():
			return
		if self.Edit.profileEdit.buttonBox.standardButton(button)\
			== QtGui.QDialogButtonBox.Apply:
			if self.Edit.profileEdit.profileName.text() != name:
				newname = self.Edit.profileEdit.profileName.text()
				self.tcd.moveProfile(name, newname)
				name = newname
			for c in self.Edit.profileEdit.configs:
				for b in self.Edit.profileEdit.configs[c]['buttons']:
					self.tcd.setOption(name, c, b.option, b.isChecked())

		self.profilesRefresh()
		self.activateEditProfileSummary(name)


	def addUser2Profile(self, users = [], profile = ''):
		""" Get the user in the self.usersList and add it to self.profilesTree

		@param 	self		A Main( instance
		@param	users	A list of strings usernames to add to _profile
		@param	profile	A string containing the destiny profile name
		"""
		_users = deepcopy(users)
		if not _users:
			for U in self.Users.usersList.selectedItems():
				try:
					_users.append(U.text())
				except:
					if U.parent():
						_users.append(U.text(0))
		if not profile:
			for P in self.Users.profilesTree.selectedItems():
				if not P.parent():
					profile = P.text(0)
				else:
					profile = P.parent().text(0)
		if not profile:
			return

		for u in _users:
			self.tcd.setUserProfile(u, profile)

		self.profilesRefresh()

	def delUser2Profile(self, *users):
		""" Get the user in the self.usersList and add it to self.profilesTree

		@param self a Main() instance
		@param _users A list of strings usernames to remove from profiles
		"""
		if len(users) == 0:
			users = []
		elif len(users) == 1:
			users = users[0]
		if not users:
			for U in self.Users.profilesTree.selectedItems():
				if U.parent():
					users.append(U.text(0))

		for u in users:
			self.tcd.setUserProfile(u)

		self.profilesRefresh()

	def makeTabItem(self, parentList, text, icon):
		""" Create a Widget to put as item in leftList

		@param	self		A Main() instance
		@param	parentList	QtGui.QListWidget object
		@param	text		String to use as title of tab
		@param	icon		QtGui.QIcon object, to use as icon of tab
		@return			a QtGui.QListWidgetItem object
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
		""" Show the widget of selected Tab

		@param	self		A Main() instance
		@param	listItem	A QtGui.QListWidgetItem object
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

		@param	self		a Main() instance
		"""
		self.new_profiles_count += 1
		n = 'New Profile {0}'.format(self.new_profiles_count)
		title = QtGui.QInputDialog.getText(self.Edit.widget, "Profile Name",
			"Enter the new profile name:", text = n)[0]
		if not title:
			return
		self.tcd.newProfile(title)
		self.profilesRefresh()
		self.activateEditProfileSummary(title)

	def delProfile(self):
		""" Delete a profile

		@param	self		a Main() instance
		"""
		profile = self.Edit.profilesList.selectedItems()
		if not profile:
			return
		_p = self.tcd.getProfilesList()
		for p in profile:
			p = p.text()
			self.tcd.moveProfile(p)
			k = _p.index(p)-1
		self.profilesRefresh()
		_p = self.tcd.getProfilesList()
		self.activateEditProfileSummary(_p[k])

	def editProfile(self):
		""" Edit a profile

		@param	self		A Main() instance
		"""
		profile = self.Edit.profilesList.selectedItems()
		if profile:
			profile = profile[0].text()
		else:
			return
		self.profileEdit(profile)

	def duplicateProfile(self):
		""" Creates a new profile from a existing one

		@param	self		A Main() instance
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

		self.tcd.moveProfile(p, title, copy=True)
		self.profilesRefresh()
		self.activateEditProfileSummary(title)

	def _dragEnterEvent(self, event):
		""" Qt Event of Drag actions

		@param self a Main() instance
		@param event a QtGui.QDragEnterEvent object
		"""
		if event.mimeData().hasFormat(
			'application/x-qabstractitemmodeldatalist'):
			event.accept()
		else:
			event.ignore()

	def _profilesDropEvent(self, event):
		""" Qt Event of Drop actions on profiles tree of Users tab

		@param	self		A Main() instance
		@param	event	A QtGui.QDropEvent object
		"""
		users = []
		if event.source() == self.Users.usersList:
			for U in self.Users.usersList.selectedItems():
				users.append(U.text())
		elif event.source() == self.Users.profilesTree:
			[users.append(U.text(0)) for U in self.Users.profilesTree.\
			selectedItems() if U.parent()]

		else:
			return
		profile = self.Users.profilesTree.itemAt(event.pos())
		if profile.parent():
			profile = profile.parent()
		self.addUser2Profile(users, profile.text(0))

	def _userDropEvent(self, event):
		""" Qt Event of Drop actions on users list of Users tab
		@param self a Main() instance
		@param event a QtGui.QDropEvent object
		"""
		if event.source() != self.Users.profilesTree:
			return
		users = []
		[users.append(U.text(0)) for U in event.source().selectedItems() \
			if U.parent()]

		self.delUser2Profile(users)


def main():
	""" The program main loop """
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
