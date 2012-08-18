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
        # Dispose of window object after close.
        self.setAttribute(Qt.WA_DeleteOnClose)


class SimpleWidgetWindow(QMainWindow, StackedWindowMixin):
    def __init__(self, parent=None, controller=None):
        QMainWindow.__init__(self, parent=parent)
        StackedWindowMixin.__init__(self)
        self.controller = controller
        self.setWindowTitle(QCoreApplication.instance().applicationName())
        self.show_content()

    def show_content(self):
        pass


class InitWindow(SimpleWidgetWindow):
    u"Splash screen of some sort."
    def show_content(self):
        self.setCentralWidget(QLabel("Please wait for application"
            " initialization to finish...", parent=self))


class MenuWindow(SimpleWidgetWindow):
    u"Window shown after logon. Shows main application actions."
    def show_content(self):
        self.setCentralWidget(MainMenu(parent=self,
            controller=self.controller))


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
            # Break reference, so window can be cleaned.
            self.controller.clean_window(self)

    def closeEvent(self, event):
        event.accept()
        if self.callback:
            self.callback()
