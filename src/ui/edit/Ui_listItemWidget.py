# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/edit/listItemWidget.ui'
#
# Created: Mon Feb 21 18:35:30 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_listItemWidget(object):
	def setupUi(self, listItemWidget):
		listItemWidget.setObjectName(_fromUtf8("listItemWidget"))
		listItemWidget.resize(559, 205)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(listItemWidget.sizePolicy().hasHeightForWidth())
		listItemWidget.setSizePolicy(sizePolicy)
		listItemWidget.setMinimumSize(QtCore.QSize(0, 0))
		self.verticalLayout = QtGui.QVBoxLayout(listItemWidget)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.collapsedWid = QtGui.QWidget(listItemWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.collapsedWid.sizePolicy().hasHeightForWidth())
		self.collapsedWid.setSizePolicy(sizePolicy)
		self.collapsedWid.setMinimumSize(QtCore.QSize(0, 40))
		self.collapsedWid.setMaximumSize(QtCore.QSize(16777215, 40))
		self.collapsedWid.setObjectName(_fromUtf8("collapsedWid"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.collapsedWid)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setMargin(4)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.expandButtonWid = QtGui.QFrame(self.collapsedWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.expandButtonWid.sizePolicy().hasHeightForWidth())
		self.expandButtonWid.setSizePolicy(sizePolicy)
		self.expandButtonWid.setFrameShape(QtGui.QFrame.StyledPanel)
		self.expandButtonWid.setFrameShadow(QtGui.QFrame.Raised)
		self.expandButtonWid.setObjectName(_fromUtf8("expandButtonWid"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.expandButtonWid)
		self.horizontalLayout_2.setSpacing(0)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.expandButton = QtGui.QToolButton(self.expandButtonWid)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/profile_edit/arrow-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.expandButton.setIcon(icon)
		self.expandButton.setIconSize(QtCore.QSize(26, 26))
		self.expandButton.setAutoRaise(True)
		self.expandButton.setObjectName(_fromUtf8("expandButton"))
		self.horizontalLayout_2.addWidget(self.expandButton)
		self.horizontalLayout.addWidget(self.expandButtonWid)
		self.prettyWid = QtGui.QFrame(self.collapsedWid)
		self.prettyWid.setFrameShape(QtGui.QFrame.StyledPanel)
		self.prettyWid.setFrameShadow(QtGui.QFrame.Raised)
		self.prettyWid.setObjectName(_fromUtf8("prettyWid"))
		self.horizontalLayout_9 = QtGui.QHBoxLayout(self.prettyWid)
		self.horizontalLayout_9.setSpacing(0)
		self.horizontalLayout_9.setMargin(0)
		self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
		self.prettyLabel = QtGui.QLabel(self.prettyWid)
		self.prettyLabel.setObjectName(_fromUtf8("prettyLabel"))
		self.horizontalLayout_9.addWidget(self.prettyLabel)
		self.horizontalLayout.addWidget(self.prettyWid)
		self.activateFrame = QtGui.QFrame(self.collapsedWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.activateFrame.sizePolicy().hasHeightForWidth())
		self.activateFrame.setSizePolicy(sizePolicy)
		self.activateFrame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.activateFrame.setFrameShadow(QtGui.QFrame.Raised)
		self.activateFrame.setObjectName(_fromUtf8("activateFrame"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.activateFrame)
		self.horizontalLayout_3.setSpacing(0)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.toggleButtonCol = QtGui.QToolButton(self.activateFrame)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.toggleButtonCol.sizePolicy().hasHeightForWidth())
		self.toggleButtonCol.setSizePolicy(sizePolicy)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit_icon/ok.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.toggleButtonCol.setIcon(icon1)
		self.toggleButtonCol.setIconSize(QtCore.QSize(22, 22))
		self.toggleButtonCol.setCheckable(True)
		self.toggleButtonCol.setObjectName(_fromUtf8("toggleButtonCol"))
		self.horizontalLayout_3.addWidget(self.toggleButtonCol)
		self.horizontalLayout.addWidget(self.activateFrame)
		self.verticalLayout.addWidget(self.collapsedWid)
		self.expandedWid = QtGui.QWidget(listItemWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.expandedWid.sizePolicy().hasHeightForWidth())
		self.expandedWid.setSizePolicy(sizePolicy)
		self.expandedWid.setMinimumSize(QtCore.QSize(0, 165))
		self.expandedWid.setMaximumSize(QtCore.QSize(16777215, 165))
		self.expandedWid.setObjectName(_fromUtf8("expandedWid"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.expandedWid)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.titleWid = QtGui.QWidget(self.expandedWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.titleWid.sizePolicy().hasHeightForWidth())
		self.titleWid.setSizePolicy(sizePolicy)
		self.titleWid.setObjectName(_fromUtf8("titleWid"))
		self.horizontalLayout_7 = QtGui.QHBoxLayout(self.titleWid)
		self.horizontalLayout_7.setSpacing(0)
		self.horizontalLayout_7.setMargin(0)
		self.horizontalLayout_7.setMargin(0)
		self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
		self.collapseButtonWid = QtGui.QFrame(self.titleWid)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.collapseButtonWid.sizePolicy().hasHeightForWidth())
		self.collapseButtonWid.setSizePolicy(sizePolicy)
		self.collapseButtonWid.setFrameShape(QtGui.QFrame.StyledPanel)
		self.collapseButtonWid.setFrameShadow(QtGui.QFrame.Raised)
		self.collapseButtonWid.setObjectName(_fromUtf8("collapseButtonWid"))
		self.horizontalLayout_10 = QtGui.QHBoxLayout(self.collapseButtonWid)
		self.horizontalLayout_10.setSpacing(0)
		self.horizontalLayout_10.setMargin(0)
		self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
		self.collapseButton = QtGui.QToolButton(self.collapseButtonWid)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/profile_edit/arrow-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.collapseButton.setIcon(icon2)
		self.collapseButton.setIconSize(QtCore.QSize(26, 26))
		self.collapseButton.setAutoRaise(True)
		self.collapseButton.setObjectName(_fromUtf8("collapseButton"))
		self.horizontalLayout_10.addWidget(self.collapseButton)
		self.horizontalLayout_7.addWidget(self.collapseButtonWid)
		self.prettyName = QtGui.QFrame(self.titleWid)
		self.prettyName.setFrameShape(QtGui.QFrame.StyledPanel)
		self.prettyName.setFrameShadow(QtGui.QFrame.Raised)
		self.prettyName.setObjectName(_fromUtf8("prettyName"))
		self.horizontalLayout_5 = QtGui.QHBoxLayout(self.prettyName)
		self.horizontalLayout_5.setSpacing(0)
		self.horizontalLayout_5.setMargin(0)
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.prettyLabel_2 = QtGui.QLabel(self.prettyName)
		self.prettyLabel_2.setStyleSheet(_fromUtf8("font-weight: bold;"))
		self.prettyLabel_2.setObjectName(_fromUtf8("prettyLabel_2"))
		self.horizontalLayout_5.addWidget(self.prettyLabel_2)
		self.horizontalLayout_7.addWidget(self.prettyName)
		self.verticalLayout_2.addWidget(self.titleWid)
		self.description = QtGui.QWidget(self.expandedWid)
		self.description.setObjectName(_fromUtf8("description"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.description)
		self.verticalLayout_3.setSpacing(4)
		self.verticalLayout_3.setContentsMargins(8, 4, 8, 4)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.descriptionText = QtGui.QTextEdit(self.description)
		self.descriptionText.setReadOnly(True)
		self.descriptionText.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
		self.descriptionText.setObjectName(_fromUtf8("descriptionText"))
		self.verticalLayout_3.addWidget(self.descriptionText)
		self.verticalLayout_2.addWidget(self.description)
		self.buttonBox = QtGui.QWidget(self.expandedWid)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.horizontalLayout_8 = QtGui.QHBoxLayout(self.buttonBox)
		self.horizontalLayout_8.setSpacing(4)
		self.horizontalLayout_8.setContentsMargins(8, 0, 8, 4)
		self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_8.addItem(spacerItem)
		self.configureButton = QtGui.QPushButton(self.buttonBox)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/profile_edit/configure.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.configureButton.setIcon(icon3)
		self.configureButton.setObjectName(_fromUtf8("configureButton"))
		self.horizontalLayout_8.addWidget(self.configureButton)
		self.toggleButtonExp = QtGui.QPushButton(self.buttonBox)
		self.toggleButtonExp.setIcon(icon1)
		self.toggleButtonExp.setCheckable(True)
		self.toggleButtonExp.setObjectName(_fromUtf8("toggleButtonExp"))
		self.horizontalLayout_8.addWidget(self.toggleButtonExp)
		self.verticalLayout_2.addWidget(self.buttonBox)
		self.verticalLayout.addWidget(self.expandedWid)

		self.retranslateUi(listItemWidget)
		QtCore.QObject.connect(self.expandButton, QtCore.SIGNAL(_fromUtf8("clicked()")), listItemWidget.setExpanded)
		QtCore.QObject.connect(self.collapseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), listItemWidget.setExpanded)
		QtCore.QObject.connect(self.toggleButtonExp, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), listItemWidget.setActivated)
		QtCore.QObject.connect(self.toggleButtonCol, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), listItemWidget.setActivated)
		QtCore.QMetaObject.connectSlotsByName(listItemWidget)

	def retranslateUi(self, listItemWidget):
		listItemWidget.setWindowTitle(QtGui.QApplication.translate("listItemWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.expandButton.setText(QtGui.QApplication.translate("listItemWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.prettyLabel.setText(QtGui.QApplication.translate("listItemWidget", "Pretty Option Name", None, QtGui.QApplication.UnicodeUTF8))
		self.toggleButtonCol.setText(QtGui.QApplication.translate("listItemWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.collapseButton.setText(QtGui.QApplication.translate("listItemWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.prettyLabel_2.setText(QtGui.QApplication.translate("listItemWidget", "Pretty Option Name", None, QtGui.QApplication.UnicodeUTF8))
		self.configureButton.setText(QtGui.QApplication.translate("listItemWidget", "Configure", None, QtGui.QApplication.UnicodeUTF8))
		self.toggleButtonExp.setText(QtGui.QApplication.translate("listItemWidget", "Activate", None, QtGui.QApplication.UnicodeUTF8))

from ui.icons import temp_icons_rc

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	listItemWidget = QtGui.QWidget()
	ui = Ui_listItemWidget()
	ui.setupUi(listItemWidget)
	listItemWidget.show()
	sys.exit(app.exec_())

