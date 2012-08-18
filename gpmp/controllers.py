import logging
from PyQt4.QtCore import QTimer

from gpmp.windows import InitWindow, LoginWindow, MenuWindow
from gpmp.model import Model


log = logging.getLogger(__name__)


class MainController(object):
    windows = set()

    def __init__(self):
        # Initialize application state.
        self._model = Model()

    def start(self):
        log.debug("Starting MainController")
        # Show app splash screen.
        self.init_window = self.display_window(InitWindow, controller=self)
        # Don't block GUI, start after loop runs.
        QTimer.singleShot(100, self.init_session)

    def init_session(self):
        if self._model.logged_in:
            return
        # Try restoring previous session first.
        if self._model.restore_session():
            return self.show_main_menu()

        # Enforce email/password login.
        self.display_window(LoginWindow, controller=self, callback=(lambda:
            self._model.logged_in and self.show_main_menu()))

    def _show(self, window):
        u"Store reference to window object and make window visible."
        self.windows.add(window)
        window.show()

    def display_window(self, cls, *args, **kwargs):
        u"""Instantiates given window class with parameters, uses ``_show``
            to display the window and prevent it from closing due to GC.
        """
        window = cls(*args, **kwargs)
        self._show(window)
        return window

    def model(self):
        # XXX: This could return some read-only proxy as well.
        return self._model

    # Pass-through methods #
    def login(self, email, password):
        return self._model.login(email, password)

    def show_main_menu(self):
        self.display_window(MenuWindow, controller=self)
        # Scrape splash screen.
        try:
            self.init_window.close()
        except AttributeError:
            pass
