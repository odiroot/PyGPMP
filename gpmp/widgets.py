from PyQt4.QtGui import QWidget

from gpmp.ui.main_menu import Ui_Menu


class MainMenu(QWidget, Ui_Menu):
    def __init__(self, parent=None, controller=None):
        QWidget.__init__(self, parent)
        self.controller = controller
        self.setupUi(self)
        # Display info about logged in user.
        if controller:
            self.lbl_user.setText("Logged in as: %s" % (
                controller.model().email or "unknown"))
