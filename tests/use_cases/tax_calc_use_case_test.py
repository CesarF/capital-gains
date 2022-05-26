from unittest import TestCase
from faker import Faker

from app.use_cases.tax_calc_use_case import TaxCalculatorUseCase
from tests.mocks import MockRepository


fake = Faker()

class TestTaxCalculatorUseCase(TestCase):

    def setUp(self):
        self._use_case = TaxCalculatorUseCase(MockRepository)

   # def test_calculate_operation_taxes(self):
