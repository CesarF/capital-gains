from unittest import TestCase
from faker import Faker

from app.adapters.repositories.account_repository import AccountRepository
from app.domains.account import Account


fake = Faker()

class TestAccountRepository(TestCase):

    def setUp(self):
        self._repo = AccountRepository()

    def test_get_account(self):
        self.assertIsNotNone(self._repo.get_element())
        self.assertIsInstance(self._repo.get_element(), Account)

    def test_set_account(self):
        account = Account()
        self.assertNotEqual(self._repo.get_element(), account)
        self._repo.set_element(account)
        self.assertEqual(self._repo.get_element(), account)

    def test_clear(self):
        account = self._repo.get_element()
        self._repo.clear()
        self.assertNotEqual(self._repo.get_element(), account)
