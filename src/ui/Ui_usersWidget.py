# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/D/Dev/Librix/thinclient/src/ui/usersWidget.ui'
#
# Created: Wed Oct 13 18:55:22 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_UsersWidget(object):
    def setupUi(self, UsersWidget):
        UsersWidget.setObjectName(_fromUtf8("UsersWidget"))
        UsersWidget.resize(500, 430)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UsersWidget.sizePolicy().hasHeightForWidth())
        UsersWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(UsersWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.usersAndProfiles = QtGui.QWidget(UsersWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usersAndProfiles.sizePolicy().hasHeightForWidth())
        self.usersAndProfiles.setSizePolicy(sizePolicy)
        self.usersAndProfiles.setObjectName(_fromUtf8("usersAndProfiles"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.usersAndProfiles)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.usersWidget = QtGui.QWidget(self.usersAndProfiles)
        self.usersWidget.setObjectName(_fromUtf8("usersWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.usersWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.usersLabel = QtGui.QLabel(self.usersWidget)
        self.usersLabel.setObjectName(_fromUtf8("usersLabel"))
        self.verticalLayout_3.addWidget(self.usersLabel)
        self.usersList = QtGui.QListWidget(self.usersWidget)
        self.usersList.setDragEnabled(True)
        self.usersList.setDragDropOverwriteMode(True)
        self.usersList.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.usersList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.usersList.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.usersList.setObjectName(_fromUtf8("usersList"))
        self.verticalLayout_3.addWidget(self.usersList)
        self.horizontalLayout.addWidget(self.usersWidget)
        self.buttons = QtGui.QWidget(self.usersAndProfiles)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setMaximumSize(QtCore.QSize(25, 60))
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.buttons)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.add = QtGui.QPushButton(self.buttons)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/add_icon/arrow-right-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon)
        self.add.setObjectName(_fromUtf8("add"))
        self.verticalLayout_2.addWidget(self.add)
        self.remove = QtGui.QPushButton(self.buttons)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/remove_icon/arrow-left-double.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon1)
        self.remove.setObjectName(_fromUtf8("remove"))
        self.verticalLayout_2.addWidget(self.remove)
        self.horizontalLayout.addWidget(self.buttons)
        self.profilesWidget = QtGui.QWidget(self.usersAndProfiles)
        self.profilesWidget.setObjectName(_fromUtf8("profilesWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.profilesWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.profilesLabel = QtGui.QLabel(self.profilesWidget)
        self.profilesLabel.setObjectName(_fromUtf8("profilesLabel"))
        self.verticalLayout_4.addWidget(self.profilesLabel)
        self.profilesTree = QtGui.QTreeWidget(self.profilesWidget)
        self.profilesTree.setDragEnabled(True)
        self.profilesTree.setDragDropOverwriteMode(True)
        self.profilesTree.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.profilesTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.profilesTree.setObjectName(_fromUtf8("profilesTree"))
        self.verticalLayout_4.addWidget(self.profilesTree)
        self.horizontalLayout.addWidget(self.profilesWidget)
        self.verticalLayout.addWidget(self.usersAndProfiles)
        self.summaryDock = QtGui.QDockWidget(UsersWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summaryDock.sizePolicy().hasHeightForWidth())
        self.summaryDock.setSizePolicy(sizePolicy)
        self.summaryDock.setMaximumSize(QtCore.QSize(524287, 200))
        self.summaryDock.setSizeIncrement(QtCore.QSize(10, 10))
        self.summaryDock.setBaseSize(QtCore.QSize(150, 150))
        self.summaryDock.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.summaryDock.setObjectName(_fromUtf8("summaryDock"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.summaryDock.setWidget(self.dockWidgetContents)
        self.verticalLayout.addWidget(self.summaryDock)

        self.retranslateUi(UsersWidget)
        QtCore.QMetaObject.connectSlotsByName(UsersWidget)

    def retranslateUi(self, UsersWidget):
        UsersWidget.setWindowTitle(QtGui.QApplication.translate("UsersWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.usersLabel.setText(QtGui.QApplication.translate("UsersWidget", "Users:", None, QtGui.QApplication.UnicodeUTF8))
        self.profilesLabel.setText(QtGui.QApplication.translate("UsersWidget", "Profiles:", None, QtGui.QApplication.UnicodeUTF8))
        self.profilesTree.headerItem().setText(0, QtGui.QApplication.translate("UsersWidget", "Profiles", None, QtGui.QApplication.UnicodeUTF8))
        self.summaryDock.setWindowTitle(QtGui.QApplication.translate("UsersWidget", "Profile Summary:", None, QtGui.QApplication.UnicodeUTF8))

import temp_icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UsersWidget = QtGui.QWidget()
    ui = Ui_UsersWidget()
    ui.setupUi(UsersWidget)
    UsersWidget.show()
    sys.exit(app.exec_())

