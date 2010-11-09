# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/exportWidget.ui'
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
		self.toolBar = QtGui.QWidget(ExportWidget)
		self.toolBar.setMinimumSize(QtCore.QSize(0, 48))
		self.toolBar.setMaximumSize(QtCore.QSize(16777215, 64))
		self.toolBar.setObjectName(_fromUtf8("toolBar"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.toolBar)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.backButton = QtGui.QToolButton(self.toolBar)
		self.backButton.setEnabled(False)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.backButton.setIcon(icon)
		self.backButton.setIconSize(QtCore.QSize(26, 26))
		self.backButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.backButton.setAutoRaise(True)
		self.backButton.setObjectName(_fromUtf8("backButton"))
		self.horizontalLayout_3.addWidget(self.backButton)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem)
		self.mainVLayout.addWidget(self.toolBar)
		self.optionsPanel = QtGui.QFrame(ExportWidget)
		self.optionsPanel.setStyleSheet(_fromUtf8("QFrame {\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"}"))
		self.optionsPanel.setFrameShape(QtGui.QFrame.StyledPanel)
		self.optionsPanel.setFrameShadow(QtGui.QFrame.Raised)
		self.optionsPanel.setObjectName(_fromUtf8("optionsPanel"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.optionsPanel)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.localBox = QtGui.QGroupBox(self.optionsPanel)
		self.localBox.setAutoFillBackground(False)
		self.localBox.setStyleSheet(_fromUtf8("QGroupBox {\n"
"	font-weight: bold;\n"
"	border: 1px solid darkgray;\n"
"	border-radius: 3px;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	border-bottom-color: rgba(255,255,255,0);\n"
"	border-right-color: rgba(255,255,255,0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.347212, y2:0.483, stop:0 rgba(196, 196, 196, 128), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	color: rgb(100, 100, 100);\n"
"	top: 5px;\n"
"	left: 5px;\n"
"}"))
		self.localBox.setAlignment(QtCore.Qt.AlignCenter)
		self.localBox.setFlat(False)
		self.localBox.setCheckable(False)
		self.localBox.setObjectName(_fromUtf8("localBox"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.localBox)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.localList = QtGui.QListWidget(self.localBox)
		self.localList.setStyleSheet(_fromUtf8("background-color: rgba(0,0,0,0);\n"
"font-weight: bold;\n"
"padding: 30px;"))
		self.localList.setFrameShape(QtGui.QFrame.NoFrame)
		self.localList.setAutoScrollMargin(0)
		self.localList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.localList.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
		self.localList.setIconSize(QtCore.QSize(64, 64))
		self.localList.setTextElideMode(QtCore.Qt.ElideNone)
		self.localList.setMovement(QtGui.QListView.Static)
		self.localList.setFlow(QtGui.QListView.LeftToRight)
		self.localList.setLayoutMode(QtGui.QListView.SinglePass)
		self.localList.setGridSize(QtCore.QSize(120, 96))
		self.localList.setViewMode(QtGui.QListView.IconMode)
		self.localList.setUniformItemSizes(False)
		self.localList.setObjectName(_fromUtf8("localList"))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/go-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/go-down.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
		item = QtGui.QListWidgetItem(self.localList)
		item.setIcon(icon1)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/go-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/go-up.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
		item = QtGui.QListWidgetItem(self.localList)
		item.setIcon(icon2)
		self.horizontalLayout.addWidget(self.localList)
		self.verticalLayout_2.addWidget(self.localBox)
		self.remoteBox = QtGui.QGroupBox(self.optionsPanel)
		self.remoteBox.setAutoFillBackground(False)
		self.remoteBox.setStyleSheet(_fromUtf8("QGroupBox {\n"
"	font-weight: bold;\n"
"	border: 1px solid darkgray;\n"
"	border-radius: 3px;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	border-bottom-color: rgba(255,255,255,0);\n"
"	border-right-color: rgba(255,255,255,0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.347212, y2:0.483, stop:0 rgba(196, 196, 196, 128), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	color: rgb(100, 100, 100);\n"
"	top: 5px;\n"
"	left: 5px;\n"
"}"))
		self.remoteBox.setObjectName(_fromUtf8("remoteBox"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.remoteBox)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.remoteList = QtGui.QListWidget(self.remoteBox)
		self.remoteList.setStyleSheet(_fromUtf8("background-color: rgba(0,0,0,0);\n"
"font-weight: bold;\n"
"padding: 30px;"))
		self.remoteList.setFrameShape(QtGui.QFrame.NoFrame)
		self.remoteList.setAutoScrollMargin(0)
		self.remoteList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.remoteList.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
		self.remoteList.setIconSize(QtCore.QSize(64, 64))
		self.remoteList.setTextElideMode(QtCore.Qt.ElideNone)
		self.remoteList.setMovement(QtGui.QListView.Static)
		self.remoteList.setFlow(QtGui.QListView.LeftToRight)
		self.remoteList.setResizeMode(QtGui.QListView.Adjust)
		self.remoteList.setGridSize(QtCore.QSize(120, 96))
		self.remoteList.setViewMode(QtGui.QListView.IconMode)
		self.remoteList.setUniformItemSizes(False)
		self.remoteList.setObjectName(_fromUtf8("remoteList"))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/net-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/net-down.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
		item = QtGui.QListWidgetItem(self.remoteList)
		item.setIcon(icon3)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/net-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/net-up.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
		item = QtGui.QListWidgetItem(self.remoteList)
		item.setIcon(icon4)
		self.horizontalLayout_2.addWidget(self.remoteList)
		self.verticalLayout_2.addWidget(self.remoteBox)
		self.mainVLayout.addWidget(self.optionsPanel)

		self.retranslateUi(ExportWidget)
		QtCore.QObject.connect(self.localList, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), self.remoteList.clearSelection)
		QtCore.QObject.connect(self.remoteList, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), self.localList.clearSelection)
		QtCore.QObject.connect(self.remoteList, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.localList.clearSelection)
		QtCore.QObject.connect(self.localList, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.remoteList.clearSelection)
		QtCore.QMetaObject.connectSlotsByName(ExportWidget)

	def retranslateUi(self, ExportWidget):
		ExportWidget.setWindowTitle(QtGui.QApplication.translate("ExportWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.backButton.setText(QtGui.QApplication.translate("ExportWidget", "Back", None, QtGui.QApplication.UnicodeUTF8))
		self.localBox.setTitle(QtGui.QApplication.translate("ExportWidget", "Local", None, QtGui.QApplication.UnicodeUTF8))
		__sortingEnabled = self.localList.isSortingEnabled()
		self.localList.setSortingEnabled(False)
		self.localList.item(0).setText(QtGui.QApplication.translate("ExportWidget", "Local Import", None, QtGui.QApplication.UnicodeUTF8))
		self.localList.item(1).setText(QtGui.QApplication.translate("ExportWidget", "Local Export", None, QtGui.QApplication.UnicodeUTF8))
		self.localList.setSortingEnabled(__sortingEnabled)
		self.remoteBox.setTitle(QtGui.QApplication.translate("ExportWidget", "Remote", None, QtGui.QApplication.UnicodeUTF8))
		__sortingEnabled = self.remoteList.isSortingEnabled()
		self.remoteList.setSortingEnabled(False)
		self.remoteList.item(0).setText(QtGui.QApplication.translate("ExportWidget", "Remote Import", None, QtGui.QApplication.UnicodeUTF8))
		self.remoteList.item(1).setText(QtGui.QApplication.translate("ExportWidget", "Remote Export", None, QtGui.QApplication.UnicodeUTF8))
		self.remoteList.setSortingEnabled(__sortingEnabled)

from . import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ExportWidget = QtGui.QWidget()
	ui = Ui_ExportWidget()
	ui.setupUi(ExportWidget)
	ExportWidget.show()
	sys.exit(app.exec_())

