# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/init.ui'
#
# Created: Sat Aug 25 19:24:47 2012
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_tape = QtGui.QLabel(self.centralwidget)
        self.lbl_tape.setText(_fromUtf8(""))
        self.lbl_tape.setObjectName(_fromUtf8("lbl_tape"))
        self.horizontalLayout.addWidget(self.lbl_tape)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        InitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InitWindow)
        QtCore.QMetaObject.connectSlotsByName(InitWindow)

    def retranslateUi(self, InitWindow):
        self.label.setText(QtGui.QApplication.translate("InitWindow", "Please wait for application initialization to finish...", None, QtGui.QApplication.UnicodeUTF8))

