# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/remoteExportWidget.ui'
#
# Created: Mon Nov  8 19:22:23 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_remoteExport(object):
	def setupUi(self, remoteExport):
		remoteExport.setObjectName(_fromUtf8("remoteExport"))
		remoteExport.resize(650, 550)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(remoteExport.sizePolicy().hasHeightForWidth())
		remoteExport.setSizePolicy(sizePolicy)
		self.mainVLayout = QtGui.QVBoxLayout(remoteExport)
		self.mainVLayout.setMargin(4)
		self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
		self.pushButton = QtGui.QPushButton(remoteExport)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.mainVLayout.addWidget(self.pushButton)

		self.retranslateUi(remoteExport)
		QtCore.QMetaObject.connectSlotsByName(remoteExport)

	def retranslateUi(self, remoteExport):
		remoteExport.setWindowTitle(QtGui.QApplication.translate("remoteExport", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("remoteExport", "PushButton 4", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	remoteExport = QtGui.QWidget()
	ui = Ui_remoteExport()
	ui.setupUi(remoteExport)
	remoteExport.show()
	sys.exit(app.exec_())

