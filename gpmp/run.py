u"""Entry script for the whole GPMP application."""
import sys
# TODO: Consider using PySide/PyQt fallback for better compatibility.
from PyQt4.QtGui import QApplication
from gpmp.windows import MainWindow


def main():
    app = QApplication(sys.argv)
    # Inspired by cutetube.
    app.setOrganizationName("Michal Odnous")
    app.setApplicationName("PyGPMP")

    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    main()
