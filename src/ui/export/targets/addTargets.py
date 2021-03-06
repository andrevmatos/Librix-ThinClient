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
from ltmt.ui.export.targets.Ui_addTargetsDialog import Ui_AddTargetsDialog

from ltmt.lib.ip import IPRange,Subnetwork

class AddTargets(QtGui.QDialog):
	"""Creates add targets dialog"""

	# Implement custom signal to carry IP list
	ipList = QtCore.pyqtSignal(list, name="ipList")

	def __init__(self, parent=None):
		"""Instantiate a AddTargets object

		@param	self		An AddTargets instance
		@param	parent		A QtGui.QWidget parent object
		"""
		QtGui.QDialog.__init__(self, parent)

		self.targets = []

		self.ui = Ui_AddTargetsDialog()
		self.ui.setupUi(self)

		self.opts = {
			self.ui.singleRadio: self.ui.singleWidget,
			self.ui.hostnameRadio: self.ui.hostnameWidget,
			self.ui.rangeRadio: self.ui.rangeWidget,
			self.ui.subnetRadio: self.ui.subnetWidget,
		}

		self.ipValidator = QtGui.QRegExpValidator(QtCore.QRegExp(
			r"0*(2(5[0-5]|[0-4]\d)|1?\d{1,2})"+
			r"(\.0*(2(5[0-5]|[0-4]\d)|1?\d{1,2})){3}"), self)
		self.urlValidator = QtGui.QRegExpValidator(QtCore.QRegExp(
			r"^[\x20-\x7E]*$"), self)

		self.ui.singleIpLine.setValidator(self.ipValidator)
		self.ui.fromIPLine.setValidator(self.ipValidator)
		self.ui.toIPLine.setValidator(self.ipValidator)
		self.ui.IPLine.setValidator(self.ipValidator)
		self.ui.netmaskLine.setValidator(self.ipValidator)
		self.ui.hostnameLine.setValidator(self.urlValidator)

		self.optClicked()

	def optClicked(self):
		"""An new option was selected on Dialog

		then, setEnabled False on others widgets
		@param	self		An ExportPage instance
		"""
		for i in self.opts:
			if i.isChecked():
				self.opts[i].setEnabled(True)
			else:
				self.opts[i].setEnabled(False)
		self.parseTargets()

	def accept(self):
		if self.targets:
			self.ipList.emit(self.targets)
			QtGui.QDialog.accept(self)

	def parseTargets(self):
		self.targets = []

		if self.ui.singleRadio.isChecked():
			t = self.ui.singleIpLine.text()
			if self.ipValidator.validate(t, len(t))[0] == 2:
				self.targets.append(t)
		elif self.ui.hostnameRadio.isChecked():
			t = self.ui.hostnameLine.text()
			if self.urlValidator.validate(t, len(t))[0] == 2:
				self.targets.append(t)
		elif self.ui.rangeRadio.isChecked():
			f = self.ui.fromIPLine.text()
			t = self.ui.toIPLine.text()
			if self.ipValidator.validate(f, len(f))[0] == \
				self.ipValidator.validate(t, len(t))[0] == 2:
				for i in IPRange(f, t):
					self.targets.append(i)

		elif self.ui.subnetRadio.isChecked():
			i = self.ui.IPLine.text()
			n = self.ui.netmaskLine.text()
			if self.ipValidator.validate(i, len(i))[0] == \
				self.ipValidator.validate(n, len(n))[0] == 2:
				for i in Subnetwork(i, n):
					self.targets.append(i)

		if self.targets:
			self.ui.nextButton.setEnabled(True)
		else:
			self.ui.nextButton.setEnabled(False)
