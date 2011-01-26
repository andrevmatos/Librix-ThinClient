# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/export/exportWidget.ui'
#
# Created: Wed Jan 26 01:10:58 2011
#      by: PyQt4 UI code generator 4.8.2
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
		self.targetsBox = QtGui.QGroupBox(ExportWidget)
		self.targetsBox.setObjectName(_fromUtf8("targetsBox"))
		self.verticalLayout = QtGui.QVBoxLayout(self.targetsBox)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.IPsWidget = QtGui.QWidget(self.targetsBox)
		self.IPsWidget.setObjectName(_fromUtf8("IPsWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.IPsWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.treeWidget = QtGui.QTreeWidget(self.IPsWidget)
		self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.treeWidget.setAnimated(True)
		self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
		self.treeWidget.header().setCascadingSectionResizes(True)
		self.treeWidget.header().setDefaultSectionSize(400)
		self.treeWidget.header().setSortIndicatorShown(True)
		self.horizontalLayout.addWidget(self.treeWidget)
		self.targetsToolBar = QtGui.QWidget(self.IPsWidget)
		self.targetsToolBar.setMinimumSize(QtCore.QSize(40, 0))
		self.targetsToolBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.targetsToolBar.setObjectName(_fromUtf8("targetsToolBar"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.targetsToolBar)
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
		self.toolButton = QtGui.QToolButton(self.targetsToolBar)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/remove_icon/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toolButton.setIcon(icon1)
		self.toolButton.setIconSize(QtCore.QSize(24, 24))
		self.toolButton.setAutoRaise(True)
		self.toolButton.setObjectName(_fromUtf8("toolButton"))
		self.verticalLayout_2.addWidget(self.toolButton)
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
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.privKeyLabel = QtGui.QLabel(self.privKeyBox)
		self.privKeyLabel.setObjectName(_fromUtf8("privKeyLabel"))
		self.horizontalLayout_2.addWidget(self.privKeyLabel)
		self.privKeyPath = QtGui.QLineEdit(self.privKeyBox)
		self.privKeyPath.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.privKeyPath.setObjectName(_fromUtf8("privKeyPath"))
		self.horizontalLayout_2.addWidget(self.privKeyPath)
		self.openButton = QtGui.QToolButton(self.privKeyBox)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.openButton.setIcon(icon2)
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
		QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportWidget.removeTargetsClicked)
		QtCore.QMetaObject.connectSlotsByName(ExportWidget)

	def retranslateUi(self, ExportWidget):
		ExportWidget.setWindowTitle(QtGui.QApplication.translate("ExportWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.targetsBox.setTitle(QtGui.QApplication.translate("ExportWidget", "Targets", None, QtGui.QApplication.UnicodeUTF8))
		self.treeWidget.setSortingEnabled(True)
		self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("ExportWidget", "Address", None, QtGui.QApplication.UnicodeUTF8))
		self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("ExportWidget", "Version", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setToolTip(QtGui.QApplication.translate("ExportWidget", "Add Targets Manually", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("ExportWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton.setToolTip(QtGui.QApplication.translate("ExportWidget", "Remove Selected Targets", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton.setText(QtGui.QApplication.translate("ExportWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.privKeyBox.setTitle(QtGui.QApplication.translate("ExportWidget", "Admin SSH Private Key", None, QtGui.QApplication.UnicodeUTF8))
		self.privKeyLabel.setText(QtGui.QApplication.translate("ExportWidget", "SSH Private Key:", None, QtGui.QApplication.UnicodeUTF8))
		self.privKeyPath.setText(QtGui.QApplication.translate("ExportWidget", "/root/.ssh/id_rsa", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setText(QtGui.QApplication.translate("ExportWidget", "...", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ExportWidget = QtGui.QWidget()
	ui = Ui_ExportWidget()
	ui.setupUi(ExportWidget)
	ExportWidget.show()
	sys.exit(app.exec_())

