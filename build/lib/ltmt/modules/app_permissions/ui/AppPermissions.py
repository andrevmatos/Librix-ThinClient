#!/usr/bin/env python3
#
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


if __name__ == '__main__':
	import sys
	sys.path.append("../../")

from PyQt4 import QtGui,QtCore
from .Ui_appPermissions import Ui_AppPermissions
#from lxml import etree as ET
from ltmt.lib.utils import DesktopParser

import re
import os
import lxml.etree as ET
from copy import deepcopy

app_dir = '/usr/share/applications'

class AppPermissions(QtGui.QDialog):
	"""Applications Permissions module Configuration Dialog"""

	def __init__(self, config, parent=None):
		"""Init method

		@param	self		A AppPermissions instance
		@param	config		A lxml.etree.Element object
		@param	parent		A QtGui.QWidget parent instance
		"""

		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_AppPermissions()
		self.ui.setupUi(self)

		self.ui.allAppsList.dragEnterEvent = self.dragEnterEvent
		self.ui.selectedAppsList.dragEnterEvent = self.dragEnterEvent
		self.ui.allAppsList.dropEvent = self.allAppsDropEvent
		self.ui.selectedAppsList.dropEvent = self.selectedAppsDropEvent

		self.allApps = {}
		self.config = config

		self.parseDialog = ParseDialog(self.allApps, self.ui.allAppsList, self)
		self.parseDialog.accepted.connect(self.readConfig)

		self.parseDialog.parse()

	def readConfig(self):
		"""Read current config and set interface

		setting policy and adding corresponding items to selected apps list
		@param	self		A AppPermissions instance
		"""
		# Policy
		if self.config is None:
			return
		if self.config.find("policy") is not None:
			if 'allow' in self.config.find("policy").text:
				self.ui.allowRadio.setChecked(True)
			elif 'deny' in self.config.find("policy").text:
				self.ui.denyRadio.setChecked(True)
		# Entries
		for i in self.allApps:
			# if filename is 'entry'.text (e.g. firefox.desktop)
			if os.path.basename(i) in [e.text for e in
				self.config.findall("entry")]:
				T = self.allApps[i]['all'].clone()
				self.allApps[i]['selected'] = T
				self.ui.selectedAppsList.addItem(T)
				self.allApps[i]['element'] = [e for e in self.config.\
					findall("entry") if e.text == os.path.basename(i)][0]

	def setPolicy(self):
		if self.config is None:
			return

		if self.ui.allowRadio.isChecked():
			self.config.find("policy").text = "allow"
		elif self.ui.denyRadio.isChecked():
			self.config.find("policy").text = "deny"

	def accept(self):
		print("_accepted Main")
		self.setPolicy()
		QtGui.QDialog.accept(self)

	def reject(self):
		print("_rejected Main")
		QtGui.QDialog.reject(self)

	def exec_(self):
		r = QtGui.QDialog.exec_(self)
		if r:
			return(deepcopy(self.config))
		else:
			return(None)

	def allSearch(self, text=''):
		if not text: text = self.ui.allSearchLine.text()
		for i in self.allApps:
			if not (text.lower() in self.allApps[i]['name'].lower() or \
				text.lower() in self.allApps[i]['exec'].lower()):
				self.allApps[i]['all'].setHidden(True)
			else:
				self.allApps[i]['all'].setHidden(False)

	def selectedSearch(self, text=''):
		if not text: text = self.ui.selectedSearchLine.text()
		for i in self.allApps:
			if 'selected' in self.allApps[i].keys():
				if not (text.lower() in self.allApps[i]['name'].lower() or \
					text.lower() in self.allApps[i]['exec'].lower()):
					self.allApps[i]['selected'].setHidden(True)
				else:
					self.allApps[i]['selected'].setHidden(False)

	def addSelected(self):
		for i in self.allApps:
			if self.allApps[i]['all'].isSelected()\
				and not 'selected' in self.allApps[i]:
				T = self.allApps[i]['all'].clone()
				self.allApps[i]['selected'] = T
				self.ui.selectedAppsList.addItem(T)
				self.allApps[i]['element'] = ET.SubElement(self.config, "entry",
					attrib={"type":"app"}).text = os.path.basename(i)

	def removeSelected(self):
		for i in self.allApps:
			if 'selected' in self.allApps[i] and\
				self.allApps[i]['selected'].isSelected():
				self.ui.selectedAppsList.takeItem(self.ui.selectedAppsList.row(
					self.allApps[i]['selected']))
				del self.allApps[i]['selected']
				self.config.remove(self.allApps[i]['element'])

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

	def allAppsDropEvent(self, event):
		"""Qt Event of Drop actions on profiles tree of Users tab

		@param	self		A Main() instance
		@param	event	A QtGui.QDropEvent object
		"""
		if event.source() == self.ui.selectedAppsList:
			self.removeSelected()
			event.accept()
		else:
			event.ignore()

	def selectedAppsDropEvent(self, event):
		"""Qt Event of Drop actions on users list of Users tab

		@param	self		A Main() instance
		@param 	event		A QtGui.QDropEvent object
		"""
		if event.source() == self.ui.allAppsList:
			self.addSelected()
			event.accept()
		else:
			event.ignore()

class ParseDialog(QtGui.QProgressDialog):
	def __init__(self, allApps, listWid, parent=None):

		self.allApps = allApps
		self.listWid = listWid

		QtGui.QProgressDialog.__init__(self, parent)

		self.setLabelText("Parsing application files")

		self.threadedParse = ThreadedParse(allApps, listWid)
		self.threadedParse.parsed.connect(self.setValue)

		self.threadedParse.finished.connect(self.accept)

	def parse(self):
		self.show()
		self.threadedParse.start()

	def accept(self):
		print("_accepted Progress")
		QtGui.QDialog.accept(self)

	def reject(self):
		print("_rejected Progress")
		self.threadedParse.stop()
		QtGui.QDialog.reject(self)

class ThreadedParse(QtCore.QThread):
	parsed = QtCore.pyqtSignal(int)
	def __init__(self, allApps, listWid):

		QtCore.QThread.__init__(self)

		self.allApps = allApps
		self.listWid = listWid

		# If cancel, stop iteration
		self.cancel = False

	def stop(self):
		self.cancel = True
		QtCore.QThread.stop(self)

	def run(self):
		"""Parse app_dir directory, looking for .desktop files

		And parse this desktop files, creating entries on self.allApps dict
		@param	self		A AppPermissions instance
		"""
		self.cancel = False
		all = []
		for D, d, F in os.walk(app_dir):
			for f in F:
				if f.endswith('.desktop'):
					all.append(os.path.join(D, f))
		self.total = len(all)
		self.concluded = 0.0
		for f in all:
			if self.cancel:
				break
			try:
				d = DesktopParser(f)
				Name = d.get('Name')
				Exec = d.get('Exec')
			except:
				continue

			T = QtGui.QListWidgetItem("{0}".format(Name), self.listWid)
			T.setToolTip(Exec)
			self.allApps[f] = {'name': Name, 'exec': Exec, 'all': T}
			self.concluded += 1
			self.parsed.emit(int(round(100.0*self.concluded/self.total)))

