# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/export/exportWidget.ui'
#
# Created: Fri Mar 11 14:27:43 2011
#      by: PyQt4 UI code generator 4.8.3
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
		self.mainVLayout.setSpacing(4)
		self.mainVLayout.setMargin(4)
		self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
		self.targetsBox = QtGui.QGroupBox(ExportWidget)
		self.targetsBox.setObjectName(_fromUtf8("targetsBox"))
		self.verticalLayout = QtGui.QVBoxLayout(self.targetsBox)
		self.verticalLayout.setSpacing(4)
		self.verticalLayout.setMargin(4)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.IPsWidget = QtGui.QWidget(self.targetsBox)
		self.IPsWidget.setObjectName(_fromUtf8("IPsWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.IPsWidget)
		self.horizontalLayout.setSpacing(4)
		self.horizontalLayout.setMargin(4)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.treeWidget = QtGui.QTreeWidget(self.IPsWidget)
		self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.treeWidget.setAnimated(True)
		self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
		self.treeWidget.header().setCascadingSectionResizes(True)
		self.treeWidget.header().setDefaultSectionSize(200)
		self.treeWidget.header().setMinimumSectionSize(250)
		self.treeWidget.header().setSortIndicatorShown(True)
		self.horizontalLayout.addWidget(self.treeWidget)
		self.targetsToolBar = QtGui.QWidget(self.IPsWidget)
		self.targetsToolBar.setMinimumSize(QtCore.QSize(40, 0))
		self.targetsToolBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.targetsToolBar.setObjectName(_fromUtf8("targetsToolBar"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.targetsToolBar)
		self.verticalLayout_2.setSpacing(4)
		self.verticalLayout_2.setMargin(4)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.addButton = QtGui.QToolButton(self.targetsToolBar)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/add_icon/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.addButton.setIcon(icon)
		self.addButton.setIconSize(QtCore.QSize(24, 24))
		self.addButton.setAutoRaise(True)
		self.addButton.setObjectName(_fromUtf8("addButton"))
		self.verticalLayout_2.addWidget(self.addButton)
		self.delButton = QtGui.QToolButton(self.targetsToolBar)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/remove_icon/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.delButton.setIcon(icon1)
		self.delButton.setIconSize(QtCore.QSize(24, 24))
		self.delButton.setAutoRaise(True)
		self.delButton.setObjectName(_fromUtf8("delButton"))
		self.verticalLayout_2.addWidget(self.delButton)
		self.line = QtGui.QFrame(self.targetsToolBar)
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName(_fromUtf8("line"))
		self.verticalLayout_2.addWidget(self.line)
		self.rescanButton = QtGui.QToolButton(self.targetsToolBar)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/tab/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.rescanButton.setIcon(icon2)
		self.rescanButton.setIconSize(QtCore.QSize(22, 22))
		self.rescanButton.setAutoRaise(True)
		self.rescanButton.setObjectName(_fromUtf8("rescanButton"))
		self.verticalLayout_2.addWidget(self.rescanButton)
		spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.horizontalLayout.addWidget(self.targetsToolBar)
		self.verticalLayout.addWidget(self.IPsWidget)
		self.mainVLayout.addWidget(self.targetsBox)
		self.privKeyBox = QtGui.QGroupBox(ExportWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.privKeyBox.sizePolicy().hasHeightForWidth())
		self.privKeyBox.setSizePolicy(sizePolicy)
		self.privKeyBox.setMinimumSize(QtCore.QSize(0, 100))
		self.privKeyBox.setMaximumSize(QtCore.QSize(16777215, 100))
		self.privKeyBox.setObjectName(_fromUtf8("privKeyBox"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.privKeyBox)
		self.horizontalLayout_2.setSpacing(4)
		self.horizontalLayout_2.setMargin(4)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.privKeyLabel = QtGui.QLabel(self.privKeyBox)
		self.privKeyLabel.setObjectName(_fromUtf8("privKeyLabel"))
		self.horizontalLayout_2.addWidget(self.privKeyLabel)
		self.privKeyPath = QtGui.QLineEdit(self.privKeyBox)
		self.privKeyPath.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.privKeyPath.setObjectName(_fromUtf8("privKeyPath"))
		self.horizontalLayout_2.addWidget(self.privKeyPath)
		self.openButton = QtGui.QToolButton(self.privKeyBox)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.openButton.setIcon(icon3)
		self.openButton.setIconSize(QtCore.QSize(24, 24))
		self.openButton.setAutoRaise(True)
		self.openButton.setObjectName(_fromUtf8("openButton"))
		self.horizontalLayout_2.addWidget(self.openButton)
		self.mainVLayout.addWidget(self.privKeyBox)
		self.buttonBox = QtGui.QDialogButtonBox(ExportWidget)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.mainVLayout.addWidget(self.buttonBox)

		self.retranslateUi(ExportWidget)
		QtCore.QObject.connect(self.privKeyPath, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), ExportWidget.checkPrivKeyFile)
		QtCore.QObject.connect(self.openButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportWidget.browsePrivKeyFile)
		QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportWidget.addTargetsClicked)
		QtCore.QObject.connect(self.delButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportWidget.removeTargetsClicked)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), ExportWidget.buttonBoxClicked)
		QtCore.QObject.connect(self.rescanButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportWidget.rescan)
		QtCore.QMetaObject.connectSlotsByName(ExportWidget)

	def retranslateUi(self, ExportWidget):
		ExportWidget.setWindowTitle(QtGui.QApplication.translate("ExportWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.targetsBox.setTitle(QtGui.QApplication.translate("ExportWidget", "Targets", None, QtGui.QApplication.UnicodeUTF8))
		self.treeWidget.setSortingEnabled(True)
		self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("ExportWidget", "Address", None, QtGui.QApplication.UnicodeUTF8))
		self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("ExportWidget", "Version", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setToolTip(QtGui.QApplication.translate("ExportWidget", "Add Targets Manually", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("ExportWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setToolTip(QtGui.QApplication.translate("ExportWidget", "Remove Selected Targets", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setText(QtGui.QApplication.translate("ExportWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.rescanButton.setText(QtGui.QApplication.translate("ExportWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.privKeyBox.setTitle(QtGui.QApplication.translate("ExportWidget", "Admin SSH Private Key", None, QtGui.QApplication.UnicodeUTF8))
		self.privKeyLabel.setText(QtGui.QApplication.translate("ExportWidget", "SSH Private Key:", None, QtGui.QApplication.UnicodeUTF8))
		self.privKeyPath.setText(QtGui.QApplication.translate("ExportWidget", "/root/.ssh/id_rsa", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setText(QtGui.QApplication.translate("ExportWidget", "...", None, QtGui.QApplication.UnicodeUTF8))

from ltmt.ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ExportWidget = QtGui.QWidget()
	ui = Ui_ExportWidget()
	ui.setupUi(ExportWidget)
	ExportWidget.show()
	sys.exit(app.exec_())

