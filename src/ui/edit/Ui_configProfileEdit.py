# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/edit/configProfileEdit.ui'
#
# Created: Mon Nov 29 17:15:35 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_configsWidget(object):
	def setupUi(self, configsWidget):
		configsWidget.setObjectName(_fromUtf8("configsWidget"))
		configsWidget.resize(280, 300)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(configsWidget.sizePolicy().hasHeightForWidth())
		configsWidget.setSizePolicy(sizePolicy)
		self.MainVerticalLayout = QtGui.QVBoxLayout(configsWidget)
		self.MainVerticalLayout.setMargin(0)
		self.MainVerticalLayout.setObjectName(_fromUtf8("MainVerticalLayout"))
		self.scrollArea = QtGui.QScrollArea(configsWidget)
		self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.content = QtGui.QWidget(self.scrollArea)
		self.content.setGeometry(QtCore.QRect(0, 0, 280, 300))
		self.content.setObjectName(_fromUtf8("content"))
		self.ConfigVerticalLayout = QtGui.QVBoxLayout(self.content)
		self.ConfigVerticalLayout.setObjectName(_fromUtf8("ConfigVerticalLayout"))
		self.scrollArea.setWidget(self.content)
		self.MainVerticalLayout.addWidget(self.scrollArea)

		self.retranslateUi(configsWidget)
		QtCore.QMetaObject.connectSlotsByName(configsWidget)

	def retranslateUi(self, configsWidget):
		configsWidget.setWindowTitle(QtGui.QApplication.translate("configsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	configsWidget = QtGui.QWidget()
	ui = Ui_configsWidget()
	ui.setupUi(configsWidget)
	configsWidget.show()
	sys.exit(app.exec_())

