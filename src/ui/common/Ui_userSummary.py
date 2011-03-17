# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/common/userSummary.ui'
#
# Created: Thu Mar 17 17:59:56 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_Summary(object):
	def setupUi(self, Summary):
		Summary.setObjectName(_fromUtf8("Summary"))
		Summary.resize(597, 223)
		self.verticalLayout = QtGui.QVBoxLayout(Summary)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.frame = QtGui.QFrame(Summary)
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.scrollArea = QtGui.QScrollArea(self.frame)
		self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
		self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.content = QtGui.QWidget()
		self.content.setGeometry(QtCore.QRect(0, 0, 583, 209))
		self.content.setObjectName(_fromUtf8("content"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.content)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.title = QtGui.QLabel(self.content)
		self.title.setText(_fromUtf8(""))
		self.title.setObjectName(_fromUtf8("title"))
		self.verticalLayout_3.addWidget(self.title)
		self.configsWidget = QtGui.QWidget(self.content)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.configsWidget.sizePolicy().hasHeightForWidth())
		self.configsWidget.setSizePolicy(sizePolicy)
		self.configsWidget.setObjectName(_fromUtf8("configsWidget"))
		self.verticalLayout_4 = QtGui.QVBoxLayout(self.configsWidget)
		self.verticalLayout_4.setMargin(0)
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.password = QtGui.QLabel(self.configsWidget)
		self.password.setIndent(20)
		self.password.setObjectName(_fromUtf8("password"))
		self.verticalLayout_4.addWidget(self.password)
		self.uid = QtGui.QLabel(self.configsWidget)
		self.uid.setIndent(20)
		self.uid.setObjectName(_fromUtf8("uid"))
		self.verticalLayout_4.addWidget(self.uid)
		self.initGroup = QtGui.QLabel(self.configsWidget)
		self.initGroup.setIndent(20)
		self.initGroup.setObjectName(_fromUtf8("initGroup"))
		self.verticalLayout_4.addWidget(self.initGroup)
		self.groups = QtGui.QLabel(self.configsWidget)
		self.groups.setIndent(20)
		self.groups.setObjectName(_fromUtf8("groups"))
		self.verticalLayout_4.addWidget(self.groups)
		self.home = QtGui.QLabel(self.configsWidget)
		self.home.setIndent(20)
		self.home.setObjectName(_fromUtf8("home"))
		self.verticalLayout_4.addWidget(self.home)
		self.shell = QtGui.QLabel(self.configsWidget)
		self.shell.setIndent(20)
		self.shell.setObjectName(_fromUtf8("shell"))
		self.verticalLayout_4.addWidget(self.shell)
		self.verticalLayout_3.addWidget(self.configsWidget)
		self.scrollArea.setWidget(self.content)
		self.verticalLayout_2.addWidget(self.scrollArea)
		self.verticalLayout.addWidget(self.frame)

		self.retranslateUi(Summary)
		QtCore.QMetaObject.connectSlotsByName(Summary)

	def retranslateUi(self, Summary):
		Summary.setWindowTitle(QtGui.QApplication.translate("Summary", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.password.setText(QtGui.QApplication.translate("Summary", "<font color=green>Shadow Password Hash:</font> <b>{0}</b>", None, QtGui.QApplication.UnicodeUTF8))
		self.uid.setText(QtGui.QApplication.translate("Summary", "<font color=green>UID:</font> <b>{0}</b>", None, QtGui.QApplication.UnicodeUTF8))
		self.initGroup.setText(QtGui.QApplication.translate("Summary", "<font color=green>Initial Group:</font> <b>{0}</b>", None, QtGui.QApplication.UnicodeUTF8))
		self.groups.setText(QtGui.QApplication.translate("Summary", "<font color=green>Other Groups:</font> <b>{0}</b>", None, QtGui.QApplication.UnicodeUTF8))
		self.home.setText(QtGui.QApplication.translate("Summary", "<font color=green>Home:</font> <b>{0}</b>", None, QtGui.QApplication.UnicodeUTF8))
		self.shell.setText(QtGui.QApplication.translate("Summary", "<font color=green>Shell:</font> <b>{0}</b>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Summary = QtGui.QWidget()
	ui = Ui_Summary()
	ui.setupUi(Summary)
	Summary.show()
	sys.exit(app.exec_())

