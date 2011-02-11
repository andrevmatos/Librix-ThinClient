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
import os
from PyQt4 import QtGui,QtCore

from ui.Ui_mainWindow import Ui_ThinClient
from ui.editkeys.EditKeys import EditKeys

from ui.users.usersPage import UsersPage
from ui.edit.editPage import EditPage
from ui.export.exportPage import ExportPage

from lib.config import LTCConfigParser
from lib.modules import LTCModuleParser

configfile = 'thinclient.conf'

# Create a class for our main window
class Main(QtGui.QMainWindow):
	def __init__(self):
		"""Creates a Main() instance, and setup the mainWindow options

		@param	self		A Main() instance
		"""
		QtGui.QMainWindow.__init__(self)

		# Setup main UI
		self.ui = Ui_ThinClient()
		self.ui.setupUi(self)
		self.hide()

#		self.ui.toolBar.addWidget(QtGui.QSpacerItem(40, 20,
#			QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
		self.ui.toolBar.addWidget(self.ui.nameEdit)

		self.ui.topBar.close()

		# Init users and profiles package
		self.moduleparser = LTCModuleParser()
		self.configparser = LTCConfigParser(self.moduleparser)

		#self.openConfigFile()
		self.newConfigFile(first=True)

		# Set config file name
		self.ui.nameEdit.setText(self.configparser.getName())

		# Users widget configuration routines
		self.Users = UsersPage(self.configparser, self.moduleparser,
			self.ui.listWidget, self)
		self.ui.horizontalLayout.addWidget(self.Users)
		#self.Users.hide()

		# Edit widget configuration routines
		self.Edit = EditPage(self.configparser, self.moduleparser,
			self.ui.listWidget, self)
		self.ui.horizontalLayout.addWidget(self.Edit)
		self.Edit.hide()

		# Export widget configuration routines
		self.Export = ExportPage(self.configparser, self.moduleparser,
			self.ui.listWidget, self)
		self.ui.horizontalLayout.addWidget(self.Export)
		self.Export.hide()

		summaryAction = self.Users.ui.summaryDock.toggleViewAction()
		summaryAction.setText(self.tr("Show user's profile summary"))
		self.ui.menuView.addAction(summaryAction)

		self.current = self.Users
		self.ui.listWidget.item(0).setSelected(True)
		self.show()

	def activateTab(self, listItem):
		"""Show the widget of selected Tab

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

	def configNameChanged(self):
		"""When config file name was changed, set it to configfile

		Qt Slot, called by UI
		@param	self		A Main window instance
		"""
		text = self.ui.nameEdit.text()
		if text:
			self.configparser.setName(text)

	def closeEvent(self, event):
		"""Reimplementation of closeEvent Qt event

		Exec writeConfigFile in self.configparser before close main window
		"""
		if not self.configparser.modified():
			event.accept()
		else:
			ret = QtGui.QMessageBox.question(self, self.tr("LTMT"),
				self.tr("The configuration file has been modified.")+
				"\n"+self.tr("Do you want to save your changes?"),
				QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |\
				QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Save)
			if ret == QtGui.QMessageBox.Save:
				self.saveConfigFile()
				event.accept()
			elif ret == QtGui.QMessageBox.Discard:
				os.remove(self.configparser.backupfile)
				self.newConfigFile()
				event.accept()
			else:
				event.ignore()

	def newConfigFile(self, first=False):
		"""Creates a new config file

		@param	self		A Main window instance
		@param	first		Bool. True if the first operation in
							configparser, when there is no configfile set on it
		"""
		if not first:
			event = QtCore.QEvent(QtCore.QEvent.User)
			self.closeEvent(event)
			if not event.isAccepted(): return

		self.configparser.newConfigFile()
		if not first:
			self.Users.updateLists()
			self.Edit.updateLists()

	def openConfigFile(self):
		"""Open file dialog to select and open a configuration

		If there is a backup file, ask if admin want to recover it
		@param	self		A Main window instance
		"""
		event = QtCore.QEvent(QtCore.QEvent.User)
		self.closeEvent(event)
		if not event.isAccepted(): return

		file = QtGui.QFileDialog.getOpenFileName(self,
			self.tr("Open Config File"), os.path.abspath("thinclient.conf"))
		if file and self.configparser.modified(file)==1:
			reply = QtGui.QMessageBox.question(self, self.tr("Backup found"),
            self.tr("A backup file of <b>{0}</b> was found.\n"+
				"Do you want to restore it?")\
			.format(file), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
			QtGui.QMessageBox.No)
			# If yes, write backup to file
			if reply == QtGui.QMessageBox.Yes:
				with open(file, 'w') as orig, open(file + '~', 'r') as bkp:
					orig.write(bkp.read())
			# finally, remove bkp
			try: os.remove(file + '~')
			except: pass

		if file:
			self.configparser.readConfigFile(file)
			# If file outdated, ask for update
			if self.configparser.getOptionsList() != self.moduleparser.getModulesList():
				if QtGui.QMessageBox.question(self,
				self.tr("Outdated Config File"), self.tr("This config file "+
				"has absent and/or hasn't present modules.\n"+
				"You want to update it (required to proceed)?\n"+
				"P.S.: New modules will be added to configurations "+
				"but absent, present in configuration, won't be touched "+
				"or shown."), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
				QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
					self.configparser.updateConfigFile()
				else:
					self.newConfigFile()
			self.ui.nameEdit.setText(self.configparser.getName())
			self.ui.statusbar.showMessage(self.tr("Editing file: {0}")\
				.format(file), 0)
			self.Users.updateLists()
			self.Edit.updateLists()

	def saveConfigFile(self):
		"""Save current opened config file

		@param	self		 A Main window instance
		"""
		if self.configparser.modified()==1:
			self.configparser.writeConfigFile()
			self.ui.statusbar.showMessage(self.tr("File \"{0}\" saved!").format(
				self.configparser.configfile), 5000)
		elif self.configparser.modified()==2:
			self.saveAsConfigFile()

	def saveAsConfigFile(self):
		"""Open Save as dialog to choose where to save current config file

		@param	self		 A Main window instance
		"""
		# TODO: change work dir of save dialog to /etc
		file = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save Config File as"),
			"thinclient.conf", self.tr("Conf files (*.conf) (*.conf);; "+
			"XML files (*.xml) (*.xml);; All files (*) (*)"))
		if file:
			self.configparser.writeConfigFile(file)
			self.ui.statusbar.showMessage(self.tr("File \"{0}\" saved!").format(
				self.configparser.configfile), 5000)

	def editKeys(self):
		"""Open EditKeys dialog

		@param	self		A Main window instance
		"""
		dialog = EditKeys(self.configparser, self)
		dialog.exec_()

def main():
	"""The program main loop"""
	app = QtGui.QApplication(sys.argv)

	# Install translations
	locale = QtCore.QLocale.system().name()
	qtTranslator = QtCore.QTranslator()
	if qtTranslator.load("qt_"+locale, "ui/i18n"):
		app.installTranslator(qtTranslator)
	appTranslator = QtCore.QTranslator()
	if appTranslator.load("app_"+locale, "ui/i18n"):
		app.installTranslator(appTranslator)

	window=Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
