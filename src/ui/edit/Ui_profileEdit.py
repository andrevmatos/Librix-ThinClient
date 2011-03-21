# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/edit/profileEdit.ui'
#
# Created: Mon Mar 21 19:42:33 2011
#      by: PyQt4 UI code generator 4.8.3
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
		EditProfile.resize(651, 550)
		self.MainVerticalLayout = QtGui.QVBoxLayout(EditProfile)
		self.MainVerticalLayout.setMargin(0)
		self.MainVerticalLayout.setObjectName(_fromUtf8("MainVerticalLayout"))
		self.profileName = QtGui.QLineEdit(EditProfile)
		self.profileName.setObjectName(_fromUtf8("profileName"))
		self.MainVerticalLayout.addWidget(self.profileName)
		self.classTabs = QtGui.QTabWidget(EditProfile)
		self.classTabs.setObjectName(_fromUtf8("classTabs"))
		self.tab = QtGui.QWidget()
		self.tab.setObjectName(_fromUtf8("tab"))
		self.verticalLayout = QtGui.QVBoxLayout(self.tab)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.optionsList = QtGui.QListWidget(self.tab)
		self.optionsList.setObjectName(_fromUtf8("optionsList"))
		self.verticalLayout.addWidget(self.optionsList)
		self.classTabs.addTab(self.tab, _fromUtf8(""))
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.classTabs.addTab(self.tab_2, _fromUtf8(""))
		self.MainVerticalLayout.addWidget(self.classTabs)
		self.buttonBox = QtGui.QDialogButtonBox(EditProfile)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.MainVerticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(EditProfile)
		self.classTabs.setCurrentIndex(0)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditProfile.readProfileConfig)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditProfile.hide)
		QtCore.QMetaObject.connectSlotsByName(EditProfile)

	def retranslateUi(self, EditProfile):
		EditProfile.setWindowTitle(QtGui.QApplication.translate("EditProfile", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.profileName.setToolTip(QtGui.QApplication.translate("EditProfile", "Profile Name", None, QtGui.QApplication.UnicodeUTF8))
		self.profileName.setText(QtGui.QApplication.translate("EditProfile", "profileName", None, QtGui.QApplication.UnicodeUTF8))
		self.classTabs.setTabText(self.classTabs.indexOf(self.tab), QtGui.QApplication.translate("EditProfile", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
		self.classTabs.setTabText(self.classTabs.indexOf(self.tab_2), QtGui.QApplication.translate("EditProfile", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

from ltmt.ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	EditProfile = QtGui.QWidget()
	ui = Ui_EditProfile()
	ui.setupUi(EditProfile)
	EditProfile.show()
	sys.exit(app.exec_())

