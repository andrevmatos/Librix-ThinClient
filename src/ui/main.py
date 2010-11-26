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
from PyQt4 import QtGui

from ui.Ui_mainWindow import Ui_ThinClient

from ui.users.usersPage import UsersPage
from ui.edit.editPage import EditPage
from ui.export.exportPage import ExportPage

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

		# TODO: implement qt translate, instead of pure strings
		self.Users = UsersPage(self.tcd, self.ui.listWidget, self)
		self.ui.horizontalLayout.addWidget(self.Users)
		#self.Users.hide()

		# Edit widget configuration routines
		self.Edit = EditPage(self.tcd, self.ui.listWidget, self)
		self.ui.horizontalLayout.addWidget(self.Edit)
		self.Edit.hide()

		# Export widget configuration routines
		self.Export = ExportPage(self.tcd, self.ui.listWidget, self)
		self.ui.horizontalLayout.addWidget(self.Export)
		self.Export.hide()

		self.current = self.Users
		self.ui.listWidget.item(0).setSelected(True)

	def activateTab(self, listItem):
		""" Show the widget of selected Tab

		@param	self		A Main() instance
		@param	listItem	A QtGui.QListWidgetItem object
		"""
		self.current.hide()
		if listItem == self.Users.tab:
			self.Users.show()
			self.current = self.Users
		elif listItem == self.Edit.tab:
			self.Edit.show()
			self.current = self.Edit
		elif listItem == self.Export.tab:
			self.Export.show()
			self.current = self.Export


def main():
	""" The program main loop """
	app = QtGui.QApplication(sys.argv)
	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
