u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QMainWindow

from gpmp.ui.account_login import Ui_AccountLogin


class MainWindow(QMainWindow):
    u"""The main window after app is launched."""
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # TODO: Model like in hsoft/guiskel
        self.setWindowTitle(QCoreApplication.instance().applicationName())
        # TODO: MainWindow ui/pyui.
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        self.show()

        self.login_window = LoginWindow(self)
        self.login_window.show()


class LoginWindow(QMainWindow, Ui_AccountLogin):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        self.setupUi(self)
