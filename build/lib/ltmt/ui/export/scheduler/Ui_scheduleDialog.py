# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/export/scheduler/scheduleDialog.ui'
#
# Created: Tue Mar 22 00:51:10 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_Scheduler(object):
	def setupUi(self, Scheduler):
		Scheduler.setObjectName(_fromUtf8("Scheduler"))
		Scheduler.setWindowModality(QtCore.Qt.WindowModal)
		Scheduler.resize(500, 151)
		Scheduler.setMinimumSize(QtCore.QSize(500, 0))
		Scheduler.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(Scheduler)
		self.verticalLayout.setSpacing(4)
		self.verticalLayout.setMargin(4)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.operationLabel = QtGui.QLabel(Scheduler)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.operationLabel.sizePolicy().hasHeightForWidth())
		self.operationLabel.setSizePolicy(sizePolicy)
		self.operationLabel.setStyleSheet(_fromUtf8("font-weight: bold;"))
		self.operationLabel.setObjectName(_fromUtf8("operationLabel"))
		self.verticalLayout.addWidget(self.operationLabel)
		self.mainWidget = QtGui.QWidget(Scheduler)
		self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.mainWidget)
		self.verticalLayout_2.setSpacing(4)
		self.verticalLayout_2.setMargin(4)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.progressLabel = QtGui.QLabel(self.mainWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
		self.progressLabel.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(8)
		self.progressLabel.setFont(font)
		self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.progressLabel.setIndent(1)
		self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
		self.verticalLayout_2.addWidget(self.progressLabel)
		self.progressBar = QtGui.QProgressBar(self.mainWidget)
		self.progressBar.setProperty(_fromUtf8("value"), 24)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		self.verticalLayout_2.addWidget(self.progressBar)
		self.verticalLayout.addWidget(self.mainWidget)
		self.buttonBox = QtGui.QWidget(Scheduler)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
		self.buttonBox.setSizePolicy(sizePolicy)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.buttonBox)
		self.horizontalLayout.setSpacing(4)
		self.horizontalLayout.setMargin(4)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.continueButton = QtGui.QPushButton(self.buttonBox)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ssh_export/arrow-down-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.continueButton.setIcon(icon)
		self.continueButton.setCheckable(True)
		self.continueButton.setDefault(True)
		self.continueButton.setObjectName(_fromUtf8("continueButton"))
		self.horizontalLayout.addWidget(self.continueButton)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.cancelButton = QtGui.QPushButton(self.buttonBox)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.cancelButton.setIcon(icon1)
		self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
		self.horizontalLayout.addWidget(self.cancelButton)
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(Scheduler)
		QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Scheduler.reject)
		QtCore.QObject.connect(self.continueButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Scheduler.accept)
		QtCore.QMetaObject.connectSlotsByName(Scheduler)

	def retranslateUi(self, Scheduler):
		Scheduler.setWindowTitle(QtGui.QApplication.translate("Scheduler", "Scheduled Export", None, QtGui.QApplication.UnicodeUTF8))
		self.operationLabel.setText(QtGui.QApplication.translate("Scheduler", "Exporting Config Files and Updates through SSH", None, QtGui.QApplication.UnicodeUTF8))
		self.progressLabel.setText(QtGui.QApplication.translate("Scheduler", "Begin: <b>{0}</b>\n"
"<br>Elapsed: <b>{1}</b>\n"
"<br>Remaining: <b>{2}</b>\n"
"<br>End: <b>{3}</b>", None, QtGui.QApplication.UnicodeUTF8))
		self.continueButton.setToolTip(QtGui.QApplication.translate("Scheduler", "Proceed to Export", None, QtGui.QApplication.UnicodeUTF8))
		self.continueButton.setStatusTip(QtGui.QApplication.translate("Scheduler", "Proceed to Export", None, QtGui.QApplication.UnicodeUTF8))
		self.continueButton.setWhatsThis(QtGui.QApplication.translate("Scheduler", "Proceed to Export", None, QtGui.QApplication.UnicodeUTF8))
		self.continueButton.setText(QtGui.QApplication.translate("Scheduler", "Continue", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setToolTip(QtGui.QApplication.translate("Scheduler", "Cancel nonstarted operations", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setStatusTip(QtGui.QApplication.translate("Scheduler", "Cancel nonstarted operations", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setWhatsThis(QtGui.QApplication.translate("Scheduler", "Cancel nonstarted operations", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setText(QtGui.QApplication.translate("Scheduler", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from ltmt.ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Scheduler = QtGui.QDialog()
	ui = Ui_Scheduler()
	ui.setupUi(Scheduler)
	Scheduler.show()
	sys.exit(app.exec_())

