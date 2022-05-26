from app.adapters.repositories.base_repository import BaseRepository
from app.domains.account import Account


class AccountRepository(BaseRepository):

    _account: Account

    def __init__(self):
        self.clear()

    def clear(self):
        self._account = Account()

    def set_element(self, element):
        self._account = element

    def get_element(self):
        return self._account
