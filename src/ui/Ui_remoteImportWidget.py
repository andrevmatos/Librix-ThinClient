# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/remoteImportWidget.ui'
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

class Ui_remoteImport(object):
	def setupUi(self, remoteImport):
		remoteImport.setObjectName(_fromUtf8("remoteImport"))
		remoteImport.resize(650, 550)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(remoteImport.sizePolicy().hasHeightForWidth())
		remoteImport.setSizePolicy(sizePolicy)
		self.mainVLayout = QtGui.QVBoxLayout(remoteImport)
		self.mainVLayout.setMargin(4)
		self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
		self.pushButton = QtGui.QPushButton(remoteImport)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.mainVLayout.addWidget(self.pushButton)

		self.retranslateUi(remoteImport)
		QtCore.QMetaObject.connectSlotsByName(remoteImport)

	def retranslateUi(self, remoteImport):
		remoteImport.setWindowTitle(QtGui.QApplication.translate("remoteImport", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("remoteImport", "PushButton 3", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	remoteImport = QtGui.QWidget()
	ui = Ui_remoteImport()
	ui.setupUi(remoteImport)
	remoteImport.show()
	sys.exit(app.exec_())

