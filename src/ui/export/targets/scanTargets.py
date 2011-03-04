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
from ltmt.ui.export.targets.Ui_scanTargetsDialog import Ui_ScanTargetsDialog
from ltmt.ui.export.targets.threadedScan import ThreadedScan

class ScanTargets(QtGui.QDialog):
	"""Creates scan targets dialog"""

	# Implement custom signal to carry IP list
	ipDict = QtCore.pyqtSignal(dict, name="ipDict")

	def __init__(self, parent=None):
		"""Instantiate a ScanTargets object

		@param	self		A ScanTargets instance
		@param	parent		A QtGui.QWidget parent object
		"""
		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_ScanTargetsDialog()
		self.ui.setupUi(self)

		self.makeMenu()

		self.threads = []
		self.total = 0.0
		self.finished = 0.0

	def makeMenu(self):
		self.menu = QtGui.QMenu(self.ui.selectButton)

		self.menu.addAction(self.tr("Select All"))\
			.triggered.connect(self.selectAll)
		self.menu.addAction(self.tr("Select Online"))\
			.triggered.connect(self.selectOnline)
		self.menu.addAction(self.tr("Select None"))\
			.triggered.connect(self.selectNone)
		self.menu.addSeparator()
		self.menu.addAction(self.tr("Invert Selection"))\
			.triggered.connect(self.invertSelection)

		self.ui.selectButton.setMenu(self.menu)

	def scan(self, targets):
		self.ui.progressBar.setValue(0)
		self.finished = 0
		self.total = len(targets)
		for i in targets:
			T = ThreadedScan(i, parent=self.ui.targetsTree)
			self.threads.append(T)
			T.finished.connect(self.increaseProgress)
			T.start()

	def rescan(self):
		self.ui.progressBar.setValue(0)
		self.finished = 0
		for i in self.threads:
			i.setSelected(False)
			i.start()

	def increaseProgress(self):
		self.finished += 1
		v = int(round(100.0*(self.finished/self.total)))
		self.ui.progressBar.setValue(v)

	def accept(self):
		targets = {}
		for i in self.threads:
			if i.isSelected():
				targets[i.address] = i.online
		self.ipDict.emit(targets)
		QtGui.QDialog.accept(self)

	def show(self, targets):
		self.total = len(targets)
		if self.isVisible():
			return
		self.scan(targets)
		QtGui.QWidget.show(self)

	def selectAll(self):
		for i in self.threads:
			i.setSelected(True)

	def selectNone(self):
		for i in self.threads:
			i.setSelected(False)

	def selectOnline(self):
		for i in self.threads:
			if i.online: i.setSelected(True)
			else: i.setSelected(False)

	def invertSelection(self):
		for i in self.threads:
			i.setSelected(not i.isSelected())

