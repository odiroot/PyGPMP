import logging
import sys
from PyQt4.QtGui import QApplication

from gpmp.windows import InitWindow


log = logging.getLogger(__name__)


class MainController(object):
    def __init__(self):
        # Create obligatory Qt context.
        self.app = app = QApplication(sys.argv)
        # This is needed for settings and phonon.
        app.setOrganizationName("Michal Odnous")
        app.setApplicationName("PyGPMP")

    def start(self):
        log.debug("Starting MainController")
        window = InitWindow()
        window.show()

        # Enter Qt's main loop.
        return self.app.exec_()
