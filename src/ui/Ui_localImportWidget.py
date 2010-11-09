# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/localImportWidget.ui'
#
# Created: Mon Nov  8 19:22:24 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_localImport(object):
	def setupUi(self, localImport):
		localImport.setObjectName(_fromUtf8("localImport"))
		localImport.resize(650, 550)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(localImport.sizePolicy().hasHeightForWidth())
		localImport.setSizePolicy(sizePolicy)
		self.mainVLayout = QtGui.QVBoxLayout(localImport)
		self.mainVLayout.setMargin(4)
		self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
		self.pushButton = QtGui.QPushButton(localImport)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.mainVLayout.addWidget(self.pushButton)

		self.retranslateUi(localImport)
		QtCore.QMetaObject.connectSlotsByName(localImport)

	def retranslateUi(self, localImport):
		localImport.setWindowTitle(QtGui.QApplication.translate("localImport", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("localImport", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	localImport = QtGui.QWidget()
	ui = Ui_localImport()
	ui.setupUi(localImport)
	localImport.show()
	sys.exit(app.exec_())

