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

from Ui_addUser import Ui_AddUser

class AddUser(QtGui.QDialog):
	"""This class provides a add user dialog feature to users page of LTMT"""
	def __init__(self, parent=None):
		"""Init method
		
		@param	self		A AddUser instance
		@param	parent		Parent QtGui.QWidget object
		"""
		self.parent = parent
		
		QtGui.QDialog.__init__(self)
		
		self.ui = Ui_AddUser()
		self.ui.setupUi(self)
