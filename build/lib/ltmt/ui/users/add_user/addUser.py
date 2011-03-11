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

import os

from PyQt4 import QtGui

from ltmt.ui.users.add_user.Ui_addUser import Ui_AddUser

class AddUser(QtGui.QDialog):
	"""This class provides a add user dialog feature to users page of LTMT"""
	def __init__(self, configparser, parent=None):
		"""Init method

		@param	self		A AddUser instance
		@param	parent	Parent QtGui.QWidget object
		"""
		self.configparser = configparser
		self.parent = parent

		QtGui.QDialog.__init__(self)

		self.ui = Ui_AddUser()
		self.ui.setupUi(self)

		self.parseDefaults()

		self.ui.detailsWid.hide()

	def parseDefaults(self):
		"""Parse some default values for new user accounts

		@param	self		A AddUser instance
		"""
		with open("/etc/default/useradd", 'r') as ua:
			for l in ua:
				L = l.strip().split('=')
				if len(L) >= 2:
					if L[0] == "GROUP":
						self.group = L[1]
					elif L[0] == "HOME":
						self.home = L[1]
					elif L[0] == "SHELL":
						self.shell = L[1]

	def userChanged(self, username):
		"""Slot called when user name was changed, updating entries

		@param	self		A AddUser instance
		@param	username	String username
		"""
		self.ui.initGLine.setText(self.group)
		self.ui.homeLine.setText(os.path.join(self.home, username))
		self.ui.shellLine.setText(self.shell)

	def accept(self):
		"""Reimplemented method QtGui.QDialog.accept

		Add user to configparser before accept dialog
		@param	self		A AddUser instance
		"""
		user = self.ui.nameLine.text()
		print("__accepted__", user)
		if user in self.configparser.getUsersList():
			if QtGui.QMessageBox.warning(self, self.tr("Replace User"),
				self.tr("Are you sure you want to overwrite \"{0}\" user?")\
				.format(user), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
				QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
				self.configparser.delUser(user)
			else:
				return
		self.configparser.addUser(user)
		if self.ui.syncCheck.isChecked():
			self.configparser.setUserSync(user, passwd=self.ui.pwLine.text(),
				uid=self.ui.uidSpin.text(), init_group=self.ui.initGLine.text(),
				groups=[g.strip() for g in self.ui.groupsLine.text().split(',')],
				home=self.ui.homeLine.text(), shell=self.ui.shellLine.text())

		QtGui.QDialog.accept(self)
