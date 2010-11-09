# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/localExportWidget.ui'
#
# Created: Mon Nov  8 19:22:25 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_localExport(object):
	def setupUi(self, localExport):
		localExport.setObjectName(_fromUtf8("localExport"))
		localExport.resize(650, 550)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(localExport.sizePolicy().hasHeightForWidth())
		localExport.setSizePolicy(sizePolicy)
		self.mainVLayout = QtGui.QVBoxLayout(localExport)
		self.mainVLayout.setMargin(4)
		self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
		self.pushButton = QtGui.QPushButton(localExport)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.mainVLayout.addWidget(self.pushButton)

		self.retranslateUi(localExport)
		QtCore.QMetaObject.connectSlotsByName(localExport)

	def retranslateUi(self, localExport):
		localExport.setWindowTitle(QtGui.QApplication.translate("localExport", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("localExport", "PushButton 2", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	localExport = QtGui.QWidget()
	ui = Ui_localExport()
	ui.setupUi(localExport)
	localExport.show()
	sys.exit(app.exec_())

