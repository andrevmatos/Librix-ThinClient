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
	def __init__(self, parent=None):
		"""Instantiate a ScanTargets object

		@param	self		A ScanTargets instance
		@param	parent		A QtGui.QWidget parent object
		"""
		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_ScanTargetsDialog()
		self.ui.setupUi(self)

		self.targets = []
		self.tree = []
		self.total = 0

	def scan(self, targets):
		#for i in self.targets:
		#	self.targets.remove(i)
		#self.targets = []
		self.ui.progressBar.setValue(0)
		self.total = len(targets)
		for i in targets:
			T = TreeElement(i, len(targets), self.ui.targetsTree)
			self.tree.append(T)
			self.connect(T.thread, QtCore.SIGNAL("pingFinished()"), self.increaseProgress)

	def rescan(self):
		self.ui.progressBar.setValue(0)
		for i in self.tree:
			i.setSelected(False)
			i.thread.start()

	def increaseProgress(self):
		p = self.ui.progressBar
		p.setValue(p.value() + int(round(100.0/self.total)))

	def backClicked(self):
		pass

	def accept(self):
		for i in self.tree:
			if i.isSelected():
				self.targets.append(i.text(0))
		QtGui.QDialog.accept(self)

	def exec_(self, targets):
		"""Reimplemented exec_ function from QtGui.QDialog

		@param	self		A ScanTargets instance
		@param	targets		A list containing IP address
		@return				A list containing IP address
		"""
		if not targets:
			return([])

		self.scan(targets)
		r = QtGui.QDialog.exec_(self)

		if r: return(self.targets)
		else: return([])

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
		self.thread.start()

	def run(self):
		self.setText(1, self.tr("Scanning", "a host or IP on add targets dialog"))
		#self.thread.msleep(int(2000*random()))
		self.on = subprocess.Popen("ping -c 4 {0}".format(self.address).split(),
			stdout=subprocess.PIPE)
		if not self.on.wait():
			self.setSelected(True)
			self.setText(1, self.tr("Online", "host connected"))
		else:
			self.setSelected(False)
			self.setText(1, self.tr("Seens Offline", "if the host has not been answered"))
		self.thread.emit(QtCore.SIGNAL("pingFinished()"))
