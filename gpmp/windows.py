u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QMainWindow, QMessageBox

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
        # Initialize model.
        self.model.restore()
        # Open log in window if necessary.
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
        # Listen for UI events.
        self.btn_login.clicked.connect(self.login_clicked)

    def login_clicked(self, *args, **kwargs):
        u"Validate fields and try logging in."
        email = self.edt_email.text()
        password = self.edt_password.text()
        if not email or not password:
            return QMessageBox.critical(self, "Missing credentials",
                "You have to provide your email and password.")

        if not self.model.login(email, password):
            return QMessageBox.critical(self, "Wrong credentials",
                "The email or password you provided is invalid.")
        else:
            self.close()
