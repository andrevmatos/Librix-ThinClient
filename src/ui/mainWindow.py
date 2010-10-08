# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Oct  8 16:27:18 2010
#      by: PyQt4 UI code generator 4.7.7
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
		ThinClient.resize(640, 480)
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
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.label = QtGui.QLabel(self.topBar)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout_4.addWidget(self.label)
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
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.horizontalLayout_3.addWidget(self.options)
		self.verticalLayout.addWidget(self.main)
		ThinClient.setCentralWidget(self.widget)
		self.statusbar = QtGui.QStatusBar(ThinClient)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		ThinClient.setStatusBar(self.statusbar)

		self.retranslateUi(ThinClient)
		QtCore.QMetaObject.connectSlotsByName(ThinClient)

	def retranslateUi(self, ThinClient):
		ThinClient.setWindowTitle(QtGui.QApplication.translate("ThinClient", "Librix Thin Client Administration Interface", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("ThinClient", "<b>Librix Thin Client Administration Tool. Draft release.</b>", None, QtGui.QApplication.UnicodeUTF8))

from . import temp_icons_rc
