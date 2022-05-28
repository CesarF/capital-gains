from typing import List
from unittest import TestCase
from faker import Faker

from app.domains.account import Account
from app.domains.operation import Operation
from app.use_cases.tax_calc_use_case import TaxCalculatorUseCase

from tests.mocks import MockAccountRepository


fake = Faker()

class TestTaxCalculatorUseCase(TestCase):

    def setUp(self):
        self._tax = fake.random_number()
        self._first_operation = fake.word()
        self._second_operation = fake.word()
        operators = {
            self._first_operation: (lambda a, b: (self._tax, Account())),
            self._second_operation: (lambda a, b: (self._tax, Account()))
        }
        self._use_case = TaxCalculatorUseCase(MockAccountRepository(), operators)
    
    def generate_operation(self, op_type:str) -> Operation:
        return Operation(op_type = op_type, unit_cost = fake.random_number(), quantity = fake.random_number())

    def generate_operation_list(self) -> List[Operation]:
        return [
            self.generate_operation(self._first_operation),
            self.generate_operation(self._second_operation),
            self.generate_operation(self._first_operation),
            self.generate_operation(self._second_operation)
        ]

    def test_calculate_operation_taxes(self):
        operation = self.generate_operation(self._first_operation)
        tax = self._use_case._calculate_operation_taxes(operation)
        self.assertEqual(tax.value, self._tax)

    def test_calculate_taxes(self):
        operations = self.generate_operation_list()
        taxes = self._use_case._calculate_taxes(operations)
        for tax in taxes:
            self.assertEqual(tax.value, self._tax)

    def test_process(self):
        simulations = [self.generate_operation_list(), self.generate_operation_list()]
        results = self._use_case.process(simulations)
        for result in results:
            for tax in result:
                self.assertEqual(tax.value, self._tax)