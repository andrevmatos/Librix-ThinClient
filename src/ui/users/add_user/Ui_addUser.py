# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/users/add_user/addUser.ui'
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

class Ui_AddUser(object):
	def setupUi(self, AddUser):
		AddUser.setObjectName(_fromUtf8("AddUser"))
		AddUser.setWindowModality(QtCore.Qt.WindowModal)
		AddUser.resize(400, 388)
		AddUser.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(AddUser)
		self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.descLabel = QtGui.QLabel(AddUser)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.descLabel.sizePolicy().hasHeightForWidth())
		self.descLabel.setSizePolicy(sizePolicy)
		self.descLabel.setObjectName(_fromUtf8("descLabel"))
		self.verticalLayout.addWidget(self.descLabel)
		self.nameLine = QtGui.QLineEdit(AddUser)
		self.nameLine.setObjectName(_fromUtf8("nameLine"))
		self.verticalLayout.addWidget(self.nameLine)
		self.syncCheck = QtGui.QCheckBox(AddUser)
		self.syncCheck.setObjectName(_fromUtf8("syncCheck"))
		self.verticalLayout.addWidget(self.syncCheck)
		self.detailsWid = QtGui.QWidget(AddUser)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.detailsWid.sizePolicy().hasHeightForWidth())
		self.detailsWid.setSizePolicy(sizePolicy)
		self.detailsWid.setObjectName(_fromUtf8("detailsWid"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.detailsWid)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.pwLabel = QtGui.QLabel(self.detailsWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pwLabel.sizePolicy().hasHeightForWidth())
		self.pwLabel.setSizePolicy(sizePolicy)
		self.pwLabel.setObjectName(_fromUtf8("pwLabel"))
		self.verticalLayout_2.addWidget(self.pwLabel)
		self.pwLine = QtGui.QLineEdit(self.detailsWid)
		self.pwLine.setEchoMode(QtGui.QLineEdit.Password)
		self.pwLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.pwLine.setObjectName(_fromUtf8("pwLine"))
		self.verticalLayout_2.addWidget(self.pwLine)
		self.uidLabel = QtGui.QLabel(self.detailsWid)
		self.uidLabel.setObjectName(_fromUtf8("uidLabel"))
		self.verticalLayout_2.addWidget(self.uidLabel)
		self.uidSpin = QtGui.QSpinBox(self.detailsWid)
		self.uidSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.uidSpin.setMinimum(1000)
		self.uidSpin.setMaximum(65535)
		self.uidSpin.setObjectName(_fromUtf8("uidSpin"))
		self.verticalLayout_2.addWidget(self.uidSpin)
		self.initGLabel = QtGui.QLabel(self.detailsWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.initGLabel.sizePolicy().hasHeightForWidth())
		self.initGLabel.setSizePolicy(sizePolicy)
		self.initGLabel.setObjectName(_fromUtf8("initGLabel"))
		self.verticalLayout_2.addWidget(self.initGLabel)
		self.initGLine = QtGui.QLineEdit(self.detailsWid)
		self.initGLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.initGLine.setObjectName(_fromUtf8("initGLine"))
		self.verticalLayout_2.addWidget(self.initGLine)
		self.groupsLabel = QtGui.QLabel(self.detailsWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.groupsLabel.sizePolicy().hasHeightForWidth())
		self.groupsLabel.setSizePolicy(sizePolicy)
		self.groupsLabel.setObjectName(_fromUtf8("groupsLabel"))
		self.verticalLayout_2.addWidget(self.groupsLabel)
		self.groupsLine = QtGui.QLineEdit(self.detailsWid)
		self.groupsLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.groupsLine.setObjectName(_fromUtf8("groupsLine"))
		self.verticalLayout_2.addWidget(self.groupsLine)
		self.homeLabel = QtGui.QLabel(self.detailsWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.homeLabel.sizePolicy().hasHeightForWidth())
		self.homeLabel.setSizePolicy(sizePolicy)
		self.homeLabel.setObjectName(_fromUtf8("homeLabel"))
		self.verticalLayout_2.addWidget(self.homeLabel)
		self.homeLine = QtGui.QLineEdit(self.detailsWid)
		self.homeLine.setText(_fromUtf8("/home"))
		self.homeLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.homeLine.setObjectName(_fromUtf8("homeLine"))
		self.verticalLayout_2.addWidget(self.homeLine)
		self.shellLabel = QtGui.QLabel(self.detailsWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.shellLabel.sizePolicy().hasHeightForWidth())
		self.shellLabel.setSizePolicy(sizePolicy)
		self.shellLabel.setObjectName(_fromUtf8("shellLabel"))
		self.verticalLayout_2.addWidget(self.shellLabel)
		self.shellLine = QtGui.QLineEdit(self.detailsWid)
		self.shellLine.setText(_fromUtf8("/bin/bash"))
		self.shellLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.shellLine.setObjectName(_fromUtf8("shellLine"))
		self.verticalLayout_2.addWidget(self.shellLine)
		self.verticalLayout.addWidget(self.detailsWid)
		self.buttonBox = QtGui.QDialogButtonBox(AddUser)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(AddUser)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddUser.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddUser.reject)
		QtCore.QObject.connect(self.syncCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.detailsWid.setVisible)
		QtCore.QObject.connect(self.nameLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AddUser.userChanged)
		QtCore.QMetaObject.connectSlotsByName(AddUser)

	def retranslateUi(self, AddUser):
		AddUser.setWindowTitle(QtGui.QApplication.translate("AddUser", "Add User", None, QtGui.QApplication.UnicodeUTF8))
		self.descLabel.setText(QtGui.QApplication.translate("AddUser", "Enter a new user name below:", None, QtGui.QApplication.UnicodeUTF8))
		self.syncCheck.setText(QtGui.QApplication.translate("AddUser", "Add this user to host accounts if it doesn\'t exist (sync).", None, QtGui.QApplication.UnicodeUTF8))
		self.pwLabel.setText(QtGui.QApplication.translate("AddUser", "Password:", None, QtGui.QApplication.UnicodeUTF8))
		self.uidLabel.setText(QtGui.QApplication.translate("AddUser", "UID:", None, QtGui.QApplication.UnicodeUTF8))
		self.initGLabel.setText(QtGui.QApplication.translate("AddUser", "Initial Group:", None, QtGui.QApplication.UnicodeUTF8))
		self.groupsLabel.setText(QtGui.QApplication.translate("AddUser", "Other Groups (comma separated):", None, QtGui.QApplication.UnicodeUTF8))
		self.homeLabel.setText(QtGui.QApplication.translate("AddUser", "Home:", None, QtGui.QApplication.UnicodeUTF8))
		self.shellLabel.setText(QtGui.QApplication.translate("AddUser", "Shell:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	AddUser = QtGui.QDialog()
	ui = Ui_AddUser()
	ui.setupUi(AddUser)
	AddUser.show()
	sys.exit(app.exec_())

