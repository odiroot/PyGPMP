u"""Entry script for the whole GPMP application."""
import logging
import os
import sys

from PyQt4.QtGui import QApplication

from gpmp.controllers import MainController


def setup_logger():
    if os.environ.get("DEBUG", False):
        # Only for development.
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(level=level)


def main():
    setup_logger()

    # Create obligatory Qt context.
    app = QApplication(sys.argv)
    # This is needed for settings and phonon.
    app.setOrganizationName("Michal Odnous")
    app.setApplicationName("PyGPMP")

    # Launch main application controller.
    MainController().start()

    # Enter Qt's main loop.
    return app.exec_()


if __name__ == "__main__":
    main()
