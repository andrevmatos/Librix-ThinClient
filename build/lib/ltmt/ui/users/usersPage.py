#!/usr/bin/env python3
#
#
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

from copy import deepcopy
from PyQt4 import QtGui

from ltmt.ui.users.Ui_usersWidget import Ui_UsersWidget
from ltmt.ui.users.add_user.addUser import AddUser
from ltmt.ui.common.LeftMenuItem import LeftMenuItem
from ltmt.ui.common.ProfileSummary import ProfileSummary
from ltmt.ui.common.UserSummary import UserSummary

class UsersPage(QtGui.QWidget):
	"""Creates the main users page"""
	def __init__(self, configparser, moduleparser, leftList, parent=None):
		"""Instantiate a UsersPage object

		@param	self		A UsersPage instance
		@param	configparser			A LTCConfigParser instance
		@param	leftList	The leftMenu QListWidget, to create the tab
		@param	parent		A QtGui.QWidget parent object
		"""
		self.configparser = configparser
		self.leftList = leftList
		self.parent = parent

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_UsersWidget()
		self.ui.setupUi(self)

		self.tab = LeftMenuItem(leftList, self.tr("Users"),
			QtGui.QIcon(":/user_icon/system-users.png"))

		self.profileSummary = ProfileSummary(configparser, moduleparser, False,
			self.ui.dockWidgetContents)
		self.userSummary = UserSummary(configparser, moduleparser, 
			self.ui.dockWidgetContents)
		self.ui.verticalLayout_5.addWidget(self.profileSummary)
		self.ui.verticalLayout_5.addWidget(self.userSummary)
		self.userSummary.hide()

		self.ui.usersList.dragEnterEvent = self.dragEnterEvent
		self.ui.usersList.dropEvent = self.usersDropEvent
		self.ui.profilesTree.dragEnterEvent = self.dragEnterEvent
		self.ui.profilesTree.dropEvent = self.profilesDropEvent

		self.updateLists()

	def updateLists(self):
		"""Update users list and profiles tree

		@param	self		A UsersPage instance
		"""
		self.ui.profilesTree.clear()
		self.ui.usersList.clear()

		self.profileSummary.setSummary()
		self.userSummary.setSummary()

		for p in self.configparser.getProfilesList():
			P = QtGui.QTreeWidgetItem(self.ui.profilesTree,
				[p])
			P.setExpanded(True)
			P.setIcon(0, QtGui.QIcon(":/edit_icon/profiles.png"))
			for u in self.configparser.getProfileUsersList(p):
				QtGui.QTreeWidgetItem(P, [u], 1000).setIcon(0,
					QtGui.QIcon(":/user_icon/user.png"))


		for u in self.configparser.getUsersList():
			U = QtGui.QListWidgetItem(
				QtGui.QIcon(":/user_icon/user.png"),
				u, self.ui.usersList)
			p = self.configparser.getUserProfile(u)
			U.setToolTip(self.tr("Profile: <b>{0}</b>").format(p if p else "None"))


	def show(self):
		"""Show self widget

		@param	self		A UsersPage instance
		"""
		self.updateLists()
		QtGui.QWidget.show(self)

	def activateProfileSummary(self, treeItem):
		"""Show summary when a Profile was selected on self.profilesTree

		@param	self		A UsersPage instance
		@param	treeItem	A QtGui.QTreeWidgetItem profile object
		"""
		self.userSummary.hide()
		if not treeItem: return
		while treeItem.parent():
			treeItem = treeItem.parent()

		self.profileSummary.setSummary(treeItem.text(0))
		self.ui.summaryDock.setWindowTitle(self.tr("Profile Summary:"))
		self.profileSummary.show()
	
	def activateUserSummary(self, listItem):
		"""Show user summary when a user is selected on self.usersList
		
		@param	self		A UsersPage instance
		@param	listItem	A QtGui.QListWidgetItem user object
		"""
		self.profileSummary.hide()
		if not listItem: return
		
		self.userSummary.setSummary(listItem.text())
		self.ui.summaryDock.setWindowTitle(self.tr("User Summary:"))
		self.userSummary.show()

	def addUsersToProfile(self, users = [], profile = ''):
		"""Get the user in the self.usersList and add it to self.profilesTree

		@param 	self		A UsersPage instance
		@param	users		A list of strings usernames to add to profile
		@param	profile		A string containing the destiny profile name
		"""
		_users = deepcopy(users)
		if not _users:
			for U in self.ui.usersList.selectedItems():
				try:
					_users.append(U.text())
				except:	# If U.text() fail, is a tree item, not list item
					if U.parent():
						_users.append(U.text(0))
		if not profile:
			for P in self.ui.profilesTree.selectedItems():
				while P.parent():
					P = P.parent()
				profile = P.text(0)
				break

		if not profile:
			return

		for u in _users:
			self.configparser.setUserProfile(u, profile)

		self.updateLists()

	def delUsersFromProfile(self, users=[]):
		"""Clean users profile of selected items in self.Users.profilesTree

		@param 	self 		A Main() instance
		@param 	users	A list of strings usernames to remove from profiles
		"""
		_users = deepcopy(users)

		if not _users:
			for U in self.ui.profilesTree.selectedItems():
				if U.parent():
					_users.append(U.text(0))

		for u in _users:
			self.configparser.setUserProfile(u)

		self.updateLists()

	def addUser(self):
		"""Ask for a username and add it to user's list

		@param	self		 A UsersPage instance
		"""
		dialog = AddUser(self.configparser, self)
		dialog.exec_()
		self.updateLists()

	def delUser(self):
		"""Delete selected user from config file

		@param	self		A UsersPage
		"""
		users = [u.text() for u in self.ui.usersList.selectedItems()]
		if users and QtGui.QMessageBox.warning(self, self.tr("Remove users"),
			self.tr("Are you sure you want to delete these users?\n")
			+','.join(users), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
			QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
				[self.configparser.delUser(u) for u in users]
		self.updateLists()

	def dragEnterEvent(self, event):
		"""Qt Event of Drag actions

		@param	self		A Main() instance
		@param	event	A QtGui.QDragEnterEvent object
		"""
		if event.mimeData().hasFormat(
			'application/x-qabstractitemmodeldatalist'):
			event.accept()
		else:
			event.ignore()

	def profilesDropEvent(self, event):
		"""Qt Event of Drop actions on profiles tree of Users tab

		@param	self		A Main() instance
		@param	event	A QtGui.QDropEvent object
		"""
		users = []
		if event.source() == self.ui.usersList:
			for U in self.ui.usersList.selectedItems():
				users.append(U.text())
		elif event.source() == self.ui.profilesTree:
			[users.append(U.text(0)) for U in \
				self.ui.profilesTree.selectedItems() if U.parent()]
		else:
			return

		profile = self.ui.profilesTree.itemAt(event.pos())
		while profile.parent():
			profile = profile.parent()

		self.addUsersToProfile(users, profile.text(0))

	def usersDropEvent(self, event):
		"""Qt Event of Drop actions on users list of Users tab

		@param	self		A Main() instance
		@param 	event		A QtGui.QDropEvent object
		"""
		if event.source() != self.ui.profilesTree:
			return

		users = [U.text(0) for U in event.source().selectedItems() \
			if U.parent()]
		self.delUsersFromProfile(users)
