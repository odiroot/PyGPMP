u"""Entry script for the whole GPMP application."""
import logging
import sys
# TODO: Consider using PySide/PyQt fallback for better compatibility.
from PyQt4.QtGui import QApplication
from gpmp.windows import MainWindow


# Only for development.
logging.basicConfig(level=logging.DEBUG)


def main():
    app = QApplication(sys.argv)
    # Inspired by cutetube.
    app.setOrganizationName("Michal Odnous")
    app.setApplicationName("PyGPMP")

    window = MainWindow()
    return app.exec_()


if __name__ == "__main__":
    main()
