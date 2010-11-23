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

from PyQt4 import QtGui,QtCore
from ui.Ui_editWidget import Ui_EditWidget
from ui.Ui_profileEdit import Ui_EditProfile
from ui.Ui_configProfileEdit import Ui_configsWidget
from ui.commonPage import *

#class ButtonConfigProfileEdit(QtGui.QPushButton):
#	def __init__(self, text, parent=None):
#
#		QtGui.QPushButton.__init__(self, text, parent)
#		self.setCheckable(True)

class ConfigProfileEdit(QtGui.QWidget):
	""" Creates the config page of a category in profile """
	def __init__(self, tcd, category, parent=None):
		""" Instantiate a ConfigProfileEdit widget

		containing category options
		@param	self		A ConfigProfileEdit instance
		@param	tcd			A librix_tcd instance
		@param	category	A string containing the category name
		@param	parent		Parent QtGui.QWidget
		"""
		self.tcd = tcd
		self.category = category
		self.parent = parent

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_configsWidget()
		self.ui.setupUi(self)

		self.buttons = {}

		for o in tcd.getOptionsList(category):
			self.buttons[o] = QtGui.QPushButton(o, self)
			self.buttons[o].setCheckable(True)
			self.ui.ConfigVerticalLayout.addWidget(self.buttons[o])

class ProfileEdit(QtGui.QWidget):
	""" Creates the page to edit profile, into EditPage """
	def __init__(self, tcd, parent=None):
		""" Instantiate ProfileEdit widget

		@param	self	A ProfileEdit instance
		@param	tcd		A librix_tcd instance
		@param	parent	Parent QtGui.QWidget
		"""
		self.parent = parent
		self.tcd = tcd

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_EditProfile()
		self.ui.setupUi(self)

		self.ui.page.close()
		self.ui.configToolBox.removeItem(0)

		self.pages = {}
		self.profile = ''

		for c in tcd.getCategoriesList():
			self.pages[c] = ConfigProfileEdit(tcd, c, None)
			self.ui.configToolBox.addItem(self.pages[c], c)

	def setProfile(self, profile):
		""" Populates ProfileEdit widget with 'profile' informations

		@param	self		A ProfileEdit instance
		@param	profile		A string containing the profile name
		"""

		self.profile = profile
		if not profile:
			print("12345", profile)
			return
		self.ui.profileName.setText(profile)

		for c in self.tcd.getCategoriesList():
			for o in self.tcd.getOptionsList(c):
				if self.tcd.getOption(profile, c, o):
					self.pages[c].buttons[o].setChecked(True)
				else:
					self.pages[c].buttons[o].setChecked(False)

	def readProfileConfig(self):
		""" Read and write configurations on EditProfile

		Called by QButtonBox in EditProfile box
		@param	self		A EditProfile instance
		"""
		name = self.profile	# Original name
		if not name in self.tcd.getProfilesList():
			return

		if self.ui.profileName.text() != name:	# if name has changed
			newname = self.ui.profileName.text()
			self.tcd.moveProfile(name, newname)
			name = newname

		for c in self.tcd.getCategoriesList():
			for o in self.tcd.getOptionsList(c):
				self.tcd.setOption(name, c, o,
					self.pages[c].buttons[o].isChecked())

		self.parent.updateLists()
		self.parent.activateProfileSummary(name)

	def show(self):
		""" Reimplementation of QtGui.QWidget.show method """

		self.parent.summary.hide()
		QtGui.QWidget.show(self)

	def hide(self):
		""" Reimplementation of QtGui.QWidget.hide method """
		self.parent.summary.show()
		QtGui.QWidget.hide(self)


class EditPage(QtGui.QWidget):
	""" Creates the main Edit page """
	def __init__(self, tcd, leftList, parent=None):
		""" Instantiate a EditPage object

		@param	self		A EditPage instance
		@param	tcd			A librix_tcd instance
		@param	leftList	The leftMenu QListWidget, to create the tab
		@param	parent		A QtGui.QWidget parent object
		"""
		self.tcd = tcd
		self.leftList = leftList
		self.parent = parent

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_EditWidget()
		self.ui.setupUi(self)

		self.tab = LeftMenuItem(leftList, 'Edit Profiles',
			QtGui.QIcon(":/edit_icon/document-edit.png"))

		self.summary = ProfilesSummary(tcd, self)
		self.ui.verticalLayout_4.addWidget(self.summary)
		self.current = self.summary

		self.profileEdit = ProfileEdit(tcd, self)
		self.ui.verticalLayout_4.addWidget(self.profileEdit)
		self.profileEdit.hide()


	def updateLists(self):
		""" Update profiles list

		@param	self		A EditPage instance
		"""
		self.ui.profilesList.clear()

		for p in self.tcd.getProfilesList():
			QtGui.QListWidgetItem(QtGui.QIcon(":/edit_icon/profiles.png"),
				p, self.ui.profilesList)

		self.current = None
		self.summary.hide()

	def show(self):
		""" Show self widget

		@param	self		A EditPage instance
		"""
		self.updateLists()
		if self.tcd.getProfilesList():
			self.activateProfileSummary(self.tcd.getProfilesList()[0])
		QtGui.QWidget.show(self)

	def activateProfileSummary(self, profile=''):
		""" Show summary of a profile

		@param	self		A EditPage instance
		@param	profile		A profile name string to show
							or a QtGui.QListWidgetItem
		"""
		if not profile:
			_profile = self.ui.profilesList.selectedItems()
			if _profile:
				_profile = _profile[0]
			else:
				return
		else:
			_profile = profile

		if type(_profile) == QtGui.QListWidgetItem:
			_profile = _profile.text()

		self.summary.setSummary(_profile)

		self.profileEdit.hide()

		self.ui.profilesList.findItems(_profile,
			QtCore.Qt.MatchExactly)[0].setSelected(True)


	def addProfile(self):
		""" Creates a new profile

		Called by editProfile toolbar buttons
		@param	self		a EditPage instance
		"""
		n = 'New Profile +{0}'.format(passwdGen(4))
		title = QtGui.QInputDialog.getText(self, "Profile Name",
			"Enter the new profile name:", text = n)[0]
		if not title:
			return
		self.tcd.newProfile(title)
		self.updateLists()
		self.activateProfileSummary(title)

	def delProfile(self):
		""" Delete a profile

		Called by editProfile toolbar buttons
		@param	self		a Main() instance
		"""
		profile = self.ui.profilesList.selectedItems()

		if not profile:
			return
		_p = self.tcd.getProfilesList()

		for p in profile:
			p = p.text()
			self.tcd.moveProfile(p)
			k = _p.index(p)-1

		self.updateLists()
		_p = self.tcd.getProfilesList()
		self.activateProfileSummary(_p[k] if k>0 else _p[0])

	def editProfile(self):
		""" Edit a profile.

		Called by editProfile toolbar buttons
		@param	self		A Main() instance
		"""
		profile = self.ui.profilesList.selectedItems()
		if profile:
			profile = profile[0].text()
		else:
			return
		self.profileEdit.setProfile(profile)
		#self.summary.hide()
		self.profileEdit.show()

	def duplicateProfile(self):
		""" Creates a new profile from a existing one.

		Called by editProfile toolbar buttons
		@param	self		A Main() instance
		"""
		self.new_profiles_count += 1
		p = self.ui.profilesList.selectedItems()

		if p:
			p = p[0].text()
		else:
			return

		n = '{0} +{1}'.format(p, passwdGen(2))
		title = QtGui.QInputDialog.getText(self, "Profile Name",
			"Enter the destination profile name:", text = n)[0]
		if not title:
			return

		self.tcd.moveProfile(p, title, copy=True)
		self.updateLists()
		self.activateProfileSummary(title)
