# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/export/scanTargetsDialog.ui'
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

class Ui_ScanTargetsDialog(object):
	def setupUi(self, ScanTargetsDialog):
		ScanTargetsDialog.setObjectName(_fromUtf8("ScanTargetsDialog"))
		ScanTargetsDialog.resize(570, 360)
		self.verticalLayout = QtGui.QVBoxLayout(ScanTargetsDialog)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.helpLabel = QtGui.QLabel(ScanTargetsDialog)
		self.helpLabel.setObjectName(_fromUtf8("helpLabel"))
		self.verticalLayout.addWidget(self.helpLabel)
		self.mainWidget = QtGui.QWidget(ScanTargetsDialog)
		self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.mainWidget)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.targetsTree = QtGui.QTreeWidget(self.mainWidget)
		self.targetsTree.setAlternatingRowColors(True)
		self.targetsTree.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
		self.targetsTree.setIndentation(20)
		self.targetsTree.setAnimated(True)
		self.targetsTree.setWordWrap(True)
		self.targetsTree.setObjectName(_fromUtf8("targetsTree"))
		self.targetsTree.header().setDefaultSectionSize(400)
		self.horizontalLayout_2.addWidget(self.targetsTree)
		self.verticalLayout.addWidget(self.mainWidget)
		self.buttonBox = QtGui.QWidget(ScanTargetsDialog)
		self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 35))
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.buttonBox)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.backButton = QtGui.QPushButton(self.buttonBox)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/remove_icon/arrow-left-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.backButton.setIcon(icon)
		self.backButton.setObjectName(_fromUtf8("backButton"))
		self.horizontalLayout.addWidget(self.backButton)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.cancelButton = QtGui.QPushButton(self.buttonBox)
		self.cancelButton.setMinimumSize(QtCore.QSize(100, 0))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.cancelButton.setIcon(icon1)
		self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
		self.horizontalLayout.addWidget(self.cancelButton)
		self.nextButton = QtGui.QPushButton(self.buttonBox)
		self.nextButton.setMinimumSize(QtCore.QSize(100, 0))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/ok.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.nextButton.setIcon(icon2)
		self.nextButton.setObjectName(_fromUtf8("nextButton"))
		self.horizontalLayout.addWidget(self.nextButton)
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(ScanTargetsDialog)
		QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ScanTargetsDialog.close)
		QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ScanTargetsDialog.backClicked)
		QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ScanTargetsDialog.accept)
		QtCore.QMetaObject.connectSlotsByName(ScanTargetsDialog)

	def retranslateUi(self, ScanTargetsDialog):
		ScanTargetsDialog.setWindowTitle(QtGui.QApplication.translate("ScanTargetsDialog", "Scan targets - Step 2/2", None, QtGui.QApplication.UnicodeUTF8))
		self.helpLabel.setText(QtGui.QApplication.translate("ScanTargetsDialog", "Select hosts to add, and click Ok", None, QtGui.QApplication.UnicodeUTF8))
		self.targetsTree.setSortingEnabled(True)
		self.targetsTree.headerItem().setText(0, QtGui.QApplication.translate("ScanTargetsDialog", "Address", None, QtGui.QApplication.UnicodeUTF8))
		self.targetsTree.headerItem().setText(1, QtGui.QApplication.translate("ScanTargetsDialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
		self.backButton.setText(QtGui.QApplication.translate("ScanTargetsDialog", "Back", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setText(QtGui.QApplication.translate("ScanTargetsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
		self.nextButton.setText(QtGui.QApplication.translate("ScanTargetsDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ScanTargetsDialog = QtGui.QDialog()
	ui = Ui_ScanTargetsDialog()
	ui.setupUi(ScanTargetsDialog)
	ScanTargetsDialog.show()
	sys.exit(app.exec_())

