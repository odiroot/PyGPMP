# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/playlists.ui'
#
# Created: Sun Jul 15 15:57:29 2012
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
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.grp_auto = QtGui.QGroupBox(self.centralwidget)
        self.grp_auto.setObjectName(_fromUtf8("grp_auto"))
        self.verticalLayout = QtGui.QVBoxLayout(self.grp_auto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lst_auto = QtGui.QListWidget(self.grp_auto)
        self.lst_auto.setObjectName(_fromUtf8("lst_auto"))
        self.verticalLayout.addWidget(self.lst_auto)
        self.verticalLayout_4.addWidget(self.grp_auto)
        self.grp_instant = QtGui.QGroupBox(self.centralwidget)
        self.grp_instant.setObjectName(_fromUtf8("grp_instant"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.grp_instant)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lst_instant = QtGui.QListWidget(self.grp_instant)
        self.lst_instant.setObjectName(_fromUtf8("lst_instant"))
        self.verticalLayout_2.addWidget(self.lst_instant)
        self.verticalLayout_4.addWidget(self.grp_instant)
        self.grp_custom = QtGui.QGroupBox(self.centralwidget)
        self.grp_custom.setObjectName(_fromUtf8("grp_custom"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.grp_custom)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lst_custom = QtGui.QListWidget(self.grp_custom)
        self.lst_custom.setObjectName(_fromUtf8("lst_custom"))
        self.verticalLayout_3.addWidget(self.lst_custom)
        self.verticalLayout_4.addWidget(self.grp_custom)
        Playlists.setCentralWidget(self.centralwidget)

        self.retranslateUi(Playlists)
        QtCore.QMetaObject.connectSlotsByName(Playlists)

    def retranslateUi(self, Playlists):
        Playlists.setWindowTitle(QtGui.QApplication.translate("Playlists", "Playlists", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_auto.setTitle(QtGui.QApplication.translate("Playlists", "Auto playlists", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_instant.setTitle(QtGui.QApplication.translate("Playlists", "Instant mixes", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_custom.setTitle(QtGui.QApplication.translate("Playlists", "Custom playlists", None, QtGui.QApplication.UnicodeUTF8))

