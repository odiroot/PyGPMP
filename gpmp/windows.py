u"""This module should contain application window classes."""
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import (QMainWindow, QMessageBox, QLabel, QWidget,
    QListWidgetItem)

from gpmp.ui.account_login import Ui_AccountLogin
from gpmp.ui.main_menu import Ui_Menu
from gpmp.ui.playlists import Ui_Playlists
from gpmp.ui.song_list import Ui_SongList


class StackedWindow(QMainWindow):
    u"Maemo-specific stacked window."
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except:
            pass


class MainWindow(StackedWindow):
    u"""The main application window stub."""
    _central = None

    def __init__(self, parent=None):
        StackedWindow.__init__(self, parent=parent)
        self.setWindowTitle(QCoreApplication.instance().applicationName())


class InitWindow(MainWindow):
    u"Splash screen of some sort."
    def __init__(self, parent=None):
        MainWindow.__init__(self, parent=parent)
        self.setCentralWidget(QLabel("Please wait for application"
            " initialization to finish...", parent=self))


class LoginWindow(StackedWindow, Ui_AccountLogin):
    def __init__(self, parent=None, model=None, callback=None):
        StackedWindow.__init__(self, parent=parent)
        self.setupUi(self)

        self.model = model
        self.callback = callback
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

    def closeEvent(self, event):
        event.accept()
        if self.callback:
            self.callback()


## OLD CODE BELOW ##
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
