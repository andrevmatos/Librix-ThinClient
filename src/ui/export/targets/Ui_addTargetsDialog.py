# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/export/targets/addTargetsDialog.ui'
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

class Ui_AddTargetsDialog(object):
	def setupUi(self, AddTargetsDialog):
		AddTargetsDialog.setObjectName(_fromUtf8("AddTargetsDialog"))
		AddTargetsDialog.resize(570, 360)
		AddTargetsDialog.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(AddTargetsDialog)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(AddTargetsDialog)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		self.label.setMaximumSize(QtCore.QSize(16777215, 30))
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.targetsWidget = QtGui.QWidget(AddTargetsDialog)
		self.targetsWidget.setObjectName(_fromUtf8("targetsWidget"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.targetsWidget)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.singleRadio = QtGui.QRadioButton(self.targetsWidget)
		self.singleRadio.setChecked(True)
		self.singleRadio.setObjectName(_fromUtf8("singleRadio"))
		self.verticalLayout_2.addWidget(self.singleRadio)
		self.singleWidget = QtGui.QWidget(self.targetsWidget)
		self.singleWidget.setObjectName(_fromUtf8("singleWidget"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.singleWidget)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.singleIpLine = QtGui.QLineEdit(self.singleWidget)
		self.singleIpLine.setInputMethodHints(QtCore.Qt.ImhNone)
		self.singleIpLine.setObjectName(_fromUtf8("singleIpLine"))
		self.horizontalLayout_2.addWidget(self.singleIpLine)
		self.verticalLayout_2.addWidget(self.singleWidget)
		self.hostnameRadio = QtGui.QRadioButton(self.targetsWidget)
		self.hostnameRadio.setObjectName(_fromUtf8("hostnameRadio"))
		self.verticalLayout_2.addWidget(self.hostnameRadio)
		self.hostnameWidget = QtGui.QWidget(self.targetsWidget)
		self.hostnameWidget.setObjectName(_fromUtf8("hostnameWidget"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.hostnameWidget)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.hostnameLine = QtGui.QLineEdit(self.hostnameWidget)
		self.hostnameLine.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
		self.hostnameLine.setObjectName(_fromUtf8("hostnameLine"))
		self.horizontalLayout_3.addWidget(self.hostnameLine)
		self.verticalLayout_2.addWidget(self.hostnameWidget)
		self.rangeRadio = QtGui.QRadioButton(self.targetsWidget)
		self.rangeRadio.setObjectName(_fromUtf8("rangeRadio"))
		self.verticalLayout_2.addWidget(self.rangeRadio)
		self.rangeWidget = QtGui.QWidget(self.targetsWidget)
		self.rangeWidget.setObjectName(_fromUtf8("rangeWidget"))
		self.horizontalLayout_4 = QtGui.QHBoxLayout(self.rangeWidget)
		self.horizontalLayout_4.setMargin(0)
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.fromIPLine = QtGui.QLineEdit(self.rangeWidget)
		self.fromIPLine.setObjectName(_fromUtf8("fromIPLine"))
		self.horizontalLayout_4.addWidget(self.fromIPLine)
		self.separatorLabel = QtGui.QLabel(self.rangeWidget)
		self.separatorLabel.setText(_fromUtf8("-"))
		self.separatorLabel.setObjectName(_fromUtf8("separatorLabel"))
		self.horizontalLayout_4.addWidget(self.separatorLabel)
		self.toIPLine = QtGui.QLineEdit(self.rangeWidget)
		self.toIPLine.setObjectName(_fromUtf8("toIPLine"))
		self.horizontalLayout_4.addWidget(self.toIPLine)
		self.verticalLayout_2.addWidget(self.rangeWidget)
		self.subnetRadio = QtGui.QRadioButton(self.targetsWidget)
		self.subnetRadio.setObjectName(_fromUtf8("subnetRadio"))
		self.verticalLayout_2.addWidget(self.subnetRadio)
		self.subnetWidget = QtGui.QWidget(self.targetsWidget)
		self.subnetWidget.setObjectName(_fromUtf8("subnetWidget"))
		self.horizontalLayout_5 = QtGui.QHBoxLayout(self.subnetWidget)
		self.horizontalLayout_5.setMargin(0)
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.IPLine = QtGui.QLineEdit(self.subnetWidget)
		self.IPLine.setObjectName(_fromUtf8("IPLine"))
		self.horizontalLayout_5.addWidget(self.IPLine)
		self.twodotsLabel = QtGui.QLabel(self.subnetWidget)
		self.twodotsLabel.setText(_fromUtf8(":"))
		self.twodotsLabel.setObjectName(_fromUtf8("twodotsLabel"))
		self.horizontalLayout_5.addWidget(self.twodotsLabel)
		self.netmaskLine = QtGui.QLineEdit(self.subnetWidget)
		self.netmaskLine.setObjectName(_fromUtf8("netmaskLine"))
		self.horizontalLayout_5.addWidget(self.netmaskLine)
		self.verticalLayout_2.addWidget(self.subnetWidget)
		self.verticalLayout.addWidget(self.targetsWidget)
		self.buttonBox = QtGui.QWidget(AddTargetsDialog)
		self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 35))
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.buttonBox)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.cancelButton = QtGui.QPushButton(self.buttonBox)
		self.cancelButton.setMinimumSize(QtCore.QSize(100, 0))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.cancelButton.setIcon(icon)
		self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
		self.horizontalLayout.addWidget(self.cancelButton)
		self.nextButton = QtGui.QPushButton(self.buttonBox)
		self.nextButton.setMinimumSize(QtCore.QSize(100, 0))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/add_icon/arrow-right-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.nextButton.setIcon(icon1)
		self.nextButton.setDefault(True)
		self.nextButton.setObjectName(_fromUtf8("nextButton"))
		self.horizontalLayout.addWidget(self.nextButton)
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(AddTargetsDialog)
		QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AddTargetsDialog.close)
		QtCore.QObject.connect(self.singleRadio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), AddTargetsDialog.optClicked)
		QtCore.QObject.connect(self.hostnameRadio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), AddTargetsDialog.optClicked)
		QtCore.QObject.connect(self.rangeRadio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), AddTargetsDialog.optClicked)
		QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AddTargetsDialog.accept)
		QtCore.QObject.connect(self.singleIpLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AddTargetsDialog.parseTargets)
		QtCore.QObject.connect(self.hostnameLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AddTargetsDialog.parseTargets)
		QtCore.QObject.connect(self.fromIPLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AddTargetsDialog.parseTargets)
		QtCore.QObject.connect(self.toIPLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AddTargetsDialog.parseTargets)
		QtCore.QObject.connect(self.IPLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AddTargetsDialog.parseTargets)
		QtCore.QObject.connect(self.netmaskLine, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), AddTargetsDialog.parseTargets)
		QtCore.QObject.connect(self.IPLine, QtCore.SIGNAL(_fromUtf8("returnPressed()")), AddTargetsDialog.accept)
		QtCore.QObject.connect(self.toIPLine, QtCore.SIGNAL(_fromUtf8("returnPressed()")), AddTargetsDialog.accept)
		QtCore.QObject.connect(self.subnetRadio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), AddTargetsDialog.optClicked)
		QtCore.QObject.connect(self.hostnameLine, QtCore.SIGNAL(_fromUtf8("returnPressed()")), AddTargetsDialog.accept)
		QtCore.QObject.connect(self.singleIpLine, QtCore.SIGNAL(_fromUtf8("returnPressed()")), AddTargetsDialog.accept)
		QtCore.QObject.connect(self.netmaskLine, QtCore.SIGNAL(_fromUtf8("returnPressed()")), AddTargetsDialog.accept)
		QtCore.QObject.connect(self.fromIPLine, QtCore.SIGNAL(_fromUtf8("returnPressed()")), AddTargetsDialog.accept)
		QtCore.QMetaObject.connectSlotsByName(AddTargetsDialog)

	def retranslateUi(self, AddTargetsDialog):
		AddTargetsDialog.setWindowTitle(QtGui.QApplication.translate("AddTargetsDialog", "Add targets - Step 1/2", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("AddTargetsDialog", "Select an option. Default values are examples:", None, QtGui.QApplication.UnicodeUTF8))
		self.singleRadio.setText(QtGui.QApplication.translate("AddTargetsDialog", "Single IP:", None, QtGui.QApplication.UnicodeUTF8))
		self.singleIpLine.setText(QtGui.QApplication.translate("AddTargetsDialog", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
		self.hostnameRadio.setText(QtGui.QApplication.translate("AddTargetsDialog", "Hostname:", None, QtGui.QApplication.UnicodeUTF8))
		self.hostnameLine.setText(QtGui.QApplication.translate("AddTargetsDialog", "librixdev.las.ic.unicamp.br", None, QtGui.QApplication.UnicodeUTF8))
		self.rangeRadio.setText(QtGui.QApplication.translate("AddTargetsDialog", "IP Range:", None, QtGui.QApplication.UnicodeUTF8))
		self.fromIPLine.setText(QtGui.QApplication.translate("AddTargetsDialog", "10.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
		self.toIPLine.setText(QtGui.QApplication.translate("AddTargetsDialog", "10.0.0.10", None, QtGui.QApplication.UnicodeUTF8))
		self.subnetRadio.setText(QtGui.QApplication.translate("AddTargetsDialog", "Sub-network:", None, QtGui.QApplication.UnicodeUTF8))
		self.IPLine.setText(QtGui.QApplication.translate("AddTargetsDialog", "192.168.1.1", None, QtGui.QApplication.UnicodeUTF8))
		self.netmaskLine.setText(QtGui.QApplication.translate("AddTargetsDialog", "255.255.255.0", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setText(QtGui.QApplication.translate("AddTargetsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
		self.nextButton.setText(QtGui.QApplication.translate("AddTargetsDialog", "Next", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	AddTargetsDialog = QtGui.QDialog()
	ui = Ui_AddTargetsDialog()
	ui.setupUi(AddTargetsDialog)
	AddTargetsDialog.show()
	sys.exit(app.exec_())

