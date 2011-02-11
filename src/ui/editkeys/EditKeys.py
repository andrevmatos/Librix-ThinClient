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

from PyQt4 import QtGui
from ui.editkeys.Ui_editKeys import Ui_EditKeys

class EditKeys(QtGui.QDialog):
	"""Show a dialog to edit pubkeys in configfile"""
	def __init__(self, configparser, parent=None):
		"""Init method

		@param	self		A EditKeys instance
		@param	configparser	A LTCConfigParser instance
		@param	parent		Parent QtGui.QWidget object
		"""
		self.parent = parent
		self.configparser = configparser

		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_EditKeys()
		self.ui.setupUi(self)

		for k in configparser.getKeys():
			QtGui.QListWidgetItem(k, self.ui.keysList).setToolTip(k)

	def openKey(self):
		"""Method called when self.ui.openButton is clicked

		Open a pubkey file
		@param	self		A EditKeys instance
		"""
		fn = QtGui.QFileDialog.getOpenFileName(self, self.tr("Open PubKey"),
			"~/.ssh/id_rsa.pub")
		if not fn: return
		with open(fn, 'r') as F:
			k = F.read().strip()
		if len(k.split()) != 3 or k.split()[0] not in ['ssh-dss', 'ssh-rsa']:
			return
		else:
			QtGui.QListWidgetItem(k, self.ui.keysList).setToolTip(k)

	def addKey(self):
		"""Method called when self.ui.addButton is clicked

		Add a entry to list
		@param	self		A EditKeys instance
		"""
		k = QtGui.QInputDialog.getText(self, self.tr("New PubKey"),
			self.tr("Enter below a valid SSH public key"))[0]
		if len(k.split()) != 3 or k.split()[0] not in ['ssh-dss', 'ssh-rsa']:
			return
		else:
			QtGui.QListWidgetItem(k, self.ui.keysList).setToolTip(k)

	def delKey(self):
		"""Method called when self.ui.delButton is clicked

		Remove selected entry from list
		@param	self		A EditKeys instance
		"""
		for i in self.ui.keysList.selectedItems():
			self.ui.keysList.takeItem(self.ui.keysList.row(i))

	def accept(self):
		"""Method called when dialog is accepted (e.g. Ok button is clicked)

		Remove all key entries from config and add current
		@param	self		A EditKeys instance
		"""
		for k in self.configparser.getKeys():
			self.configparser.delKey(k)

		for i in range(self.ui.keysList.count()):
			k = self.ui.keysList.item(i).text()
			self.configparser.addKey(k)

		QtGui.QDialog.accept(self)

