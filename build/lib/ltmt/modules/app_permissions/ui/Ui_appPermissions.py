# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/modules/app_permissions/ui/appPermissions.ui'
#
# Created: Mon Mar 21 19:42:34 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_AppPermissions(object):
	def setupUi(self, AppPermissions):
		AppPermissions.setObjectName(_fromUtf8("AppPermissions"))
		AppPermissions.resize(640, 480)
		self.verticalLayout = QtGui.QVBoxLayout(AppPermissions)
		self.verticalLayout.setSpacing(4)
		self.verticalLayout.setMargin(4)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.mainWidget = QtGui.QWidget(AppPermissions)
		self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.mainWidget)
		self.verticalLayout_2.setSpacing(4)
		self.verticalLayout_2.setMargin(4)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.optionsLabel = QtGui.QLabel(self.mainWidget)
		self.optionsLabel.setObjectName(_fromUtf8("optionsLabel"))
		self.verticalLayout_2.addWidget(self.optionsLabel)
		self.policyWidget = QtGui.QWidget(self.mainWidget)
		self.policyWidget.setObjectName(_fromUtf8("policyWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.policyWidget)
		self.horizontalLayout.setSpacing(4)
		self.horizontalLayout.setMargin(4)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.allowRadio = QtGui.QRadioButton(self.policyWidget)
		self.allowRadio.setChecked(True)
		self.allowRadio.setObjectName(_fromUtf8("allowRadio"))
		self.horizontalLayout.addWidget(self.allowRadio)
		self.denyRadio = QtGui.QRadioButton(self.policyWidget)
		self.denyRadio.setChecked(False)
		self.denyRadio.setObjectName(_fromUtf8("denyRadio"))
		self.horizontalLayout.addWidget(self.denyRadio)
		self.verticalLayout_2.addWidget(self.policyWidget)
		self.listsWidget = QtGui.QWidget(self.mainWidget)
		self.listsWidget.setObjectName(_fromUtf8("listsWidget"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.listsWidget)
		self.horizontalLayout_2.setSpacing(4)
		self.horizontalLayout_2.setMargin(4)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.allListWid = QtGui.QWidget(self.listsWidget)
		self.allListWid.setObjectName(_fromUtf8("allListWid"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.allListWid)
		self.verticalLayout_3.setSpacing(4)
		self.verticalLayout_3.setMargin(4)
		self.verticalLayout_3.setMargin(0)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.allSearchWid = QtGui.QWidget(self.allListWid)
		self.allSearchWid.setObjectName(_fromUtf8("allSearchWid"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.allSearchWid)
		self.horizontalLayout_3.setSpacing(0)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.allSearchLine = QtGui.QLineEdit(self.allSearchWid)
		self.allSearchLine.setObjectName(_fromUtf8("allSearchLine"))
		self.horizontalLayout_3.addWidget(self.allSearchLine)
		self.allSearchClearButton = QtGui.QToolButton(self.allSearchWid)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/clear-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.allSearchClearButton.setIcon(icon)
		self.allSearchClearButton.setAutoRaise(True)
		self.allSearchClearButton.setObjectName(_fromUtf8("allSearchClearButton"))
		self.horizontalLayout_3.addWidget(self.allSearchClearButton)
		self.verticalLayout_3.addWidget(self.allSearchWid)
		self.allLabel = QtGui.QLabel(self.allListWid)
		self.allLabel.setObjectName(_fromUtf8("allLabel"))
		self.verticalLayout_3.addWidget(self.allLabel)
		self.allAppsList = QtGui.QListWidget(self.allListWid)
		self.allAppsList.setDragEnabled(True)
		self.allAppsList.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
		self.allAppsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.allAppsList.setObjectName(_fromUtf8("allAppsList"))
		self.verticalLayout_3.addWidget(self.allAppsList)
		self.horizontalLayout_2.addWidget(self.allListWid)
		self.actionsWid = QtGui.QWidget(self.listsWidget)
		self.actionsWid.setObjectName(_fromUtf8("actionsWid"))
		self.verticalLayout_5 = QtGui.QVBoxLayout(self.actionsWid)
		self.verticalLayout_5.setSpacing(4)
		self.verticalLayout_5.setMargin(4)
		self.verticalLayout_5.setMargin(0)
		self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
		spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_5.addItem(spacerItem)
		self.addButton = QtGui.QToolButton(self.actionsWid)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/arrow-right-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.addButton.setIcon(icon1)
		self.addButton.setIconSize(QtCore.QSize(22, 22))
		self.addButton.setObjectName(_fromUtf8("addButton"))
		self.verticalLayout_5.addWidget(self.addButton)
		self.delButton = QtGui.QToolButton(self.actionsWid)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/arrow-left-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.delButton.setIcon(icon2)
		self.delButton.setIconSize(QtCore.QSize(22, 22))
		self.delButton.setObjectName(_fromUtf8("delButton"))
		self.verticalLayout_5.addWidget(self.delButton)
		spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_5.addItem(spacerItem1)
		self.horizontalLayout_2.addWidget(self.actionsWid)
		self.selectedWid = QtGui.QWidget(self.listsWidget)
		self.selectedWid.setObjectName(_fromUtf8("selectedWid"))
		self.verticalLayout_4 = QtGui.QVBoxLayout(self.selectedWid)
		self.verticalLayout_4.setSpacing(4)
		self.verticalLayout_4.setMargin(4)
		self.verticalLayout_4.setMargin(0)
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.selectedSearchWid = QtGui.QWidget(self.selectedWid)
		self.selectedSearchWid.setObjectName(_fromUtf8("selectedSearchWid"))
		self.horizontalLayout_4 = QtGui.QHBoxLayout(self.selectedSearchWid)
		self.horizontalLayout_4.setSpacing(0)
		self.horizontalLayout_4.setMargin(0)
		self.horizontalLayout_4.setMargin(0)
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.selectedSearchLine = QtGui.QLineEdit(self.selectedSearchWid)
		self.selectedSearchLine.setObjectName(_fromUtf8("selectedSearchLine"))
		self.horizontalLayout_4.addWidget(self.selectedSearchLine)
		self.selectedSearchClearButton = QtGui.QToolButton(self.selectedSearchWid)
		self.selectedSearchClearButton.setIcon(icon)
		self.selectedSearchClearButton.setAutoRaise(True)
		self.selectedSearchClearButton.setObjectName(_fromUtf8("selectedSearchClearButton"))
		self.horizontalLayout_4.addWidget(self.selectedSearchClearButton)
		self.verticalLayout_4.addWidget(self.selectedSearchWid)
		self.selectedLabel = QtGui.QLabel(self.selectedWid)
		self.selectedLabel.setObjectName(_fromUtf8("selectedLabel"))
		self.verticalLayout_4.addWidget(self.selectedLabel)
		self.selectedAppsList = QtGui.QListWidget(self.selectedWid)
		self.selectedAppsList.setDragEnabled(True)
		self.selectedAppsList.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
		self.selectedAppsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.selectedAppsList.setObjectName(_fromUtf8("selectedAppsList"))
		self.verticalLayout_4.addWidget(self.selectedAppsList)
		self.horizontalLayout_2.addWidget(self.selectedWid)
		self.verticalLayout_2.addWidget(self.listsWidget)
		self.verticalLayout.addWidget(self.mainWidget)
		self.buttonBox = QtGui.QDialogButtonBox(AppPermissions)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(AppPermissions)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AppPermissions.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AppPermissions.reject)
		QtCore.QObject.connect(self.allSearchClearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.allSearchLine.clear)
		QtCore.QObject.connect(self.selectedSearchClearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectedSearchLine.clear)
		QtCore.QObject.connect(self.allSearchLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AppPermissions.allSearch)
		QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AppPermissions.addSelected)
		QtCore.QObject.connect(self.delButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AppPermissions.removeSelected)
		QtCore.QObject.connect(self.selectedSearchLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AppPermissions.selectedSearch)
		QtCore.QObject.connect(self.allowRadio, QtCore.SIGNAL(_fromUtf8("clicked()")), AppPermissions.setPolicy)
		QtCore.QObject.connect(self.denyRadio, QtCore.SIGNAL(_fromUtf8("clicked()")), AppPermissions.setPolicy)
		QtCore.QMetaObject.connectSlotsByName(AppPermissions)

	def retranslateUi(self, AppPermissions):
		AppPermissions.setWindowTitle(QtGui.QApplication.translate("AppPermissions", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.optionsLabel.setText(QtGui.QApplication.translate("AppPermissions", "Default Policy:", None, QtGui.QApplication.UnicodeUTF8))
		self.allowRadio.setText(QtGui.QApplication.translate("AppPermissions", "Allow All", None, QtGui.QApplication.UnicodeUTF8))
		self.denyRadio.setText(QtGui.QApplication.translate("AppPermissions", "Deny All", None, QtGui.QApplication.UnicodeUTF8))
		self.allSearchClearButton.setToolTip(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.allSearchClearButton.setStatusTip(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.allSearchClearButton.setWhatsThis(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.allSearchClearButton.setText(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.allLabel.setText(QtGui.QApplication.translate("AppPermissions", "All Applications", None, QtGui.QApplication.UnicodeUTF8))
		self.allAppsList.setSortingEnabled(True)
		self.addButton.setText(QtGui.QApplication.translate("AppPermissions", "Add Application", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setText(QtGui.QApplication.translate("AppPermissions", "Remove Application", None, QtGui.QApplication.UnicodeUTF8))
		self.selectedSearchClearButton.setToolTip(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.selectedSearchClearButton.setStatusTip(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.selectedSearchClearButton.setWhatsThis(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.selectedSearchClearButton.setText(QtGui.QApplication.translate("AppPermissions", "Clear Search", None, QtGui.QApplication.UnicodeUTF8))
		self.selectedLabel.setText(QtGui.QApplication.translate("AppPermissions", "Exceptions:", None, QtGui.QApplication.UnicodeUTF8))
		self.selectedAppsList.setSortingEnabled(True)

from ltmt.modules.app_permissions.ui.icons import app_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	AppPermissions = QtGui.QDialog()
	ui = Ui_AppPermissions()
	ui.setupUi(AppPermissions)
	AppPermissions.show()
	sys.exit(app.exec_())

