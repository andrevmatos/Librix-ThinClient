# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/editkeys/editKeys.ui'
#
# Created: Fri Mar 11 14:33:13 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_EditKeys(object):
	def setupUi(self, EditKeys):
		EditKeys.setObjectName(_fromUtf8("EditKeys"))
		EditKeys.resize(678, 266)
		EditKeys.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(EditKeys)
		self.verticalLayout.setSpacing(4)
		self.verticalLayout.setMargin(4)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(EditKeys)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.mainWidget = QtGui.QWidget(EditKeys)
		self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.mainWidget)
		self.horizontalLayout.setSpacing(4)
		self.horizontalLayout.setMargin(4)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.keysList = QtGui.QListWidget(self.mainWidget)
		self.keysList.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
		self.keysList.setAlternatingRowColors(True)
		self.keysList.setObjectName(_fromUtf8("keysList"))
		self.horizontalLayout.addWidget(self.keysList)
		self.toolBar = QtGui.QWidget(self.mainWidget)
		self.toolBar.setObjectName(_fromUtf8("toolBar"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.toolBar)
		self.verticalLayout_2.setSpacing(2)
		self.verticalLayout_2.setMargin(2)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.openButton = QtGui.QToolButton(self.toolBar)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.openButton.setIcon(icon)
		self.openButton.setIconSize(QtCore.QSize(22, 22))
		self.openButton.setAutoRaise(True)
		self.openButton.setObjectName(_fromUtf8("openButton"))
		self.verticalLayout_2.addWidget(self.openButton)
		self.addButton = QtGui.QToolButton(self.toolBar)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/add_icon/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.addButton.setIcon(icon1)
		self.addButton.setIconSize(QtCore.QSize(22, 22))
		self.addButton.setAutoRaise(True)
		self.addButton.setObjectName(_fromUtf8("addButton"))
		self.verticalLayout_2.addWidget(self.addButton)
		self.delButton = QtGui.QToolButton(self.toolBar)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/remove_icon/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.delButton.setIcon(icon2)
		self.delButton.setIconSize(QtCore.QSize(22, 22))
		self.delButton.setAutoRaise(True)
		self.delButton.setObjectName(_fromUtf8("delButton"))
		self.verticalLayout_2.addWidget(self.delButton)
		spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.horizontalLayout.addWidget(self.toolBar)
		self.verticalLayout.addWidget(self.mainWidget)
		self.buttonBox = QtGui.QDialogButtonBox(EditKeys)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(EditKeys)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditKeys.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditKeys.reject)
		QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EditKeys.addKey)
		QtCore.QObject.connect(self.delButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EditKeys.delKey)
		QtCore.QObject.connect(self.openButton, QtCore.SIGNAL(_fromUtf8("clicked()")), EditKeys.openKey)
		QtCore.QMetaObject.connectSlotsByName(EditKeys)

	def retranslateUi(self, EditKeys):
		EditKeys.setWindowTitle(QtGui.QApplication.translate("EditKeys", "Edit PubKeys", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("EditKeys", "Super User SSH Public Keys:", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setToolTip(QtGui.QApplication.translate("EditKeys", "Add PubKey from File", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setStatusTip(QtGui.QApplication.translate("EditKeys", "Add PubKey from File", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setWhatsThis(QtGui.QApplication.translate("EditKeys", "Add PubKey from File", None, QtGui.QApplication.UnicodeUTF8))
		self.openButton.setText(QtGui.QApplication.translate("EditKeys", "Add PubKey from File", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setToolTip(QtGui.QApplication.translate("EditKeys", "Add PubKey", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setStatusTip(QtGui.QApplication.translate("EditKeys", "Add PubKey", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setWhatsThis(QtGui.QApplication.translate("EditKeys", "Add PubKey", None, QtGui.QApplication.UnicodeUTF8))
		self.addButton.setText(QtGui.QApplication.translate("EditKeys", "Add PubKey", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setToolTip(QtGui.QApplication.translate("EditKeys", "Remove PubKey", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setStatusTip(QtGui.QApplication.translate("EditKeys", "Remove PubKey", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setWhatsThis(QtGui.QApplication.translate("EditKeys", "Remove PubKey", None, QtGui.QApplication.UnicodeUTF8))
		self.delButton.setText(QtGui.QApplication.translate("EditKeys", "Remove PubKey", None, QtGui.QApplication.UnicodeUTF8))

from ltmt.ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	EditKeys = QtGui.QDialog()
	ui = Ui_EditKeys()
	ui.setupUi(EditKeys)
	EditKeys.show()
	sys.exit(app.exec_())

