# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/account_login.ui'
#
# Created: Sat Jul  7 00:32:46 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AccountLogin(object):
    def setupUi(self, AccountLogin):
        AccountLogin.setObjectName(_fromUtf8("AccountLogin"))
        self.centralwidget = QtGui.QWidget(AccountLogin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        AccountLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountLogin)
        QtCore.QMetaObject.connectSlotsByName(AccountLogin)

    def retranslateUi(self, AccountLogin):
        AccountLogin.setWindowTitle(QtGui.QApplication.translate("AccountLogin", "Log in to Google Music", None, QtGui.QApplication.UnicodeUTF8))

