# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/export/exportWidget.ui'
#
# Created: Fri Nov 26 13:36:01 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_ExportWidget(object):
	def setupUi(self, ExportWidget):
		ExportWidget.setObjectName(_fromUtf8("ExportWidget"))
		ExportWidget.resize(650, 550)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(ExportWidget.sizePolicy().hasHeightForWidth())
		ExportWidget.setSizePolicy(sizePolicy)
		self.mainVLayout = QtGui.QVBoxLayout(ExportWidget)
		self.mainVLayout.setMargin(4)
		self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))

		self.retranslateUi(ExportWidget)
		QtCore.QMetaObject.connectSlotsByName(ExportWidget)

	def retranslateUi(self, ExportWidget):
		ExportWidget.setWindowTitle(QtGui.QApplication.translate("ExportWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ExportWidget = QtGui.QWidget()
	ui = Ui_ExportWidget()
	ui.setupUi(ExportWidget)
	ExportWidget.show()
	sys.exit(app.exec_())

