import logging
from PyQt4.QtCore import QTimer, QCoreApplication
from PyQt4.phonon import Phonon

from gpmp.windows import (InitWindow, LoginWindow, MenuWindow, ListingWindow,
    PlaylistWindow)
from gpmp.model import Model


log = logging.getLogger(__name__)


class MainController(object):
    windows = set()

    def __init__(self):
        # Initialize application state.
        self._model = Model()
        self._player = Player(model=self._model)

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

    def clean_window(self, window):
        u"Remove reference to a window so it can be GC'ed"
        if window in self.windows:
            self.windows.remove(window)

    def model(self):
        # XXX: This could return some read-only proxy as well.
        return self._model

    def show_main_menu(self):
        self.display_window(MenuWindow, controller=self)
        # Scrape splash screen.
        try:
            self.init_window.close()
        except AttributeError:
            pass

    # Pass-through methods #
    def login(self, email, password):
        return self._model.login(email, password)

    def quit(self):
        # Just quit the application the Qt's way.
        QCoreApplication.instance().quit()

    ## Playlists ## TODO: move to other controller?

    def show_auto_playlists(self, parent=None):
        self.display_window(ListingWindow, kind="auto", parent=parent,
            controller=self)

    def show_playlist(self, playlist_id, parent=None):
        self.display_window(PlaylistWindow, playlist_id=playlist_id,
            parent=parent, controller=self)

    def play_song(self, song_id, title):
        self._player.play_song(song_id, title)


class Player(object):
    def __init__(self, model):
        self.model = model
        # Media playing interface provided by Phonon stack.
        self.media = Phonon.createPlayer(Phonon.MusicCategory)

    def play_song(self, song_id, title):
        u"""Plays song by external request (not from current queue)
            Song is first added to 'now playing' list.
        """
        self.model.queue.append(song_id, title)

        # Start playback if no song is currently playing.
        if self.media.state() != Phonon.PlayingState:
            next = self.model.queue.get_next()
            if not next:  # Queue is empty.
                return

            self._load_source(next[0])
            self.media.play()

    def _load_source(self, song_id):
        u"Gets song url from id, provides as a source for media player."
        url = self.model.get_stream_url(song_id)
        self.media.setCurrentSource(Phonon.MediaSource(url))
