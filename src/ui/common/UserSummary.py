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
from ui.common.Ui_userSummary import Ui_Summary

class UserSummary(QtGui.QWidget):
	"""Creates a frame with profile summary"""
	def __init__(self, configparser, moduleparser, parent=None):
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

	def setSummary(self, user=''):
		"""Set the summary of _profile on _label

		@param	self		A ProfilesSummary instance
		@param	profile		A string containing the name of the profile
		"""
		if not user:
			self.ui.title.setText('')
			self.ui.password.setText('')
			self.ui.uid.setText('')
			self.ui.initGroup.setText('')
			self.ui.groups.setText('')
			self.ui.home.setText('')
			self.ui.shell.setText('')
		else:
			opt = self.configparser.getUserSync(user)
			self.ui.title.setText(self.tr("<h2><b>Name: "+
				"<font color=blue>{0}</font></b></h2>\n").format(user))

			self.ui.password.setText(self.tr("<font color=green>Shadow "+
				"Password Hash:</font> <b>{0}</b>").format(opt["passwd"]))
			self.ui.uid.setText(self.tr("<font color=green>"+
				"UID:</font> <b>{0}</b>").format(opt["uid"]))
			self.ui.initGroup.setText(self.tr("<font color=green>"+
				"Initial Group:</font> <b>{0}</b>").format(opt["init_group"]))
			self.ui.groups.setText(self.tr("<font color=green>"+
				"Other Groups:</font> <b>{0}</b>").format(opt["groups"]))
			self.ui.home.setText(self.tr("<font color=green>"+
				"Home:</font> <b>{0}</b>").format(opt["home"]))
			self.ui.shell.setText(self.tr("<font color=green>"+
				"Shell:</font> <b>{0}</b>").format(opt["shell"]))

