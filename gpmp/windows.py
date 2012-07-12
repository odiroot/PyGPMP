u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QMainWindow

from gpmp.ui.account_login import Ui_AccountLogin
from gpmp.model import Model


class MainWindow(QMainWindow):
    u"""The main window after app is launched."""
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle(QCoreApplication.instance().applicationName())
        self.model = Model()

        # TODO: MainWindow ui/pyui.
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        # Show main window and proceed with usual behaviour.
        self.show()
        self.run()

    def run(self):
        if not self.model.logged_in:
            self.handle_login()

    def handle_login(self):
        login_window = LoginWindow(self, model=self.model)
        login_window.show()


class LoginWindow(QMainWindow, Ui_AccountLogin):
    def __init__(self, parent=None, model=None):
        QMainWindow.__init__(self, parent)
        self.model = model
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        self.setupUi(self)

    # def closeEvent(self, event):
    #     return QMainWindow.closeEvent(self, event)
