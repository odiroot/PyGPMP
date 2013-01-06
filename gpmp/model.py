u"Application state."
import logging

from PyQt4.QtCore import QObject, QSettings
from gmusicapi.api import Api


log = logging.getLogger(__name__)


class SettingsWrapper(object):
    u"Mapping-like wrapper for QSettings."
    def __init__(self):
        self.store = QSettings()

    def __getitem__(self, name):
        return self.store.value(name)

    def __setitem__(self, name, value):
        return self.store.setValue(name, value)

    def __delitem__(self, name):
        return self.store.remove(name)


class SessionMixin(object):
    u"The model part responsible for session operations."
    _logged_in = False
    _TOKENS = ["lsid", "sid", "auth"]

    @property
    def logged_in(self):
        return self._logged_in

    @property
    def email(self):
        if not hasattr(self, "_email"):
            return
        return self._email

    def restore_session(self):
        u"Try API initialization with previously acquired tokens."
        t = self.read_tokens()
        # Check tokens are not empty.
        if not all(map(t.get, self._TOKENS)):
            return False
        # Try logging in with tokens.
        try:
            result = self.api.login(tokens=t)
        except RuntimeError:
            result = False
            log.warn("Couldn't login with received tokens")
        if result:
            log.info("Successfully logged in with tokens")
            self._logged_in = True
        else:  # Tokens are no longer valid.
            self.purge_tokens()
        return result

    def read_tokens(self):
        t = {}
        for name in self._TOKENS:
            t[name] = str(self.settings["tokens/%s" % name].toString())
        email = self.settings["user/email"].toString()
        if email:
            self._email = email
        return t

    def store_tokens(self, tokens):
        u"Store session tokens in application's settings."
        if tokens:
            for name in self._TOKENS:
                self.settings["tokens/%s" % name] = tokens[name]
        else:
            log.info("Tried to save empty session tokens")
        self.settings["user/email"] = self._email

    def purge_tokens(self):
        u"Clear stored tokens."
        for name in self._TOKENS:
            del self.settings["tokens/%s" % name]
        del self.settings["user/email"]

    def login(self, email, password):
        u"Initialize API with user's email address and account password."
        try:
            result = self.api.login(email=email, password=password)
            if result:
                self._logged_in = True
                # TODO: Consider user class.
                self._email = email
                # Remember tokens for the next session.
                self.store_tokens(self.api.session.client.get_tokens())
            return result
        except RuntimeError:  # Wrong credentials generate exception.
            return False


class PlaylistMixin(object):
    def get_playlist_ids(self, kind):
        # For validity sake.
        assert kind in ["auto", "user"], "Wrong playlist kind"
        # Ignore unwanted kind.
        kwargs = dict(auto=False, user=False)
        kwargs[kind] = True
        result = self.api.get_all_playlist_ids(**kwargs)
        return result[kind]

    def get_playlist_songs(self, playlist_id):
        return self.api.get_playlist_songs(playlist_id)

    def get_stream_url(self, song_id):
        return self.api.get_stream_url(song_id)


class QueueMixin(object):
    u"Acts as a 'now playing' playlist."
    _queue = []
    _current_song = None

    def queue_song(self, song_id, title):
        u"Adds song to internal playlist."
        self._queue.append((song_id, title))

    def get_queue_current(self):
        return self._current_song

    def get_queue_next(self):
        u"Returns next (in order) song to be played."
        if not self._queue:  # Empty playlist.
            return None

        if self._current_song is None:
            return self._queue[0]
        else:
            idx = self._queue.index(self._current_song) + 1
            next = min(idx, len(self._queue) - 1)
            return self._queue[next]

    def get_queue_songs(self):
        u"Returns copy of internal playlist for display."
        return self._queue[:]

    def set_queue_current(self, song_id):
        for (sid, title) in self._queue:
            if sid == song_id:
                self._current_song = (sid, title)
                return  # Prevent fall-through.
        # Fallback to no current song.
        self._current_song = None


class Model(QObject, SessionMixin, PlaylistMixin, QueueMixin):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.settings = SettingsWrapper()
        self.api = Api()
