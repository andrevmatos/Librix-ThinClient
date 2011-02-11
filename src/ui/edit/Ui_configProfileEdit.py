# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/edit/configProfileEdit.ui'
#
# Created: Fri Feb 11 19:24:57 2011
#      by: PyQt4 UI code generator 4.8.3
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
		configsWidget.resize(645, 437)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(configsWidget.sizePolicy().hasHeightForWidth())
		configsWidget.setSizePolicy(sizePolicy)
		self.verticalLayout = QtGui.QVBoxLayout(configsWidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(configsWidget)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.listWidget = QtGui.QListWidget(configsWidget)
		self.listWidget.setEnabled(True)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
		self.listWidget.setSizePolicy(sizePolicy)
		self.listWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.listWidget.setAutoFillBackground(True)
		self.listWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.listWidget.setIconSize(QtCore.QSize(48, 48))
		self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
		self.listWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.listWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.listWidget.setFlow(QtGui.QListView.TopToBottom)
		self.listWidget.setProperty(_fromUtf8("isWrapping"), False)
		self.listWidget.setResizeMode(QtGui.QListView.Adjust)
		self.listWidget.setLayoutMode(QtGui.QListView.Batched)
		self.listWidget.setViewMode(QtGui.QListView.ListMode)
		self.listWidget.setUniformItemSizes(False)
		self.listWidget.setBatchSize(100)
		self.listWidget.setWordWrap(True)
		self.listWidget.setSelectionRectVisible(True)
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.verticalLayout.addWidget(self.listWidget)

		self.retranslateUi(configsWidget)
		QtCore.QMetaObject.connectSlotsByName(configsWidget)

	def retranslateUi(self, configsWidget):
		configsWidget.setWindowTitle(QtGui.QApplication.translate("configsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("configsWidget", "Modules:", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	configsWidget = QtGui.QWidget()
	ui = Ui_configsWidget()
	ui.setupUi(configsWidget)
	configsWidget.show()
	sys.exit(app.exec_())

