u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QMainWindow, QMessageBox, QLabel

from gpmp.ui.account_login import Ui_AccountLogin
from gpmp.widgets import MainMenu


class StackedWindowMixin(object):
    u"Maemo-specific stacked window."
    def __init__(self):
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass


class InitWindow(QMainWindow):
    u"Splash screen of some sort."
    def __init__(self, parent=None, controller=None):
        QMainWindow.__init__(self, parent=parent)
        self.controller = controller

        self.setWindowTitle(QCoreApplication.instance().applicationName())
        self.setCentralWidget(QLabel("Please wait for application"
            " initialization to finish...", parent=self))

    def show_main_menu(self):
        self._main_menu = MainMenu(parent=self, controller=self.controller)
        self.setCentralWidget(self._main_menu)


class LoginWindow(QMainWindow, StackedWindowMixin, Ui_AccountLogin):
    def __init__(self, parent=None, controller=None, callback=None):
        QMainWindow.__init__(self, parent=parent)
        StackedWindowMixin.__init__(self)
        self.setupUi(self)

        self.controller = controller
        self.callback = callback
        # Listen for UI events.
        self.btn_login.clicked.connect(self.login_clicked)

    def login_clicked(self, *args, **kwargs):
        u"Validate fields and try logging in."
        email = self.edt_email.text()
        password = self.edt_password.text()
        if not email or not password:
            return QMessageBox.critical(self, "Missing credentials",
                "You have to provide your email and password.")

        if not self.controller.login(email, password):
            return QMessageBox.critical(self, "Wrong credentials",
                "The email or password you provided is invalid.")
        else:
            self.close()

    def closeEvent(self, event):
        event.accept()
        if self.callback:
            self.callback()
