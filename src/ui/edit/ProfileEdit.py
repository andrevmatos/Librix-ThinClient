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

from ui.edit.Ui_profileEdit import Ui_EditProfile
from ui.edit.ConfigProfileEdit import ConfigProfileEdit

class ProfileEdit(QtGui.QWidget):
	"""Creates the page to edit profile, into EditPage"""
	def __init__(self, tcd, parent=None):
		"""Instantiate ProfileEdit widget

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
		"""Populates ProfileEdit widget with 'profile' informations

		@param	self		A ProfileEdit instance
		@param	profile		A string containing the profile name
		"""

		self.profile = profile
		if not profile:
			return
		self.ui.profileName.setText(profile)

		for c in self.tcd.getCategoriesList():
			for o in self.tcd.getOptionsList(c):
				if self.tcd.getOption(profile, c, o):
					self.pages[c].buttons[o].setChecked(True)
				else:
					self.pages[c].buttons[o].setChecked(False)

	def readProfileConfig(self):
		"""Read and write configurations on EditProfile

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
		"""Reimplementation of QtGui.QWidget.show method"""

		self.parent.summary.hide()
		QtGui.QWidget.show(self)

	def hide(self):
		"""Reimplementation of QtGui.QWidget.hide method"""
		self.parent.summary.show()
		QtGui.QWidget.hide(self)
