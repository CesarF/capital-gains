from unittest import TestCase
from faker import Faker

from app.domains.account import Account


fake = Faker()

class TestAccount(TestCase):

    def setUp(self):
        self._current_stock_price = fake.random_number()
        self._current_stock_quantity = fake.random_number()
        self._account = Account(self._current_stock_quantity, self._current_stock_price)

    def test_get_current_stock_quantity(self):
        self.assertEqual(self._account.current_stock_quantity, self._current_stock_quantity)

    def test_set_weighted_average_price(self):
        new_stock_price = fake.random_number()
        self._account.weighted_average_price = new_stock_price
        self.assertEqual(new_stock_price, self._account.weighted_average_price)

    def test_set_current_stock_quantity(self):
        new_stock_price = fake.random_number()
        self._account.current_stock_price = new_stock_price
        self.assertEqual(new_stock_price, self._account.current_stock_price)