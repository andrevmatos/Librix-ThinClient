# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/edit/editWidget.ui'
#
# Created: Mon Jan 17 15:43:14 2011
#      by: PyQt4 UI code generator 4.8.2
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
		EditWidget.resize(650, 550)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(EditWidget.sizePolicy().hasHeightForWidth())
		EditWidget.setSizePolicy(sizePolicy)
		self.horizontalLayout = QtGui.QHBoxLayout(EditWidget)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.profilesListWidget = QtGui.QWidget(EditWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.profilesListWidget.sizePolicy().hasHeightForWidth())
		self.profilesListWidget.setSizePolicy(sizePolicy)
		self.profilesListWidget.setMaximumSize(QtCore.QSize(200, 16777215))
		self.profilesListWidget.setObjectName(_fromUtf8("profilesListWidget"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.profilesListWidget)
		self.verticalLayout_3.setMargin(0)
		self.verticalLayout_3.setMargin(0)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.profilesLabel = QtGui.QLabel(self.profilesListWidget)
		self.profilesLabel.setObjectName(_fromUtf8("profilesLabel"))
		self.verticalLayout_3.addWidget(self.profilesLabel)
		self.profilesList = QtGui.QListWidget(self.profilesListWidget)
		self.profilesList.setObjectName(_fromUtf8("profilesList"))
		self.verticalLayout_3.addWidget(self.profilesList)
		self.EditToolBarWidget = QtGui.QWidget(self.profilesListWidget)
		self.EditToolBarWidget.setMinimumSize(QtCore.QSize(0, 0))
		self.EditToolBarWidget.setObjectName(_fromUtf8("EditToolBarWidget"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.EditToolBarWidget)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.addButton = QtGui.QToolButton(self.EditToolBarWidget)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.addButton.setIcon(icon)
		self.addButton.setIconSize(QtCore.QSize(24, 24))
		self.addButton.setAutoRaise(True)
		self.addButton.setObjectName(_fromUtf8("addButton"))
		self.horizontalLayout_2.addWidget(self.addButton)
		self.delButton = QtGui.QToolButton(self.EditToolBarWidget)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/document-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.delButton.setIcon(icon1)
		self.delButton.setIconSize(QtCore.QSize(24, 24))
		self.delButton.setAutoRaise(True)
		self.delButton.setObjectName(_fromUtf8("delButton"))
		self.horizontalLayout_2.addWidget(self.delButton)
		self.separator = QtGui.QFrame(self.EditToolBarWidget)
		self.separator.setFrameShape(QtGui.QFrame.VLine)
		self.separator.setFrameShadow(QtGui.QFrame.Sunken)
		self.separator.setObjectName(_fromUtf8("separator"))
		self.horizontalLayout_2.addWidget(self.separator)
		self.editButton = QtGui.QToolButton(self.EditToolBarWidget)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/document-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.editButton.setIcon(icon2)
		self.editButton.setIconSize(QtCore.QSize(24, 24))
		self.editButton.setAutoRaise(True)
		self.editButton.setObjectName(_fromUtf8("editButton"))
		self.horizontalLayout_2.addWidget(self.editButton)
		self.duplicateButton = QtGui.QToolButton(self.EditToolBarWidget)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/document-edit-verify.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.duplicateButton.setIcon(icon3)
		self.duplicateButton.setIconSize(QtCore.QSize(24, 24))
		self.duplicateButton.setAutoRaise(True)
		self.duplicateButton.setObjectName(_fromUtf8("duplicateButton"))
		self.horizontalLayout_2.addWidget(self.duplicateButton)
		spacerItem = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.verticalLayout_3.addWidget(self.EditToolBarWidget)
		self.horizontalLayout.addWidget(self.profilesListWidget)
		self.editProfilesWidget = QtGui.QWidget(EditWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.editProfilesWidget.sizePolicy().hasHeightForWidth())
		self.editProfilesWidget.setSizePolicy(sizePolicy)
		self.editProfilesWidget.setObjectName(_fromUtf8("editProfilesWidget"))
		self.verticalLayout_4 = QtGui.QVBoxLayout(self.editProfilesWidget)
		self.verticalLayout_4.setMargin(0)
		self.verticalLayout_4.setMargin(0)
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.horizontalLayout.addWidget(self.editProfilesWidget)

		self.retranslateUi(EditWidget)
		QtCore.QObject.connect(self.profilesList, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), EditWidget.activateProfileSummary)
		QtCore.QObject.connect(self.delButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EditWidget.delProfile)
		QtCore.QObject.connect(self.editButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EditWidget.editProfile)
		QtCore.QObject.connect(self.duplicateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EditWidget.duplicateProfile)
		QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EditWidget.addProfile)
		QtCore.QMetaObject.connectSlotsByName(EditWidget)

	def retranslateUi(self, EditWidget):
		EditWidget.setWindowTitle(QtGui.QApplication.translate("EditWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.profilesLabel.setText(QtGui.QApplication.translate("EditWidget", "Profiles:", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setToolTip(QtGui.QApplication.translate("EditWidget", "New Profile", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setWhatsThis(QtGui.QApplication.translate("EditWidget", "Creates an empty profile", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("EditWidget", "New Profile", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setToolTip(QtGui.QApplication.translate("EditWidget", "Remove Profile", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setWhatsThis(QtGui.QApplication.translate("EditWidget", "Delete the selected profile. This action can\'t be undo", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setText(QtGui.QApplication.translate("EditWidget", "Remove Profile", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setToolTip(QtGui.QApplication.translate("EditWidget", "Edit Profile", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setWhatsThis(QtGui.QApplication.translate("EditWidget", "Edit selected profile", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setText(QtGui.QApplication.translate("EditWidget", "Edit Profile", None, QtGui.QApplication.UnicodeUTF8))
		self.duplicateButton.setToolTip(QtGui.QApplication.translate("EditWidget", "Duplicate Profile", None, QtGui.QApplication.UnicodeUTF8))
		self.duplicateButton.setWhatsThis(QtGui.QApplication.translate("EditWidget", "Creates a new profile with the same configuration of the selected one.", None, QtGui.QApplication.UnicodeUTF8))
		self.duplicateButton.setText(QtGui.QApplication.translate("EditWidget", "Duplicate Profile", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	EditWidget = QtGui.QWidget()
	ui = Ui_EditWidget()
	ui.setupUi(EditWidget)
	EditWidget.show()
	sys.exit(app.exec_())

