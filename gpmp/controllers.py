import logging
from PyQt4.QtCore import QTimer, QCoreApplication
from PyQt4.phonon import Phonon

from gpmp.windows import (InitWindow, LoginWindow, MenuWindow, ListingWindow,
    PlaylistWindow, QueueWindow)
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
        self.init_window = self.display_window(InitWindow)
        # Don't block GUI, start after loop runs.
        QTimer.singleShot(100, self.init_session)

    def init_session(self):
        if self._model.logged_in:
            return
        # Try restoring previous session first.
        if self._model.restore_session():
            return self.show_main_menu()

        # Enforce email/password login.
        self.display_window(LoginWindow, callback=(lambda:
            self._model.logged_in and self.show_main_menu()))

    def _show(self, window):
        u"Store reference to window object and make window visible."
        self.windows.add(window)
        window.show()

    def display_window(self, cls, *args, **kwargs):
        u"""Instantiates given window class with parameters, uses ``_show``
            to display the window and prevent it from closing due to GC.
        """
        if "controller" not in kwargs:
            kwargs["controller"] = self
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
        self.display_window(MenuWindow)
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
        self.display_window(ListingWindow, kind="auto", parent=parent)

    def show_user_playlists(self, parent=None):
        self.display_window(ListingWindow, kind="user", parent=parent)

    def show_playlist(self, playlist_id, parent=None):
        self.display_window(PlaylistWindow, playlist_id=playlist_id,
            parent=parent, controller=self._player)

    def show_queue(self, parent=None):
        self.display_window(QueueWindow, parent=parent,
            controller=self._player)


class Player(object):
    def __init__(self, model):
        self._model = model
        # Media playing interface provided by Phonon stack.
        self._media = Phonon.createPlayer(Phonon.MusicCategory)
        # Connect signal to progress song playback.
        self._media.aboutToFinish.connect(self.play_next)

    def model(self):
        return self._model

    @property
    def is_playing(self):
        return self._media.state() == Phonon.PlayingState

    def _load_source(self, song_id):
        u"Gets song url from id, provides as a source for media player."
        url = self._model.get_stream_url(song_id)
        self._media.setCurrentSource(Phonon.MediaSource(url))

    def play_song(self, song_id, title):
        u"""Plays song by external request (not from current queue)
            Song is first added to 'now playing' list.
        """
        log.info("Queuing song %s with id %s" % (title, song_id))
        self._model.queue_song(song_id, title)
        if not self.is_playing:
            self.play_next()

    def play_next(self):
        u"Play next song from the queue."
        next = self._model.get_queue_next()
        if next:
            log.info("Playing song %s with id %s" % next)
            self.play_by_id(next[0])

    def play_by_id(self, song_id):
        u"Immediately play song with a specific id."
        # Notify queue about change.
        self._model.set_queue_current(song_id)

        self._load_source(song_id)
        if not self.is_playing:
            self._media.play()
