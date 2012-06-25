u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QMainWindow


class MainWindow(QMainWindow):
    u"""The main window after app is launched."""
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # TODO: Ui from designer, inheritance
        # self.setupUi()
        # TODO: Model like in hsoft/guiskel
        self.setWindowTitle(QCoreApplication.instance().applicationName()) 
