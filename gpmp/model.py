u"Application state."
import logging
from PyQt4.QtCore import QObject, QSettings, pyqtSignal
from gmusicapi.api import Api


log = logging.getLogger(__name__)


class Model(QObject):
    _logged_in = False
    _TOKENS = ["lsid", "sid", "auth"]
    _playlists = None
    _user = None

    sig_logged_in = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.settings = QSettings()
        self.api = Api()

    def restore(self):
        u"Restore state of the model."
        self.__tokens_login()

    @property
    def logged_in(self):
        return self._logged_in

    @property
    def user(self):
        return self._user

    def read_tokens(self):
        t = {}
        for name in self._TOKENS:
            t[name] = str(self.settings.value("tokens/%s" % name).toString())
        email = self.settings.value("user/email").toString()
        if email:
            self._user = email
        return t

    def store_tokens(self, tokens):
        u"Store session tokens in application's settings."
        if tokens:
            for name in self._TOKENS:
                self.settings.setValue("tokens/%s" % name, tokens[name])
        else:
            log.info("Tried to save empty session tokens")
        self.settings.setValue("user/email", self._user)

    def purge_tokens(self):
        u"Clear stored tokens."
        for name in self._TOKENS:
            self.settings.remove("tokens/%s" % name)
        self.settings.remove("user/email")

    def __tokens_login(self):
        u"Try API initialization with previously acquired tokens."
        t = self.read_tokens()
        # Check tokens are not empty.
        if all(map(t.get, self._TOKENS)):
            try:
                result = self.api.login(tokens=t)
            except RuntimeError:
                result = False
                log.warn("Couldn't login with received tokens")
            if result:
                log.info("Successfully logged in with tokens")
                self.sig_logged_in.emit()
            else:  # Tokens are no longer valid.
                self.purge_tokens()
            self._logged_in = result

    def login(self, email, password):
        u"Initialize API with user's email address and account password."
        # TODO: For manual (E/P) login enable device registration.
        try:
            result = self.api.login(email=email, password=password)
            if result:
                self._logged_in = True
                # TODO: Consider user class.
                self._user = email
                # Remember tokens for the next session.
                self.store_tokens(self.api.session.client.get_tokens())
                # Notify listeners about success.
                self.sig_logged_in.emit()
            return result
        # Wrong credentials generate exception.
        except RuntimeError:
            return False

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
