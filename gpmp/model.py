u"Application state."
import logging
from PyQt4.QtCore import QSettings
from gmusicapi.api import Api


log = logging.getLogger(__name__)


class Model(object):
    logged_in = False
    _TOKENS = ["lsid", "sid", "auth"]

    def __init__(self):
        self.settings = QSettings()
        self.api = Api()

    def restore(self):
        u"Restore state of the model."
        self.__tokens_login()

    def read_tokens(self):
        t = {}
        for name in self._TOKENS:
            t[name] = str(self.settings.value("tokens/%s" % name).toString())
        return t

    def store_tokens(self, tokens):
        u"Store session tokens in application's settings."
        if tokens:
            for name in self._TOKENS:
                self.settings.setValue("tokens/%s" % name, tokens[name])
        else:
            log.info("Tried to save empty session tokens")

    def purge_tokens(self):
        u"Clear stored tokens."

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
            else:  # Tokens are no longer valid.
                self.__purge_tokens()
            self.logged_in = result

    def login(self, email, password):
        u"Initialize API with user's email address and account password."
        # TODO: For manual (E/P) login enable device registration.
        try:
            result = self.api.login(email=email, password=password)
            if result:
                self.logged_in = True
                # Remember tokens for the next session.
                self.store_tokens(self.api.session.client.get_tokens())
            return result
        # Wrong credentials generate exception.
        except RuntimeError:
            return False
