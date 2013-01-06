# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/main_menu.ui'
#
# Created: Sun Jan  6 13:25:50 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName(_fromUtf8("MainMenu"))
        MainMenu.resize(139, 154)
        self.centralwidget = QtGui.QWidget(MainMenu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_user = QtGui.QLabel(self.centralwidget)
        self.lbl_user.setObjectName(_fromUtf8("lbl_user"))
        self.verticalLayout.addWidget(self.lbl_user)
        self.btn_user_lists = QtGui.QPushButton(self.centralwidget)
        self.btn_user_lists.setObjectName(_fromUtf8("btn_user_lists"))
        self.verticalLayout.addWidget(self.btn_user_lists)
        self.btn_auto_lists = QtGui.QPushButton(self.centralwidget)
        self.btn_auto_lists.setObjectName(_fromUtf8("btn_auto_lists"))
        self.verticalLayout.addWidget(self.btn_auto_lists)
        self.btn_now = QtGui.QPushButton(self.centralwidget)
        self.btn_now.setObjectName(_fromUtf8("btn_now"))
        self.verticalLayout.addWidget(self.btn_now)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_quit = QtGui.QPushButton(self.centralwidget)
        self.btn_quit.setObjectName(_fromUtf8("btn_quit"))
        self.verticalLayout.addWidget(self.btn_quit)
        MainMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        self.lbl_user.setText(QtGui.QApplication.translate("MainMenu", "Logged in as:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_user_lists.setText(QtGui.QApplication.translate("MainMenu", "Show user playlists", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_auto_lists.setText(QtGui.QApplication.translate("MainMenu", "Show auto playlists", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_now.setText(QtGui.QApplication.translate("MainMenu", "Now playing", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setText(QtGui.QApplication.translate("MainMenu", "Quit", None, QtGui.QApplication.UnicodeUTF8))

