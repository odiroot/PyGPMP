# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/main_menu.ui'
#
# Created: Sun Jul 15 15:15:14 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        self.verticalLayout = QtGui.QVBoxLayout(Menu)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_user = QtGui.QLabel(Menu)
        self.lbl_user.setObjectName(_fromUtf8("lbl_user"))
        self.verticalLayout.addWidget(self.lbl_user)
        self.btn_playlists = QtGui.QPushButton(Menu)
        self.btn_playlists.setObjectName(_fromUtf8("btn_playlists"))
        self.verticalLayout.addWidget(self.btn_playlists)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_quit = QtGui.QPushButton(Menu)
        self.btn_quit.setObjectName(_fromUtf8("btn_quit"))
        self.verticalLayout.addWidget(self.btn_quit)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QtGui.QApplication.translate("Menu", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_user.setText(QtGui.QApplication.translate("Menu", "Logged in as:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_playlists.setText(QtGui.QApplication.translate("Menu", "Show playlists", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setText(QtGui.QApplication.translate("Menu", "Quit", None, QtGui.QApplication.UnicodeUTF8))

