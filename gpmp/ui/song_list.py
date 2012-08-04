# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/song_list.ui'
#
# Created: Sat Aug  4 19:13:57 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SongList(object):
    def setupUi(self, SongList):
        SongList.setObjectName(_fromUtf8("SongList"))
        self.centralwidget = QtGui.QWidget(SongList)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.list = QtGui.QListWidget(self.centralwidget)
        self.list.setObjectName(_fromUtf8("list"))
        self.verticalLayout.addWidget(self.list)
        SongList.setCentralWidget(self.centralwidget)

        self.retranslateUi(SongList)
        QtCore.QMetaObject.connectSlotsByName(SongList)

    def retranslateUi(self, SongList):
        SongList.setWindowTitle(QtGui.QApplication.translate("SongList", "Song list", None, QtGui.QApplication.UnicodeUTF8))

