# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/keygen/keyGen.ui'
#
# Created: Mon Mar 21 19:51:01 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_KeyGen(object):
	def setupUi(self, KeyGen):
		KeyGen.setObjectName(_fromUtf8("KeyGen"))
		KeyGen.setWindowModality(QtCore.Qt.WindowModal)
		KeyGen.resize(520, 419)
		KeyGen.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(KeyGen)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(KeyGen)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.logText = QtGui.QTextEdit(KeyGen)
		self.logText.setReadOnly(True)
		self.logText.setObjectName(_fromUtf8("logText"))
		self.verticalLayout.addWidget(self.logText)
		self.widget = QtGui.QWidget(KeyGen)
		self.widget.setObjectName(_fromUtf8("widget"))
		self.gridLayout = QtGui.QGridLayout(self.widget)
		self.gridLayout.setMargin(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.savePrivKey = QtGui.QPushButton(self.widget)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.savePrivKey.setIcon(icon)
		self.savePrivKey.setObjectName(_fromUtf8("savePrivKey"))
		self.gridLayout.addWidget(self.savePrivKey, 0, 0, 1, 1)
		self.savePubKey = QtGui.QPushButton(self.widget)
		self.savePubKey.setIcon(icon)
		self.savePubKey.setObjectName(_fromUtf8("savePubKey"))
		self.gridLayout.addWidget(self.savePubKey, 1, 0, 1, 1)
		self.openPrivKeyFile = QtGui.QPushButton(self.widget)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/export_icon/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.openPrivKeyFile.setIcon(icon1)
		self.openPrivKeyFile.setObjectName(_fromUtf8("openPrivKeyFile"))
		self.gridLayout.addWidget(self.openPrivKeyFile, 0, 1, 1, 1)
		self.openPubKeyFile = QtGui.QPushButton(self.widget)
		self.openPubKeyFile.setIcon(icon1)
		self.openPubKeyFile.setObjectName(_fromUtf8("openPubKeyFile"))
		self.gridLayout.addWidget(self.openPubKeyFile, 1, 1, 1, 1)
		self.verticalLayout.addWidget(self.widget)
		self.close = QtGui.QPushButton(KeyGen)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.close.setIcon(icon2)
		self.close.setObjectName(_fromUtf8("close"))
		self.verticalLayout.addWidget(self.close)

		self.retranslateUi(KeyGen)
		QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), KeyGen.reject)
		QtCore.QObject.connect(self.savePrivKey, QtCore.SIGNAL(_fromUtf8("clicked()")), KeyGen.savePrivKey)
		QtCore.QObject.connect(self.savePubKey, QtCore.SIGNAL(_fromUtf8("clicked()")), KeyGen.savePubKey)
		QtCore.QObject.connect(self.openPrivKeyFile, QtCore.SIGNAL(_fromUtf8("clicked()")), KeyGen.openPrivKey)
		QtCore.QObject.connect(self.openPubKeyFile, QtCore.SIGNAL(_fromUtf8("clicked()")), KeyGen.openPubKey)
		QtCore.QMetaObject.connectSlotsByName(KeyGen)

	def retranslateUi(self, KeyGen):
		KeyGen.setWindowTitle(QtGui.QApplication.translate("KeyGen", "Public/Private SSH Key Generation", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("KeyGen", "Log:", None, QtGui.QApplication.UnicodeUTF8))
		self.savePrivKey.setText(QtGui.QApplication.translate("KeyGen", "Sa&ve Private Key File", None, QtGui.QApplication.UnicodeUTF8))
		self.savePubKey.setText(QtGui.QApplication.translate("KeyGen", "&Save Public Key File", None, QtGui.QApplication.UnicodeUTF8))
		self.openPrivKeyFile.setText(QtGui.QApplication.translate("KeyGen", "O&pen Private Key File", None, QtGui.QApplication.UnicodeUTF8))
		self.openPubKeyFile.setText(QtGui.QApplication.translate("KeyGen", "&Open Public Key File", None, QtGui.QApplication.UnicodeUTF8))
		self.close.setText(QtGui.QApplication.translate("KeyGen", "&Close", None, QtGui.QApplication.UnicodeUTF8))

from ltmt.ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	KeyGen = QtGui.QDialog()
	ui = Ui_KeyGen()
	ui.setupUi(KeyGen)
	KeyGen.show()
	sys.exit(app.exec_())

