# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/profileEdit.ui'
#
# Created: Mon Oct 25 16:13:01 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_EditProfile(object):
	def setupUi(self, EditProfile):
		EditProfile.setObjectName(_fromUtf8("EditProfile"))
		EditProfile.resize(450, 550)
		self.MainVerticalLayout = QtGui.QVBoxLayout(EditProfile)
		self.MainVerticalLayout.setMargin(0)
		self.MainVerticalLayout.setObjectName(_fromUtf8("MainVerticalLayout"))
		self.profileName = QtGui.QLineEdit(EditProfile)
		self.profileName.setObjectName(_fromUtf8("profileName"))
		self.MainVerticalLayout.addWidget(self.profileName)
		self.configBox = QtGui.QGroupBox(EditProfile)
		self.configBox.setObjectName(_fromUtf8("configBox"))
		self.verticalLayout = QtGui.QVBoxLayout(self.configBox)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.configToolBox = QtGui.QToolBox(self.configBox)
		self.configToolBox.setObjectName(_fromUtf8("configToolBox"))
		self.page = QtGui.QWidget()
		self.page.setGeometry(QtCore.QRect(0, 0, 426, 420))
		self.page.setObjectName(_fromUtf8("page"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.scrollArea = QtGui.QScrollArea(self.page)
		self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 418, 412))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.verticalLayout_3.addWidget(self.pushButton)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.verticalLayout_2.addWidget(self.scrollArea)
		self.configToolBox.addItem(self.page, _fromUtf8(""))
		self.verticalLayout.addWidget(self.configToolBox)
		self.MainVerticalLayout.addWidget(self.configBox)
		self.buttonBox = QtGui.QDialogButtonBox(EditProfile)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.MainVerticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(EditProfile)
		self.configToolBox.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(EditProfile)

	def retranslateUi(self, EditProfile):
		EditProfile.setWindowTitle(QtGui.QApplication.translate("EditProfile", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.profileName.setToolTip(QtGui.QApplication.translate("EditProfile", "Profile Name", None, QtGui.QApplication.UnicodeUTF8))
		self.profileName.setText(QtGui.QApplication.translate("EditProfile", "profileName", None, QtGui.QApplication.UnicodeUTF8))
		self.configBox.setTitle(QtGui.QApplication.translate("EditProfile", "Profile Configuration", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("EditProfile", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
		self.configToolBox.setItemText(self.configToolBox.indexOf(self.page), QtGui.QApplication.translate("EditProfile", "Page 1", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	EditProfile = QtGui.QWidget()
	ui = Ui_EditProfile()
	ui.setupUi(EditProfile)
	EditProfile.show()
	sys.exit(app.exec_())

