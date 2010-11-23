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

from copy import deepcopy
from PyQt4 import QtGui
from ui.Ui_usersWidget import Ui_UsersWidget
from ui.commonPage import *

class UsersPage(QtGui.QWidget):
	""" Creates the main users page """
	def __init__(self, tcd, leftList, parent=None):
		""" Instantiate a UsersPage object

		@param	self		A UsersPage instance
		@param	tcd			A librix_tcd instance
		@param	leftList	The leftMenu QListWidget, to create the tab
		@param	parent		A QtGui.QWidget parent object
		"""
		self.tcd = tcd
		self.leftList = leftList
		self.parent = parent

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_UsersWidget()
		self.ui.setupUi(self)

		self.tab = LeftMenuItem(leftList, 'Users',
			QtGui.QIcon(":/user_icon/system-users.png"))

		self.summary = ProfilesSummary(tcd, self.ui.dockWidgetContents)
		self.ui.verticalLayout_5.addWidget(self.summary)

		self.ui.usersList.dragEnterEvent = self.dragEnterEvent
		self.ui.usersList.dropEvent = self.usersDropEvent
		self.ui.profilesTree.dragEnterEvent = self.dragEnterEvent
		self.ui.profilesTree.dropEvent = self.profilesDropEvent

	def updateLists(self):
		""" Update users list and profiles tree

		@param	self		A UsersPage instance
		"""
		self.ui.profilesTree.clear()
		self.ui.usersList.clear()

		self.summary.setSummary()

		for p in self.tcd.getProfilesList():
			P = QtGui.QTreeWidgetItem(self.ui.profilesTree,
				[p])
			P.setExpanded(True)
			P.setIcon(0, QtGui.QIcon(":/edit_icon/profiles.png"))
			for u in self.tcd.getProfileUsersList(p):
				QtGui.QTreeWidgetItem(P, [u], 1000).setIcon(0,
					QtGui.QIcon(":/user_icon/user.png"))


		for u in self.tcd.getUsersList():
			U = QtGui.QListWidgetItem(
				QtGui.QIcon(":/user_icon/user.png"),
				u, self.ui.usersList)
			p = self.tcd.getUserProfile(u)
			U.setToolTip("Profile: <b>{0}</b>".format(p if p else "None"))


	def show(self):
		""" Show self widget

		@param	self		A UsersPage instance
		"""
		self.updateLists()
		QtGui.QWidget.show(self)

	def activateProfileSummary(self, treeItem):
		""" Show summary when a Profile was selected on self.profilesTree

		@param	self		A UsersPage instance
		@param	treeItem	A QtGui.QTreeWidgetItem profile object
		"""
		if not treeItem: return
		if treeItem.parent():
			treeItem = treeItem.parent()

		self.summary.setSummary(treeItem.text(0))

	def addUsers(self, users = [], profile = ''):
		""" Get the user in the self.usersList and add it to self.profilesTree

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
				if not P.parent():
					profile = P.text(0)
				else:
					profile = P.parent().text(0)
				break

		if not profile:
			return

		for u in _users:
			self.tcd.setUserProfile(u, profile)

		self.updateLists()

	def delUsers(self, users=[]):
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
			self.tcd.setUserProfile(u)

		self.updateLists()


	def dragEnterEvent(self, event):
		""" Qt Event of Drag actions

		@param	self		A Main() instance
		@param	event	A QtGui.QDragEnterEvent object
		"""
		if event.mimeData().hasFormat(
			'application/x-qabstractitemmodeldatalist'):
			event.accept()
		else:
			event.ignore()

	def profilesDropEvent(self, event):
		""" Qt Event of Drop actions on profiles tree of Users tab

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
		if profile.parent():
			profile = profile.parent()

		self.addUsers(users, profile.text(0))

	def usersDropEvent(self, event):
		""" Qt Event of Drop actions on users list of Users tab

		@param	self		A Main() instance
		@param 	event		A QtGui.QDropEvent object
		"""
		if event.source() != self.ui.profilesTree:
			return

		users = [U.text(0) for U in event.source().selectedItems() \
			if U.parent()]
		self.delUsers(users)
