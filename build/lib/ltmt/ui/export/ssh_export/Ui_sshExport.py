# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/export/ssh_export/sshExport.ui'
#
# Created: Fri Mar 11 14:38:43 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_SSHExport(object):
	def setupUi(self, SSHExport):
		SSHExport.setObjectName(_fromUtf8("SSHExport"))
		SSHExport.setWindowModality(QtCore.Qt.WindowModal)
		SSHExport.resize(600, 394)
		SSHExport.setMinimumSize(QtCore.QSize(600, 0))
		SSHExport.setModal(True)
		self.verticalLayout = QtGui.QVBoxLayout(SSHExport)
		self.verticalLayout.setSpacing(4)
		self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
		self.verticalLayout.setMargin(4)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.operationLabel = QtGui.QLabel(SSHExport)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.operationLabel.sizePolicy().hasHeightForWidth())
		self.operationLabel.setSizePolicy(sizePolicy)
		self.operationLabel.setStyleSheet(_fromUtf8("font-weight: bold;"))
		self.operationLabel.setObjectName(_fromUtf8("operationLabel"))
		self.verticalLayout.addWidget(self.operationLabel)
		self.mainWidget = QtGui.QWidget(SSHExport)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
		self.mainWidget.setSizePolicy(sizePolicy)
		self.mainWidget.setMaximumSize(QtCore.QSize(16777215, 72))
		self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.mainWidget)
		self.verticalLayout_2.setSpacing(4)
		self.verticalLayout_2.setMargin(4)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.progressLabel = QtGui.QLabel(self.mainWidget)
		font = QtGui.QFont()
		font.setPointSize(8)
		self.progressLabel.setFont(font)
		self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.progressLabel.setIndent(1)
		self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
		self.verticalLayout_2.addWidget(self.progressLabel)
		spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.progressBar = QtGui.QProgressBar(self.mainWidget)
		self.progressBar.setProperty(_fromUtf8("value"), 24)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		self.verticalLayout_2.addWidget(self.progressBar)
		spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem1)
		self.verticalLayout.addWidget(self.mainWidget)
		self.buttonBox = QtGui.QWidget(SSHExport)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
		self.buttonBox.setSizePolicy(sizePolicy)
		self.buttonBox.setMinimumSize(QtCore.QSize(500, 0))
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.buttonBox)
		self.horizontalLayout.setSpacing(4)
		self.horizontalLayout.setMargin(4)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.detailsButton = QtGui.QPushButton(self.buttonBox)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ssh_export/arrow-down-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.detailsButton.setIcon(icon)
		self.detailsButton.setCheckable(True)
		self.detailsButton.setDefault(True)
		self.detailsButton.setObjectName(_fromUtf8("detailsButton"))
		self.horizontalLayout.addWidget(self.detailsButton)
		spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem2)
		self.cancelButton = QtGui.QPushButton(self.buttonBox)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.cancelButton.setIcon(icon1)
		self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
		self.horizontalLayout.addWidget(self.cancelButton)
		self.verticalLayout.addWidget(self.buttonBox)
		self.detailsWidget = QtGui.QWidget(SSHExport)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.detailsWidget.sizePolicy().hasHeightForWidth())
		self.detailsWidget.setSizePolicy(sizePolicy)
		self.detailsWidget.setMinimumSize(QtCore.QSize(0, 250))
		self.detailsWidget.setObjectName(_fromUtf8("detailsWidget"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.detailsWidget)
		self.verticalLayout_3.setSpacing(4)
		self.verticalLayout_3.setMargin(4)
		self.verticalLayout_3.setMargin(0)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.detailsTree = QtGui.QTreeWidget(self.detailsWidget)
		self.detailsTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.detailsTree.setAlternatingRowColors(True)
		self.detailsTree.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.detailsTree.setUniformRowHeights(True)
		self.detailsTree.setItemsExpandable(True)
		self.detailsTree.setObjectName(_fromUtf8("detailsTree"))
		self.detailsTree.header().setCascadingSectionResizes(False)
		self.detailsTree.header().setHighlightSections(True)
		self.detailsTree.header().setStretchLastSection(True)
		self.verticalLayout_3.addWidget(self.detailsTree)
		self.verticalLayout.addWidget(self.detailsWidget)

		self.retranslateUi(SSHExport)
		QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SSHExport.reject)
		QtCore.QObject.connect(self.detailsButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), SSHExport.showDetails)
		QtCore.QMetaObject.connectSlotsByName(SSHExport)

	def retranslateUi(self, SSHExport):
		SSHExport.setWindowTitle(QtGui.QApplication.translate("SSHExport", "SSH Export", None, QtGui.QApplication.UnicodeUTF8))
		self.operationLabel.setText(QtGui.QApplication.translate("SSHExport", "Exporting Config Files and Updates through SSH", None, QtGui.QApplication.UnicodeUTF8))
		self.progressLabel.setText(QtGui.QApplication.translate("SSHExport", "Operation {0} of {1}: {2}", None, QtGui.QApplication.UnicodeUTF8))
		self.detailsButton.setToolTip(QtGui.QApplication.translate("SSHExport", "Show detailed status of operation", None, QtGui.QApplication.UnicodeUTF8))
		self.detailsButton.setStatusTip(QtGui.QApplication.translate("SSHExport", "Show detailed status of operation", None, QtGui.QApplication.UnicodeUTF8))
		self.detailsButton.setWhatsThis(QtGui.QApplication.translate("SSHExport", "Show detailed status of operation", None, QtGui.QApplication.UnicodeUTF8))
		self.detailsButton.setText(QtGui.QApplication.translate("SSHExport", "Details", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setToolTip(QtGui.QApplication.translate("SSHExport", "Cancel nonstarted operations", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setStatusTip(QtGui.QApplication.translate("SSHExport", "Cancel nonstarted operations", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setWhatsThis(QtGui.QApplication.translate("SSHExport", "Cancel nonstarted operations", None, QtGui.QApplication.UnicodeUTF8))
		self.cancelButton.setText(QtGui.QApplication.translate("SSHExport", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
		self.detailsTree.headerItem().setText(0, QtGui.QApplication.translate("SSHExport", "Operation", None, QtGui.QApplication.UnicodeUTF8))
		self.detailsTree.headerItem().setText(1, QtGui.QApplication.translate("SSHExport", "Destiny", None, QtGui.QApplication.UnicodeUTF8))
		self.detailsTree.headerItem().setText(2, QtGui.QApplication.translate("SSHExport", "Status", None, QtGui.QApplication.UnicodeUTF8))

from ltmt.ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	SSHExport = QtGui.QDialog()
	ui = Ui_SSHExport()
	ui.setupUi(SSHExport)
	SSHExport.show()
	sys.exit(app.exec_())

