# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/mainWindow.ui'
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

class Ui_ThinClient(object):
	def setupUi(self, ThinClient):
		ThinClient.setObjectName(_fromUtf8("ThinClient"))
		ThinClient.resize(800, 600)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/user_icon/system-users.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		ThinClient.setWindowIcon(icon)
		self.widget = QtGui.QWidget(ThinClient)
		self.widget.setObjectName(_fromUtf8("widget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.widget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.topBar = QtGui.QWidget(self.widget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.topBar.sizePolicy().hasHeightForWidth())
		self.topBar.setSizePolicy(sizePolicy)
		self.topBar.setMaximumSize(QtCore.QSize(16777215, 28))
		self.topBar.setObjectName(_fromUtf8("topBar"))
		self.horizontalLayout_4 = QtGui.QHBoxLayout(self.topBar)
		self.horizontalLayout_4.setMargin(0)
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.label = QtGui.QLabel(self.topBar)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout_4.addWidget(self.label)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem)
		self.nameEdit = QtGui.QLineEdit(self.topBar)
		self.nameEdit.setMinimumSize(QtCore.QSize(250, 0))
		self.nameEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.nameEdit.setText(_fromUtf8(""))
		self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
		self.horizontalLayout_4.addWidget(self.nameEdit)
		self.verticalLayout.addWidget(self.topBar)
		self.main = QtGui.QWidget(self.widget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
		self.main.setSizePolicy(sizePolicy)
		self.main.setObjectName(_fromUtf8("main"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.main)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.leftList = QtGui.QWidget(self.main)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.leftList.sizePolicy().hasHeightForWidth())
		self.leftList.setSizePolicy(sizePolicy)
		self.leftList.setMaximumSize(QtCore.QSize(150, 16777215))
		self.leftList.setObjectName(_fromUtf8("leftList"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.leftList)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.listWidget = QtGui.QListWidget(self.leftList)
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
		self.listWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
		self.listWidget.setFlow(QtGui.QListView.TopToBottom)
		self.listWidget.setResizeMode(QtGui.QListView.Adjust)
		self.listWidget.setLayoutMode(QtGui.QListView.Batched)
		self.listWidget.setViewMode(QtGui.QListView.ListMode)
		self.listWidget.setUniformItemSizes(True)
		self.listWidget.setBatchSize(100)
		self.listWidget.setWordWrap(True)
		self.listWidget.setSelectionRectVisible(True)
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.horizontalLayout_2.addWidget(self.listWidget)
		self.horizontalLayout_3.addWidget(self.leftList)
		self.options = QtGui.QWidget(self.main)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.options.sizePolicy().hasHeightForWidth())
		self.options.setSizePolicy(sizePolicy)
		self.options.setObjectName(_fromUtf8("options"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.options)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.horizontalLayout_3.addWidget(self.options)
		self.verticalLayout.addWidget(self.main)
		ThinClient.setCentralWidget(self.widget)
		self.statusbar = QtGui.QStatusBar(ThinClient)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		ThinClient.setStatusBar(self.statusbar)
		self.menuBar = QtGui.QMenuBar(ThinClient)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
		self.menuBar.setObjectName(_fromUtf8("menuBar"))
		self.menuFile = QtGui.QMenu(self.menuBar)
		self.menuFile.setObjectName(_fromUtf8("menuFile"))
		self.menuView = QtGui.QMenu(self.menuBar)
		self.menuView.setObjectName(_fromUtf8("menuView"))
		self.menuEdit = QtGui.QMenu(self.menuBar)
		self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
		ThinClient.setMenuBar(self.menuBar)
		self.toolBar = QtGui.QToolBar(ThinClient)
		self.toolBar.setIconSize(QtCore.QSize(22, 22))
		self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
		self.toolBar.setObjectName(_fromUtf8("toolBar"))
		ThinClient.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
		self.actionOpen = QtGui.QAction(ThinClient)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionOpen.setIcon(icon1)
		self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
		self.actionSave = QtGui.QAction(ThinClient)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSave.setIcon(icon2)
		self.actionSave.setObjectName(_fromUtf8("actionSave"))
		self.actionSave_as = QtGui.QAction(ThinClient)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSave_as.setIcon(icon3)
		self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
		self.actionQuit = QtGui.QAction(ThinClient)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionQuit.setIcon(icon4)
		self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
		self.actionShow_users_profile_summary = QtGui.QAction(ThinClient)
		self.actionShow_users_profile_summary.setCheckable(True)
		self.actionShow_users_profile_summary.setChecked(True)
		self.actionShow_users_profile_summary.setObjectName(_fromUtf8("actionShow_users_profile_summary"))
		self.actionNew = QtGui.QAction(ThinClient)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/profileAction/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionNew.setIcon(icon5)
		self.actionNew.setObjectName(_fromUtf8("actionNew"))
		self.actionEdit_PubKeys = QtGui.QAction(ThinClient)
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/document-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionEdit_PubKeys.setIcon(icon6)
		self.actionEdit_PubKeys.setObjectName(_fromUtf8("actionEdit_PubKeys"))
		self.menuFile.addAction(self.actionNew)
		self.menuFile.addAction(self.actionOpen)
		self.menuFile.addAction(self.actionSave)
		self.menuFile.addAction(self.actionSave_as)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionQuit)
		self.menuEdit.addAction(self.actionEdit_PubKeys)
		self.menuBar.addAction(self.menuFile.menuAction())
		self.menuBar.addAction(self.menuView.menuAction())
		self.menuBar.addAction(self.menuEdit.menuAction())
		self.toolBar.addAction(self.actionNew)
		self.toolBar.addAction(self.actionOpen)
		self.toolBar.addAction(self.actionSave)
		self.toolBar.addAction(self.actionSave_as)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionEdit_PubKeys)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionQuit)
		self.toolBar.addSeparator()

		self.retranslateUi(ThinClient)
		QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), ThinClient.activateTab)
		QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), ThinClient.close)
		QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("activated()")), ThinClient.openConfigFile)
		QtCore.QObject.connect(self.nameEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), ThinClient.configNameChanged)
		QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("activated()")), ThinClient.saveConfigFile)
		QtCore.QObject.connect(self.actionSave_as, QtCore.SIGNAL(_fromUtf8("activated()")), ThinClient.saveAsConfigFile)
		QtCore.QObject.connect(self.actionEdit_PubKeys, QtCore.SIGNAL(_fromUtf8("activated()")), ThinClient.editKeys)
		QtCore.QObject.connect(self.actionNew, QtCore.SIGNAL(_fromUtf8("activated()")), ThinClient.newConfigFile)
		QtCore.QMetaObject.connectSlotsByName(ThinClient)

	def retranslateUi(self, ThinClient):
		ThinClient.setWindowTitle(QtGui.QApplication.translate("ThinClient", "LTMT", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("ThinClient", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans [unknown]\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Librix Thin Client Management Tool. Alpha release.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.nameEdit.setToolTip(QtGui.QApplication.translate("ThinClient", "Enter config name/version here", None, QtGui.QApplication.UnicodeUTF8))
		self.menuFile.setTitle(QtGui.QApplication.translate("ThinClient", "File", None, QtGui.QApplication.UnicodeUTF8))
		self.menuView.setTitle(QtGui.QApplication.translate("ThinClient", "View", None, QtGui.QApplication.UnicodeUTF8))
		self.menuEdit.setTitle(QtGui.QApplication.translate("ThinClient", "Edit", None, QtGui.QApplication.UnicodeUTF8))
		self.toolBar.setWindowTitle(QtGui.QApplication.translate("ThinClient", "Main Tool Bar", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpen.setText(QtGui.QApplication.translate("ThinClient", "Open", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpen.setToolTip(QtGui.QApplication.translate("ThinClient", "Open config file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpen.setStatusTip(QtGui.QApplication.translate("ThinClient", "Open config file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpen.setWhatsThis(QtGui.QApplication.translate("ThinClient", "Open config file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpen.setShortcut(QtGui.QApplication.translate("ThinClient", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setText(QtGui.QApplication.translate("ThinClient", "Save", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setToolTip(QtGui.QApplication.translate("ThinClient", "Save current file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setStatusTip(QtGui.QApplication.translate("ThinClient", "Save current file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setWhatsThis(QtGui.QApplication.translate("ThinClient", "Save current file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setShortcut(QtGui.QApplication.translate("ThinClient", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave_as.setText(QtGui.QApplication.translate("ThinClient", "Save as", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave_as.setIconText(QtGui.QApplication.translate("ThinClient", "Save as", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave_as.setToolTip(QtGui.QApplication.translate("ThinClient", "Save current file as another file name", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave_as.setStatusTip(QtGui.QApplication.translate("ThinClient", "Save current file as another file name", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave_as.setWhatsThis(QtGui.QApplication.translate("ThinClient", "Save current file as another file name", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave_as.setShortcut(QtGui.QApplication.translate("ThinClient", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setText(QtGui.QApplication.translate("ThinClient", "Quit", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setToolTip(QtGui.QApplication.translate("ThinClient", "Quit Librix Thin Client", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setStatusTip(QtGui.QApplication.translate("ThinClient", "Quit Librix Thin Client", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setWhatsThis(QtGui.QApplication.translate("ThinClient", "Quit Librix Thin Client", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setShortcut(QtGui.QApplication.translate("ThinClient", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
		self.actionShow_users_profile_summary.setText(QtGui.QApplication.translate("ThinClient", "Show users profile summary", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNew.setText(QtGui.QApplication.translate("ThinClient", "New", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNew.setToolTip(QtGui.QApplication.translate("ThinClient", "Creates a new empty config file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNew.setStatusTip(QtGui.QApplication.translate("ThinClient", "Creates a new empty config file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNew.setWhatsThis(QtGui.QApplication.translate("ThinClient", "Creates a new empty config file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNew.setShortcut(QtGui.QApplication.translate("ThinClient", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
		self.actionEdit_PubKeys.setText(QtGui.QApplication.translate("ThinClient", "Edit PubKeys", None, QtGui.QApplication.UnicodeUTF8))
		self.actionEdit_PubKeys.setShortcut(QtGui.QApplication.translate("ThinClient", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ThinClient = QtGui.QMainWindow()
	ui = Ui_ThinClient()
	ui.setupUi(ThinClient)
	ThinClient.show()
	sys.exit(app.exec_())

