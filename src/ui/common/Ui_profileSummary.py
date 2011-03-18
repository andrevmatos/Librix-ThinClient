# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/common/profileSummary.ui'
#
# Created: Fri Mar 18 14:34:49 2011
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
		Summary.resize(450, 550)
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
		self.content.setGeometry(QtCore.QRect(0, 0, 434, 534))
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
		self.horizontalLayout = QtGui.QHBoxLayout(self.configsWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.verticalLayout_3.addWidget(self.configsWidget)
		self.scrollArea.setWidget(self.content)
		self.verticalLayout_2.addWidget(self.scrollArea)
		self.verticalLayout.addWidget(self.frame)

		self.retranslateUi(Summary)
		QtCore.QMetaObject.connectSlotsByName(Summary)

	def retranslateUi(self, Summary):
		Summary.setWindowTitle(QtGui.QApplication.translate("Summary", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Summary = QtGui.QWidget()
	ui = Ui_Summary()
	ui.setupUi(Summary)
	Summary.show()
	sys.exit(app.exec_())

