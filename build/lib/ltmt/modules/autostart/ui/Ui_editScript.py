# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/modules/autostart/ui/editScript.ui'
#
# Created: Fri Mar 11 14:47:20 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_EditScript(object):
	def setupUi(self, EditScript):
		EditScript.setObjectName(_fromUtf8("EditScript"))
		EditScript.setWindowModality(QtCore.Qt.WindowModal)
		EditScript.resize(320, 240)
		EditScript.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(EditScript)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(EditScript)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.textEdit = QtGui.QTextEdit(EditScript)
		self.textEdit.setObjectName(_fromUtf8("textEdit"))
		self.verticalLayout.addWidget(self.textEdit)
		self.buttonBox = QtGui.QDialogButtonBox(EditScript)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(EditScript)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditScript.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditScript.reject)
		QtCore.QMetaObject.connectSlotsByName(EditScript)

	def retranslateUi(self, EditScript):
		EditScript.setWindowTitle(QtGui.QApplication.translate("EditScript", "Edit Script", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("EditScript", "Enter script below:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	EditScript = QtGui.QDialog()
	ui = Ui_EditScript()
	ui.setupUi(EditScript)
	EditScript.show()
	sys.exit(app.exec_())

