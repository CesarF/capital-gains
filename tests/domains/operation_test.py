from unittest import TestCase
from faker import Faker

from app.domains.operation import Operation, json_to_operation, operation_to_json


fake = Faker()

class TestOperation(TestCase):

    def setUp(self):
        self._op_type = fake.word()
        self._unit_cost = fake.random_number()
        self._quantity = fake.random_number()
        self._operation = Operation(self._op_type, self._unit_cost, self._quantity)

    def test_get_op_type(self):
        self.assertEqual(self._operation.op_type, self._op_type)

    def test_get_unit_cost(self):
        self.assertEqual(self._operation.unit_cost, self._unit_cost)

    def test_get_quantity(self):
        self.assertEqual(self._operation.quantity, self._quantity)

    def test_set_op_type(self):
        new_op_type = fake.word()
        self._operation.op_type = new_op_type
        self.assertEqual(new_op_type, self._operation.op_type)

    def test_set_unit_cost(self):
        new_unit_cost = fake.random_number()
        self._operation.unit_cost = new_unit_cost
        self.assertEqual(new_unit_cost, self._operation.unit_cost)

    def test_set_quantity(self):
        new_quantity = fake.random_number()
        self._operation.quantity = new_quantity
        self.assertEqual(new_quantity, self._operation.quantity)

    def test_json_to_operation(self):
        json_obj = {
            'operation': self._op_type,
            'unit-cost': self._unit_cost,
            'quantity': self._quantity
        }
        operation = json_to_operation(json_obj)
        self.assertIsInstance(operation, Operation)
        self.assertEqual(operation.op_type, self._operation.op_type)
        self.assertEqual(operation.unit_cost, self._operation.unit_cost)
        self.assertEqual(operation.quantity, self._operation.quantity)

    def test_operation_to_json(self):
        json_obj = operation_to_json(self._operation)
        self.assertEqual(json_obj['operation'], self._operation.op_type)
        self.assertEqual(json_obj['unit-cost'], self._operation.unit_cost)
        self.assertEqual(json_obj['quantity'], self._operation.quantity)
