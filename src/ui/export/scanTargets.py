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
from ui.export.Ui_scanTargetsDialog import Ui_ScanTargetsDialog

#from lib.ping import ping
import subprocess
from random import random

class ScanTargets(QtGui.QDialog):
	"""Creates scan targets dialog"""
	def __init__(self, targets, parent=None):
		"""Instantiate a ScanTargets object

		@param	self		A ScanTargets instance
		@param	parent		A QtGui.QWidget parent object
		"""
		QtGui.QDialog.__init__(self, parent)

		self.scanUi = Ui_ScanTargetsDialog()
		self.scanUi.setupUi(self)

		self.targets = []
		self.parentTargets = targets

	def scan(self):
		#for i in self.targets:
		#	self.targets.remove(i)
		#self.targets = []
		for i in self.back.targets:
			self.targets.append(TreeElement(i,
				len(self.back.targets), self.scanUi.targetsTree))

	def setupBack(self, back):
		"""Setup previous dialog

		@param	self		A ScanTargets instance
		@param	back		A QtGui.QDialog instance
		"""
		self.back = back

	def backClicked(self):
		"""Execute add dialog when back was clicked on scanTargets dialog

		@param	self		A ScanTargets instance
		"""
		self.hide()
		self.back.show()

	def accept(self):
		for i in self.targets:
			if i.isSelected():
				self.parentTargets.append(i.text(0))
				#self.parent.refreshTargets()
		#self.close()
		QtGui.QDialog.accept(self)

	def exec_(self):
		self.scan()
		QtGui.QDialog.exec_(self)

class TreeElement(QtGui.QTreeWidgetItem):
	def __init__(self, address, total, parent=None):
		self.parent = parent
		self.address = address
		self.total = total

		QtGui.QTreeWidgetItem.__init__(self, parent)

		self.setText(0, address)

		self.thread = QtCore.QThread()
		self.thread.element = self
		self.thread.run = self.run

		self.setText(1, "Scanning")
		self.thread.start()

	def run(self):
		self.thread.msleep(int(2000*random()))
		self.on = subprocess.Popen("ping -c 4 {0}".format(self.address).split(),
			stdout=subprocess.PIPE)
		if not self.on.wait():
			self.setSelected(True)
			self.setText(1, "Online")
		else:
			self.setSelected(False)
			self.setText(1, "Seens Offline")
		#self.progressBar.setValue(self.progressBar.value()+
		#	int(100.0/self.total))
