# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/playlists.ui'
#
# Created: Tue Sep 11 21:11:37 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Playlists(object):
    def setupUi(self, Playlists):
        Playlists.setObjectName(_fromUtf8("Playlists"))
        self.centralwidget = QtGui.QWidget(Playlists)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lst_lists = QtGui.QListWidget(self.centralwidget)
        self.lst_lists.setObjectName(_fromUtf8("lst_lists"))
        self.verticalLayout.addWidget(self.lst_lists)
        Playlists.setCentralWidget(self.centralwidget)

        self.retranslateUi(Playlists)
        QtCore.QMetaObject.connectSlotsByName(Playlists)

    def retranslateUi(self, Playlists):
        Playlists.setWindowTitle(QtGui.QApplication.translate("Playlists", "Playlists", None, QtGui.QApplication.UnicodeUTF8))

