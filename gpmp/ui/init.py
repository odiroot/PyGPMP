# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/init.ui'
#
# Created: Sat Aug 25 18:53:33 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_InitWindow(object):
    def setupUi(self, InitWindow):
        InitWindow.setObjectName(_fromUtf8("InitWindow"))
        self.centralwidget = QtGui.QWidget(InitWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        InitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InitWindow)
        QtCore.QMetaObject.connectSlotsByName(InitWindow)

    def retranslateUi(self, InitWindow):
        InitWindow.setWindowTitle(QtGui.QApplication.translate("InitWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("InitWindow", "Please wait for application initialization to finish...", None, QtGui.QApplication.UnicodeUTF8))

