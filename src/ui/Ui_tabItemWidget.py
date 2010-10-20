# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/tabItemWidget.ui'
#
# Created: Tue Oct 19 20:35:02 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_tabWidget(object):
	def setupUi(self, tabWidget):
		tabWidget.setObjectName(_fromUtf8("tabWidget"))
		tabWidget.resize(86, 75)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(tabWidget.sizePolicy().hasHeightForWidth())
		tabWidget.setSizePolicy(sizePolicy)
		tabWidget.setMinimumSize(QtCore.QSize(0, 0))
		self.verticalLayout = QtGui.QVBoxLayout(tabWidget)
		self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
		self.verticalLayout.setMargin(4)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.iconLabel = QtGui.QLabel(tabWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
		self.iconLabel.setSizePolicy(sizePolicy)
		self.iconLabel.setMinimumSize(QtCore.QSize(48, 48))
		self.iconLabel.setText(_fromUtf8(""))
		self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.iconLabel.setObjectName(_fromUtf8("iconLabel"))
		self.verticalLayout.addWidget(self.iconLabel)
		self.titleLabel = QtGui.QLabel(tabWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
		self.titleLabel.setSizePolicy(sizePolicy)
		self.titleLabel.setText(_fromUtf8(""))
		self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
		self.verticalLayout.addWidget(self.titleLabel)

		self.retranslateUi(tabWidget)
		QtCore.QMetaObject.connectSlotsByName(tabWidget)

	def retranslateUi(self, tabWidget):
		tabWidget.setWindowTitle(QtGui.QApplication.translate("tabWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	tabWidget = QtGui.QWidget()
	ui = Ui_tabWidget()
	ui.setupUi(tabWidget)
	tabWidget.show()
	sys.exit(app.exec_())

