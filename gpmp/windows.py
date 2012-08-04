u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication, Qt, QTimer
from PyQt4.QtGui import (QMainWindow, QMessageBox, QLabel, QWidget,
    QListWidgetItem)

from gpmp.ui.account_login import Ui_AccountLogin
from gpmp.ui.main_menu import Ui_Menu
from gpmp.ui.playlists import Ui_Playlists
from gpmp.ui.song_list import Ui_SongList
from gpmp.model import Model


class MainWindow(QMainWindow):
    u"""The main window after app is launched."""
    _central = None

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle(QCoreApplication.instance().applicationName())
        # All windows will communicate using single model.
        self.model = Model(parent=self)
        # Try working in Maemo-specific stacked window mode.
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        # Show main window and proceed with usual behavior.
        self.show()
        self.__switch_central(QLabel("Please wait for application"
            " initialization to finish...", parent=self))
        # Don't block the main window.
        QTimer.singleShot(200, self.run)

    def __switch_central(self, widget):
        u"Clean previous and attach new central window widget."
        self.setCentralWidget(None)
        if self._central:
            self._central.deleteLater()
        self._central = widget
        self.setCentralWidget(widget)

    def run(self):
        u"Prepare application model, pass control to other windows."
        # Initialize model.
        self.model.sig_logged_in.connect(self.show_menu)
        self.model.restore()
        # Open log in window if necessary.
        if not self.model.logged_in:
            self.handle_login()

    def handle_login(self):
        u"Allow user to log in with email and password."
        login_window = LoginWindow(parent=self, model=self.model)
        login_window.show()

    def show_menu(self):
        self.__switch_central(MainMenu(parent=self, model=self.model))


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


class MainMenu(QWidget, Ui_Menu):
    def __init__(self, parent=None, model=None):
        QWidget.__init__(self, parent)
        self.model = model
        self.setupUi(self)
        # Connect signals.
        # TODO: Some cleaning in model before application quits.
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_playlists.clicked.connect(self.playlists_clicked)
        # Display info about logged in user.
        if self.model.user:
            self.lbl_user.setText("Logged in as: %s" % self.model.user)
        else:
            self.lbl_user.setText("Logged in as: unknown")

    def playlists_clicked(self):
        PlaylistsWindow(parent=self, model=self.model).show()


class PlaylistsWindow(QMainWindow, Ui_Playlists):
    def __init__(self, parent=None, model=None):
        QMainWindow.__init__(self, parent)
        self.model = model
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        self.setupUi(self)
        self.load()

    def load(self):
        self.__show_playlists_group(self.model.auto_playlists(), self.lst_auto)
        self.__show_playlists_group(self.model.instant_mixes(),
            self.lst_instant)
        self.__show_playlists_group(self.model.custom_playlists(),
            self.lst_custom)

    def __show_playlists_group(self, group, widget):
        u"Display single playlists group in a QListWidget."
        for label, name in group.items():
            item = QListWidgetItem(label, widget)
            item.name = name
        widget.itemClicked.connect(self.playlist_clicked)

    def playlist_clicked(self, item):
        SongListWindow(playlist=item.name, parent=self,
            model=self.model).show()


class SongListWindow(QMainWindow, Ui_SongList):
    def __init__(self, playlist, parent=None, model=None):
        self.playlist = playlist
        QMainWindow.__init__(self, parent)
        self.model = model
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass
        self.setupUi(self)
        self.setWindowTitle("Songs in: %s" % playlist)

        self.load()

    def load(self):
        songs = self.model.get_playlist_songs(self.playlist)
        for sd in songs:  # Loop over song dicts.
            text = "%(artist)s - %(title)s" % sd
            item = QListWidgetItem(text, self.list)
            item.song_id = sd["id"]
