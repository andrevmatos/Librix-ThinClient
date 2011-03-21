# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/keygen/openKey.ui'
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

class Ui_OpenKey(object):
	def setupUi(self, OpenKey):
		OpenKey.setObjectName(_fromUtf8("OpenKey"))
		OpenKey.setWindowModality(QtCore.Qt.WindowModal)
		OpenKey.resize(569, 357)
		OpenKey.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(OpenKey)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.textEdit = QtGui.QTextEdit(OpenKey)
		self.textEdit.setReadOnly(True)
		self.textEdit.setObjectName(_fromUtf8("textEdit"))
		self.verticalLayout.addWidget(self.textEdit)
		self.copyButton = QtGui.QPushButton(OpenKey)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/tab/copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.copyButton.setIcon(icon)
		self.copyButton.setObjectName(_fromUtf8("copyButton"))
		self.verticalLayout.addWidget(self.copyButton)
		self.closeButton = QtGui.QPushButton(OpenKey)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.closeButton.setIcon(icon1)
		self.closeButton.setObjectName(_fromUtf8("closeButton"))
		self.verticalLayout.addWidget(self.closeButton)

		self.retranslateUi(OpenKey)
		QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), OpenKey.reject)
		QtCore.QObject.connect(self.copyButton, QtCore.SIGNAL(_fromUtf8("clicked()")), OpenKey.copy)
		QtCore.QMetaObject.connectSlotsByName(OpenKey)

	def retranslateUi(self, OpenKey):
		OpenKey.setWindowTitle(QtGui.QApplication.translate("OpenKey", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.copyButton.setText(QtGui.QApplication.translate("OpenKey", "&Copy to Clipboard", None, QtGui.QApplication.UnicodeUTF8))
		self.closeButton.setText(QtGui.QApplication.translate("OpenKey", "&Close", None, QtGui.QApplication.UnicodeUTF8))

from ltmt.ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	OpenKey = QtGui.QDialog()
	ui = Ui_OpenKey()
	ui.setupUi(OpenKey)
	OpenKey.show()
	sys.exit(app.exec_())

