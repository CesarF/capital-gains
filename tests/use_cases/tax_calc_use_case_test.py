from unittest import TestCase
from faker import Faker

from app.adapters.repositories.account_repository import AccountRepository
from app.domains.operation import Operation
from app.use_cases.operation_processors import calculate_sell_taxes, process_buy_operation
from app.use_cases.tax_calc_use_case import TaxCalculatorUseCase
from tests.mocks import MockAccountRepository

'''
fake = Faker()

class TestTaxCalculatorUseCase(TestCase):

    def setUp(self):
        operators = {
            'buy': process_buy_operation,
            'sell': calculate_sell_taxes
        }
        self._use_case = TaxCalculatorUseCase(AccountRepository(), operators)

    def test_calculate_taxes(self):
        operations = [
            Operation(op_type='buy', unit_cost=10, quantity=10000),
            Operation(op_type='sell', unit_cost=50, quantity=10000),
            Operation(op_type='buy', unit_cost=20, quantity=10000),
            Operation(op_type='sell', unit_cost=50, quantity=10000)
        ]
        taxes = self._use_case._calculate_taxes(operations)
        for tax in taxes:
            print(tax.value)
    
'''