# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './modules/autostart/ui/autoExecConfig.ui'
#
# Created: Tue Mar  1 13:53:41 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_AutoExecConfig(object):
	def setupUi(self, AutoExecConfig):
		AutoExecConfig.setObjectName(_fromUtf8("AutoExecConfig"))
		AutoExecConfig.setWindowModality(QtCore.Qt.WindowModal)
		AutoExecConfig.resize(640, 360)
		AutoExecConfig.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(AutoExecConfig)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(AutoExecConfig)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.mainWid = QtGui.QWidget(AutoExecConfig)
		self.mainWid.setObjectName(_fromUtf8("mainWid"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.mainWid)
		self.horizontalLayout.setMargin(2)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.listWidget = QtGui.QListWidget(self.mainWid)
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		self.horizontalLayout.addWidget(self.listWidget)
		self.toolbarWid = QtGui.QWidget(self.mainWid)
		self.toolbarWid.setObjectName(_fromUtf8("toolbarWid"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.toolbarWid)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.editButton = QtGui.QToolButton(self.toolbarWid)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/document-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.editButton.setIcon(icon)
		self.editButton.setIconSize(QtCore.QSize(24, 24))
		self.editButton.setAutoRaise(True)
		self.editButton.setObjectName(_fromUtf8("editButton"))
		self.verticalLayout_2.addWidget(self.editButton)
		self.openButton = QtGui.QToolButton(self.toolbarWid)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.openButton.setIcon(icon1)
		self.openButton.setIconSize(QtCore.QSize(24, 24))
		self.openButton.setAutoRaise(True)
		self.openButton.setObjectName(_fromUtf8("openButton"))
		self.verticalLayout_2.addWidget(self.openButton)
		self.addButton = QtGui.QToolButton(self.toolbarWid)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.addButton.setIcon(icon2)
		self.addButton.setIconSize(QtCore.QSize(24, 24))
		self.addButton.setAutoRaise(True)
		self.addButton.setObjectName(_fromUtf8("addButton"))
		self.verticalLayout_2.addWidget(self.addButton)
		self.removeButton = QtGui.QToolButton(self.toolbarWid)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.removeButton.setIcon(icon3)
		self.removeButton.setIconSize(QtCore.QSize(24, 24))
		self.removeButton.setAutoRaise(True)
		self.removeButton.setObjectName(_fromUtf8("removeButton"))
		self.verticalLayout_2.addWidget(self.removeButton)
		spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.horizontalLayout.addWidget(self.toolbarWid)
		self.verticalLayout.addWidget(self.mainWid)
		self.buttonBox = QtGui.QDialogButtonBox(AutoExecConfig)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(AutoExecConfig)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AutoExecConfig.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AutoExecConfig.reject)
		QtCore.QObject.connect(self.editButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AutoExecConfig.editCommand)
		QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AutoExecConfig.newCommand)
		QtCore.QObject.connect(self.removeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AutoExecConfig.delCommand)
		QtCore.QMetaObject.connectSlotsByName(AutoExecConfig)

	def retranslateUi(self, AutoExecConfig):
		AutoExecConfig.setWindowTitle(QtGui.QApplication.translate("AutoExecConfig", "AutoStart Configuration", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("AutoExecConfig", "Commands List:", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setToolTip(QtGui.QApplication.translate("AutoExecConfig", "Edit Command", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setStatusTip(QtGui.QApplication.translate("AutoExecConfig", "Edit Command", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setWhatsThis(QtGui.QApplication.translate("AutoExecConfig", "Edit Command", None, QtGui.QApplication.UnicodeUTF8))
		self.editButton.setText(QtGui.QApplication.translate("AutoExecConfig", "Edit Command", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setToolTip(QtGui.QApplication.translate("AutoExecConfig", "Import from a Menu Item", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setStatusTip(QtGui.QApplication.translate("AutoExecConfig", "Import from a Menu Item", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setWhatsThis(QtGui.QApplication.translate("AutoExecConfig", "Import from a Menu Item", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setText(QtGui.QApplication.translate("AutoExecConfig", "Import from a Menu Item", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setToolTip(QtGui.QApplication.translate("AutoExecConfig", "Add Command", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setStatusTip(QtGui.QApplication.translate("AutoExecConfig", "Add Command", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setWhatsThis(QtGui.QApplication.translate("AutoExecConfig", "Add Command", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("AutoExecConfig", "Add Command", None, QtGui.QApplication.UnicodeUTF8))
		self.removeButton.setToolTip(QtGui.QApplication.translate("AutoExecConfig", "Delete Command", None, QtGui.QApplication.UnicodeUTF8))
		self.removeButton.setStatusTip(QtGui.QApplication.translate("AutoExecConfig", "Delete Command", None, QtGui.QApplication.UnicodeUTF8))
		self.removeButton.setWhatsThis(QtGui.QApplication.translate("AutoExecConfig", "Delete Command", None, QtGui.QApplication.UnicodeUTF8))
		self.removeButton.setText(QtGui.QApplication.translate("AutoExecConfig", "Delete Command", None, QtGui.QApplication.UnicodeUTF8))

from modules.autostart.ui.icons import autostart_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	AutoExecConfig = QtGui.QDialog()
	ui = Ui_AutoExecConfig()
	ui.setupUi(AutoExecConfig)
	AutoExecConfig.show()
	sys.exit(app.exec_())

