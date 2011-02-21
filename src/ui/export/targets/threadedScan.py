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

from urllib.request import urlopen
from random import random


class ThreadedScan(QtCore.QThread):
	"""Class to provide network scan of a host, adding it to parent tree"""
	def __init__(self, address, version='', parent=None):
		"""Init method

		@param	self		A ThreadedScan instance
		@param	address		A string containing a valid ip or host address
		@param	parent		Parent QtGui.QTreeWidget object,
							where first column is address and second, version
		"""
		self.parent = parent
		self.address = address

		QtCore.QThread.__init__(self)

		self.treeItem = QtGui.QTreeWidgetItem(parent)
		self.treeItem.setText(0, address)

		if version: self.treeItem.setText(1, version)
		else: self.treeItem.setText(1, self.tr("Seens Offline"))

	def setSelected(self, value):
		"""Set state of self.treeItem

		@param	self		A ThreadedScan instance
		@param	value		Bool, if True, set treeItem selected
		"""
		self.treeItem.setSelected(value)

	def isSelected(self):
		"""Return state of self.treeItem

		@param	self		A ThreadedScan instance
		@return				Bool, True fi treeItem is selected
		"""
		return(self.treeItem.isSelected())

	def run(self):
		"""Main method of thread, scan target

		Stores version string in self.online, if host is up
		@param	self		A ThreadedScan instance
		"""
		self.treeItem.setText(1, self.tr("Scanning",
			"a host or IP on add targets dialog"))
		self.online = None
		# if all threads starts simultaneously, app may segfault,
		self.msleep(int(3000*random()))	# then wait [0-3]s

		for k in range(1):
			try:
				u = urlopen("http://{0}:8088".format(self.address), None, 5)
				self.online = u.read().decode('utf-8').strip()
				break
			except:
				continue

		if self.online:
			self.treeItem.setSelected(True)
			self.treeItem.setText(1, self.online)
		else:
			self.treeItem.setSelected(False)
			self.treeItem.setText(1, self.tr("Offline",
			"if the host has not responded"))
