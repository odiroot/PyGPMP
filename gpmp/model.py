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


class Model(QObject, SessionMixin):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.settings = SettingsWrapper()
        self.api = Api()


## OLD CODE BELOW ##
class OldModel(QObject):
    _playlists = None

    @property
    def user(self):
        return self._email

    def fetch_playlists(self, force=False):
        # TODO: Local storage caching.
        # TODO: Wrap playlists in objects, lazily fetch songs info.
        if not self._playlists or force:
            self._playlists = self.api.get_all_playlist_ids()

    def __get_playlist_group(self, name):
        # Fetch playlist groups from server.
        self.fetch_playlists()
        if not self._playlists:
            return None
        return self._playlists[name]

    def auto_playlists(self):
        return self.__get_playlist_group("auto")

    def instant_mixes(self):
        return self.__get_playlist_group("instant")

    def custom_playlists(self):
        return self.__get_playlist_group("user")

    def get_playlist_songs(self, name):
        return self.api.get_playlist_songs(name)
