# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpmp/ui/playlists.ui'
#
# Created: Sun Jul 15 16:32:15 2012
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
        self.tbw_playlists = QtGui.QTabWidget(self.centralwidget)
        self.tbw_playlists.setObjectName(_fromUtf8("tbw_playlists"))
        self.tab_auto = QtGui.QWidget()
        self.tab_auto.setObjectName(_fromUtf8("tab_auto"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_auto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lst_auto = QtGui.QListWidget(self.tab_auto)
        self.lst_auto.setObjectName(_fromUtf8("lst_auto"))
        self.verticalLayout.addWidget(self.lst_auto)
        self.tbw_playlists.addTab(self.tab_auto, _fromUtf8(""))
        self.tab_instant = QtGui.QWidget()
        self.tab_instant.setObjectName(_fromUtf8("tab_instant"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_instant)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lst_instant = QtGui.QListWidget(self.tab_instant)
        self.lst_instant.setObjectName(_fromUtf8("lst_instant"))
        self.verticalLayout_2.addWidget(self.lst_instant)
        self.tbw_playlists.addTab(self.tab_instant, _fromUtf8(""))
        self.tab_custom = QtGui.QWidget()
        self.tab_custom.setObjectName(_fromUtf8("tab_custom"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_custom)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lst_custom = QtGui.QListWidget(self.tab_custom)
        self.lst_custom.setObjectName(_fromUtf8("lst_custom"))
        self.verticalLayout_3.addWidget(self.lst_custom)
        self.tbw_playlists.addTab(self.tab_custom, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tbw_playlists)
        Playlists.setCentralWidget(self.centralwidget)

        self.retranslateUi(Playlists)
        self.tbw_playlists.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Playlists)

    def retranslateUi(self, Playlists):
        Playlists.setWindowTitle(QtGui.QApplication.translate("Playlists", "Playlists", None, QtGui.QApplication.UnicodeUTF8))
        self.tbw_playlists.setTabText(self.tbw_playlists.indexOf(self.tab_auto), QtGui.QApplication.translate("Playlists", "Auto playlists", None, QtGui.QApplication.UnicodeUTF8))
        self.tbw_playlists.setTabText(self.tbw_playlists.indexOf(self.tab_instant), QtGui.QApplication.translate("Playlists", "Instant mixes", None, QtGui.QApplication.UnicodeUTF8))
        self.tbw_playlists.setTabText(self.tbw_playlists.indexOf(self.tab_custom), QtGui.QApplication.translate("Playlists", "Custom playlists", None, QtGui.QApplication.UnicodeUTF8))

