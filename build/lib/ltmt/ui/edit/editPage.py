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

from PyQt4 import QtGui,QtCore

from ltmt.ui.edit.Ui_editWidget import Ui_EditWidget
from ltmt.ui.edit.ProfileEdit import ProfileEdit

from ltmt.ui.common.LeftMenuItem import LeftMenuItem
from ltmt.ui.common.ProfileSummary import ProfileSummary

class EditPage(QtGui.QWidget):
	"""Creates the main Edit page"""
	def __init__(self, configparser, moduleparser, leftList, parent=None):
		"""Instantiate a EditPage object

		@param	self		A EditPage instance
		@param	configparser			A LTCConfigParser instance
		@param	leftList	The leftMenu QListWidget, to create the tab
		@param	parent		A QtGui.QWidget parent object
		"""
		self.moduleparser = moduleparser
		self.configparser = configparser
		self.leftList = leftList
		self.parent = parent

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_EditWidget()
		self.ui.setupUi(self)

		self.tab = LeftMenuItem(leftList, self.tr("Profiles"),
			QtGui.QIcon(":/edit_icon/document-edit.png"))

		self.summary = ProfileSummary(configparser, moduleparser, True, self)
		self.ui.verticalLayout_4.addWidget(self.summary)
		self.current = self.summary

		self.profileEdit = ProfileEdit(configparser, moduleparser, self)
		self.ui.verticalLayout_4.addWidget(self.profileEdit)
		self.profileEdit.hide()


	def updateLists(self):
		"""Update profiles list

		@param	self		A EditPage instance
		"""
		self.ui.profilesList.clear()

		for p in self.configparser.getProfilesList():
			QtGui.QListWidgetItem(QtGui.QIcon(":/edit_icon/profiles.png"),
				p, self.ui.profilesList)

		self.current = None
		self.summary.hide()

	def show(self):
		"""Show self widget

		@param	self		A EditPage instance
		"""
		self.updateLists()
		if self.configparser.getProfilesList():
			self.activateProfileSummary(self.configparser.getProfilesList()[0])
		QtGui.QWidget.show(self)

	def activateProfileSummary(self, profile=''):
		"""Show summary of a profile

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
		"""Creates a new profile

		Called by editProfile toolbar buttons
		@param	self		a EditPage instance
		"""
		title = QtGui.QInputDialog.getText(self, self.tr("Profile Name"),
			self.tr("Enter the new profile name:"))[0]

		# Confirm overwriting if title already in profiles list
		if title and (title not in self.configparser.getProfilesList() or \
			QtGui.QMessageBox.warning(self, self.tr("Replace profile"),
			self.tr("Are you sure you want to overwrite \"{0}\" profile?\n")\
			.format(title), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
			QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes):
				self.configparser.newProfile(title)
				self.updateLists()
				self.activateProfileSummary(title)

	def delProfile(self):
		"""Delete a profile

		Called by editProfile toolbar buttons
		@param	self		a Main() instance
		"""
		profile = self.ui.profilesList.selectedItems()

		if not profile:
			return
		_p = self.configparser.getProfilesList()

		for p in profile:
			p = p.text()
			# Confirm profile deletion
			if QtGui.QMessageBox.warning(self, self.tr("Remove profile"),
				self.tr("Are you sure you want to delete \"{0}\" profile?\n")\
				.format(p), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
				QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
				self.configparser.moveProfile(p)
			k = _p.index(p)-1

		self.updateLists()
		_p = self.configparser.getProfilesList()
		self.activateProfileSummary(_p[k] if k>0 else _p[0])

	def editProfile(self):
		"""Edit a profile.

		Called by editProfile toolbar buttons
		@param	self		A Main() instance
		"""
		profile = self.ui.profilesList.selectedItems()
		if profile:
			profile = profile[0].text()
		else:
			return
		self.profileEdit.setProfile(profile)
		self.profileEdit.show()

	def duplicateProfile(self):
		"""Creates a new profile from a existing one.

		Called by editProfile toolbar buttons
		@param	self		A Main() instance
		"""
		p = self.ui.profilesList.selectedItems()

		if p:
			p = p[0].text()
		else:
			return

		# Get target profile name
		title = QtGui.QInputDialog.getText(self, self.tr("Profile Name"),
			self.tr("Enter the destination profile name:"))[0]

		# Confirm profile overwriting
		if title in self.configparser.getProfilesList() and not \
			QtGui.QMessageBox.warning(self, self.tr("Replace profile"),
			self.tr("Are you sure you want to overwrite \"{0}\" profile?\n")\
			.format(title), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
			QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
				return

		if title:
			self.configparser.moveProfile(p, title, copy=True)
			self.updateLists()
			self.activateProfileSummary(title)
