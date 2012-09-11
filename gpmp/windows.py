u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication, Qt, pyqtSlot, QObject
from PyQt4.QtGui import QMainWindow, QMessageBox, QPixmap, QListWidgetItem

from gpmp.ui.account_login import Ui_AccountLogin
from gpmp.ui.init import Ui_InitWindow
from gpmp.ui.main_menu import Ui_MainMenu
from gpmp.ui.playlists import Ui_Playlists
from gpmp import get_asset


class StackedWindowMixin(object):
    u"Maemo-specific stacked window."
    def __init__(self):
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        # Dispose of window object after close.
        self.setAttribute(Qt.WA_DeleteOnClose)


class TopWindowBase(QMainWindow, StackedWindowMixin):
    u"Base for all top level windows with app's title and controller."
    def __init__(self, parent=None, controller=None):
        QMainWindow.__init__(self, parent=parent)
        StackedWindowMixin.__init__(self)
        self.controller = controller
        self.setWindowTitle(QCoreApplication.instance().applicationName())


class InitWindow(TopWindowBase, Ui_InitWindow):
    u"Splash screen of some sort."
    def __init__(self, parent=None, controller=None):
        super(InitWindow, self).__init__(parent=parent, controller=controller)
        self.setupUi(self)
        self.lbl_tape.setPixmap(QPixmap(get_asset("media-tape.png")))


class LoginWindow(QMainWindow, StackedWindowMixin, Ui_AccountLogin):
    def __init__(self, parent=None, controller=None, callback=None):
        QMainWindow.__init__(self, parent=parent)
        StackedWindowMixin.__init__(self)
        self.setupUi(self)

        self.controller = controller
        self.callback = callback

    @pyqtSlot()
    def on_btn_login_clicked(self):
        u"Handle login button click: validate fields and try logging in."
        email = self.edt_email.text()
        password = self.edt_password.text()
        if not email or not password:
            return QMessageBox.critical(self, "Missing credentials",
                "You have to provide your email and password.")

        self.btn_login.setEnabled(False)  # Disable during API call.
        if not self.controller.login(email, password):
            self.btn_login.setEnabled(True)
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


class MenuWindow(TopWindowBase, Ui_MainMenu):
    u"Window shown after logon. Shows main application actions."
    def __init__(self, parent=None, controller=None):
        super(MenuWindow, self).__init__(parent=parent, controller=controller)
        # Prepare window contents.
        self.setupUi(self)
        self.lbl_user.setText("Logged in as: %s" % (
            controller.model().email or "unknown"))

    @pyqtSlot()
    def on_btn_quit_clicked(self):
        u"Handle quit button click."
        self.controller.quit()

    @pyqtSlot()
    def on_btn_auto_lists_clicked(self):
        self.controller.show_auto_playlists(self)


class ListingWindow(TopWindowBase, Ui_Playlists):
    def __init__(self, kind, parent=None, controller=None):
        self.kind = kind
        super(ListingWindow, self).__init__(parent=parent,
            controller=controller)
        self.setupUi(self)
        self.setWindowTitle("%s playlists" % kind.capitalize())
        # Fetch playlist listing and update UI.
        self.fill_listing()

    def fill_listing(self):
        playlists = self.controller.model().get_playlist_ids(self.kind)
        self.lst_lists.clear()

        for name, pid in playlists.items():
            item = QListWidgetItem(name, self.lst_lists)
            item.playlist_id = pid  # For click callback.

    @pyqtSlot(QListWidgetItem)
    def on_lst_lists_itemClicked(self, item):
        print "Clicked", item.text()

    def closeEvent(self, event):
        event.accept()
        self.controller.clean_window(self)
