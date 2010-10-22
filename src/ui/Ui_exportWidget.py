# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/exportWidget.ui'
#
# Created: Fri Oct 22 16:54:14 2010
#      by: PyQt4 UI code generator 4.7.7
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
		ExportWidget.resize(500, 430)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(ExportWidget.sizePolicy().hasHeightForWidth())
		ExportWidget.setSizePolicy(sizePolicy)
		self.verticalLayout = QtGui.QVBoxLayout(ExportWidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.tabWidget = QtGui.QTabWidget(ExportWidget)
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.tab = QtGui.QWidget()
		self.tab.setObjectName(_fromUtf8("tab"))
		self.tabWidget.addTab(self.tab, _fromUtf8(""))
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.verticalLayout.addWidget(self.tabWidget)

		self.retranslateUi(ExportWidget)
		QtCore.QMetaObject.connectSlotsByName(ExportWidget)

	def retranslateUi(self, ExportWidget):
		ExportWidget.setWindowTitle(QtGui.QApplication.translate("ExportWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ExportWidget", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ExportWidget", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ExportWidget = QtGui.QWidget()
	ui = Ui_ExportWidget()
	ui.setupUi(ExportWidget)
	ExportWidget.show()
	sys.exit(app.exec_())

