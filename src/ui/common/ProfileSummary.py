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

from PyQt4 import QtGui
from ltmt.ui.common.Ui_profileSummary import Ui_Summary

class ProfileSummary(QtGui.QWidget):
	"""Creates a frame with profile summary"""
	def __init__(self, configparser, moduleparser, vert=False, parent=None):
		"""Instantiate a ProfilesSummary object

		@param	self		A ProfilesSummary instance
		@param	configparser	A LTCConfigParser instance
		@param	vert		Bool. Vertical alignment of categories
		"""
		self.parent = parent
		self.moduleparser = moduleparser
		self.configparser = configparser

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_Summary()
		self.ui.setupUi(self)

		if vert:
			self.ui.horizontalLayout.setDirection(QtGui.QBoxLayout.TopToBottom)

		self.configsWidgets = {}

	def setSummary(self, profile=''):
		"""Set the summary of _profile on _label

		@param	self		A ProfilesSummary instance
		@param	profile		A string containing the name of the profile
		"""
		if not profile:
			self.ui.title.setText('')
			for c in self.configsWidgets:
				self.configsWidgets[c].setText('')
		else:
			self.ui.title.setText(self.tr("<h2><b>Name: "+
				"<font color=blue>{0}</font></b></h2>\n").format(profile))

			# for each category, creates a QLabel and add the configurations
			for c in self.moduleparser.getCategoriesList():
				config = "<h4>{0}:</h4>\n".format(c)

				for o in self.moduleparser.getModulesList(c):
					config += "<h6> ➜ {0}: ".format(o)
					if self.configparser.getOption(profile, o):
						config += self.tr("<font color=green><b>On</b></font></h6>\n",
							"if option is activated on profile")
					else:
						config += self.tr("<font color=red><b>Off</b></font></h6>\n",
							"if option is deactivated on profile")

				if not c in self.configsWidgets:
					self.configsWidgets[c] = QtGui.QLabel(self.ui.configsWidget)
					self.ui.horizontalLayout.addWidget(self.configsWidgets[c])

				self.configsWidgets[c].setText(config)

#	def show(self):
#		"""Reimplementation of QtGui.QWidget.show method"""
#		if self.parent.current:
#			self.parent.current.hide()
#
#		self.parent.current = self
#		QtGui.QWidget.show(self)
