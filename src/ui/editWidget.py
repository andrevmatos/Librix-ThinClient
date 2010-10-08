# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editWidget.ui'
#
# Created: Fri Oct  8 16:27:18 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_EditWidget(object):
	def setupUi(self, EditWidget):
		EditWidget.setObjectName(_fromUtf8("EditWidget"))
		EditWidget.resize(500, 430)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(EditWidget.sizePolicy().hasHeightForWidth())
		EditWidget.setSizePolicy(sizePolicy)
		self.verticalLayout = QtGui.QVBoxLayout(EditWidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.editWidget = QtGui.QWidget(EditWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.editWidget.sizePolicy().hasHeightForWidth())
		self.editWidget.setSizePolicy(sizePolicy)
		self.editWidget.setObjectName(_fromUtf8("editWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.editWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.profilesListWidget = QtGui.QWidget(self.editWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.profilesListWidget.sizePolicy().hasHeightForWidth())
		self.profilesListWidget.setSizePolicy(sizePolicy)
		self.profilesListWidget.setMaximumSize(QtCore.QSize(200, 16777215))
		self.profilesListWidget.setObjectName(_fromUtf8("profilesListWidget"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.profilesListWidget)
		self.verticalLayout_3.setMargin(0)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.profilesLabel = QtGui.QLabel(self.profilesListWidget)
		self.profilesLabel.setObjectName(_fromUtf8("profilesLabel"))
		self.verticalLayout_3.addWidget(self.profilesLabel)
		self.profilesList = QtGui.QListWidget(self.profilesListWidget)
		self.profilesList.setObjectName(_fromUtf8("profilesList"))
		self.verticalLayout_3.addWidget(self.profilesList)
		self.EditToolBarWidget = QtGui.QWidget(self.profilesListWidget)
		self.EditToolBarWidget.setObjectName(_fromUtf8("EditToolBarWidget"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.EditToolBarWidget)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.verticalLayout_3.addWidget(self.EditToolBarWidget)
		self.horizontalLayout.addWidget(self.profilesListWidget)
		self.editProfilesWidget = QtGui.QWidget(self.editWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.editProfilesWidget.sizePolicy().hasHeightForWidth())
		self.editProfilesWidget.setSizePolicy(sizePolicy)
		self.editProfilesWidget.setObjectName(_fromUtf8("editProfilesWidget"))
		self.verticalLayout_4 = QtGui.QVBoxLayout(self.editProfilesWidget)
		self.verticalLayout_4.setMargin(0)
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.horizontalLayout.addWidget(self.editProfilesWidget)
		self.verticalLayout.addWidget(self.editWidget)

		self.retranslateUi(EditWidget)
		QtCore.QMetaObject.connectSlotsByName(EditWidget)

	def retranslateUi(self, EditWidget):
		EditWidget.setWindowTitle(QtGui.QApplication.translate("EditWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.profilesLabel.setText(QtGui.QApplication.translate("EditWidget", "Profiles:", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc
