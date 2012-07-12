# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/account_login.ui'
#
# Created: Thu Jul 12 13:40:47 2012
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
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_info = QtGui.QLabel(self.centralwidget)
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))
        self.verticalLayout.addWidget(self.lbl_info)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.edt_email = QtGui.QLineEdit(self.centralwidget)
        self.edt_email.setObjectName(_fromUtf8("edt_email"))
        self.gridLayout.addWidget(self.edt_email, 0, 1, 1, 1)
        self.lbl_email = QtGui.QLabel(self.centralwidget)
        self.lbl_email.setObjectName(_fromUtf8("lbl_email"))
        self.gridLayout.addWidget(self.lbl_email, 0, 0, 1, 1)
        self.lbl_password = QtGui.QLabel(self.centralwidget)
        self.lbl_password.setObjectName(_fromUtf8("lbl_password"))
        self.gridLayout.addWidget(self.lbl_password, 1, 0, 1, 1)
        self.edt_password = QtGui.QLineEdit(self.centralwidget)
        self.edt_password.setEchoMode(QtGui.QLineEdit.Password)
        self.edt_password.setObjectName(_fromUtf8("edt_password"))
        self.gridLayout.addWidget(self.edt_password, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btn_login = QtGui.QPushButton(self.centralwidget)
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.verticalLayout.addWidget(self.btn_login)
        AccountLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountLogin)
        QtCore.QMetaObject.connectSlotsByName(AccountLogin)

    def retranslateUi(self, AccountLogin):
        AccountLogin.setWindowTitle(QtGui.QApplication.translate("AccountLogin", "Log in to Google Music", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_info.setText(QtGui.QApplication.translate("AccountLogin", "<html><head/><body><p>In order to use Google Music you have to specify your Google account\'s email address and password.<br/>You only need to do this once.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_email.setText(QtGui.QApplication.translate("AccountLogin", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_password.setText(QtGui.QApplication.translate("AccountLogin", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_login.setText(QtGui.QApplication.translate("AccountLogin", "Log in", None, QtGui.QApplication.UnicodeUTF8))

