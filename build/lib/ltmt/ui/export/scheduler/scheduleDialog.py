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

from PyQt4 import QtGui, QtCore

from ltmt.ui.export.scheduler.Ui_scheduleDialog import Ui_Scheduler

class Scheduler(QtGui.QDialog):
	"""Show a progress dialog of export operations through SSH"""
	def __init__(self, to, parent=None):
		"""Init method

		@param	self		A Scheduler instance
		@param	to			A QDateTime object containint target date time
		@param	parent		Parent QtGui.QWidget
		"""
		self.parent = parent

		self.begin = QtCore.QDateTime.currentDateTime()
		self.end = to

		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_Scheduler()
		self.ui.setupUi(self)

		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update)

		self.timer.start(1000)
		self.update()

	def update(self):
		"""Update counters

		@param	self		A Scheduler instance
		"""
		current = QtCore.QDateTime.currentDateTime()
		if current == self.end:
			self.accept()

		elapsed = QtCore.QDateTime()
		elapsed.addSecs(self.begin.secsTo(current))
		remaining = QtCore.QDateTime()
		remaining.addSecs(current.secsTo(self.end))

		porc = float(current.toMSecsSinceEpoch() - self.begin.toMSecsSinceEpoch())\
			/float(self.end.toMSecsSinceEpoch() - self.begin.toMSecsSinceEpoch())
		self.ui.progressBar.setValue(int(round(porc)))

		self.ui.progressLabel.setText(self.ui.progressLabel.text().format(
			self.begin.toString(), elapsed.toString(), remaining.toString(),
			self.end.toString()))
