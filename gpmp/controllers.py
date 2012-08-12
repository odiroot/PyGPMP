import logging
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QTimer

from gpmp.windows import InitWindow, LoginWindow
from gpmp.model import Model


log = logging.getLogger(__name__)


class MainController(object):
    window = None

    def __init__(self):
        # Create obligatory Qt context.
        self.app = app = QApplication(sys.argv)
        # This is needed for settings and phonon.
        app.setOrganizationName("Michal Odnous")
        app.setApplicationName("PyGPMP")
        # Initialize application state.
        self._model = Model()

    def start(self):
        log.debug("Starting MainController")
        # Show app splash screen.
        self.window = InitWindow(controller=self)
        self.window.show()
        # Don't block GUI, start after loop runs.
        QTimer.singleShot(200, self.init_session)
        # Enter Qt's main loop.
        return self.app.exec_()

    def init_session(self):
        if self._model.logged_in:
            return
        # Try restoring previous session first.
        if self._model.restore_session():
            return self.show_main_menu()

        # Enforce email/password login.
        LoginWindow(parent=self.window, controller=self,
            callback=lambda: self._model.logged_in and self.show_main_menu()
        ).show()

    def model(self):
        # XXX: This could return some read-only proxy as well.
        return self._model

    # Pass-through methods #
    def login(self, email, password):
        return self._model.login(email, password)

    def show_main_menu(self):
        self.window.show_main_menu()
