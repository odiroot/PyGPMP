u"Application state."
import logging
from PyQt4.QtCore import QObject, QSettings, pyqtSignal
from gmusicapi.api import Api


log = logging.getLogger(__name__)


class Model(QObject):
    _logged_in = False
    _TOKENS = ["lsid", "sid", "auth"]

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
                self.sig_logged_in.emit()
            else:  # Tokens are no longer valid.
                self.__purge_tokens()
            self._logged_in = result

    def login(self, email, password):
        u"Initialize API with user's email address and account password."
        # TODO: For manual (E/P) login enable device registration.
        try:
            result = self.api.login(email=email, password=password)
            if result:
                self._logged_in = True
                # Remember tokens for the next session.
                self.store_tokens(self.api.session.client.get_tokens())
                # Notify listeners about success.
                self.sig_logged_in.emit()
            return result
        # Wrong credentials generate exception.
        except RuntimeError:
            return False
