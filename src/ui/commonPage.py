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

import string
from random import choice

from PyQt4 import QtCore,QtGui

from ui.Ui_profileSummary import Ui_Summary
from ui.Ui_tabItemWidget import Ui_tabWidget

def passwdGen(size=8):
	""" Generates a password (random letters and digits string) of size lenght

	@param	size		The string lenght
	"""
	return(''.join([choice(string.ascii_letters + string.digits)\
		for i in range(size)]))


class LeftMenuItem(QtGui.QListWidgetItem):
	""" Creates a item on leftMenu """
	def __init__(self, parent, text, icon):
		""" Instantiate a LeftMenuItem object

		@param	self		A LeftMenuItem instance
		@param	parent		A QListWidget widget object
		@param	text		A string to use as name of the item
		@param	icon		A QIcon object, to use in interface
		"""
		self.parent = parent

		QtGui.QListWidgetItem.__init__(self, self.parent)

		self.ui = Ui_tabWidget()
		self.tabWidget = QtGui.QWidget()
		self.ui.setupUi(self.tabWidget)
		self.setSizeHint(self.tabWidget.size())

		self.ui.iconLabel.setPixmap(icon.pixmap(QtCore.QSize(48, 48)))
		self.ui.titleLabel.setText('<b>{0}</b>'.format(text))

		self.parent.setItemWidget(self, self.tabWidget)

class ProfilesSummary(QtGui.QWidget):
	""" Creates a frame with profile summary """
	def __init__(self, tcd, parent=None):
		""" Instantiate a ProfilesSummary object

		@param	self		A ProfilesSummary instance
		"""
		self.parent = parent
		self.tcd = tcd

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_Summary()
		self.ui.setupUi(self)

		self.configsWidgets = {}

	def setSummary(self, profile=''):
		""" Set the summary of _profile on _label

		@param	self		A ProfilesSummary instance
		@param	profile		A string containing the name of the profile
		"""
		if not profile:
			self.ui.title.setText('')
			for c in self.configsWidgets:
				self.configsWidgets[c].setText('')
		else:
			self.ui.title.setText("<h2><b>Name: \
				<font color=blue>{0}</font></b></h2>\n".format(profile))

			# for each category, creates a QLabel and add the configurations
			for c in self.tcd.getCategoriesList():
				config = "<h4>{0}:</h4>\n".format(c)

				for o in self.tcd.getOptionsList(c):
					config += "<h6> ➜ {0}: ".format(o)
					if self.tcd.getOption(profile, c, o):
						config += "<font color=green><b>On</b></font></h6>\n"
					else:
						config += "<font color=red><b>Off</b></font></h6>\n"

				if not c in self.configsWidgets:
					self.configsWidgets[c] = QtGui.QLabel(self.ui.configsWidget)
					self.ui.horizontalLayout.addWidget(self.configsWidgets[c])

				self.configsWidgets[c].setText(config)

	def show(self):
		""" Reimplementation of QtGui.QWidget.show method """
		if self.parent.current:
			self.parent.current.hide()

		self.parent.current = self
		QtGui.QWidget.show(self)
