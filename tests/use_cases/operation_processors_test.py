from unittest import TestCase
from faker import Faker

from app.domains.account import Account
from app.domains.operation import Operation
from app.use_cases.operation_processors import calculate_sell_taxes, process_buy_operation


fake = Faker()

class TestOperationProcessors(TestCase):

    def test_process_buy_operation__first_time(self):
        unit_cost = fake.random_number()
        quantity = fake.random_number()
        operation = Operation(op_type = 'buy', unit_cost = unit_cost, quantity = quantity)
        account = Account()
        tax, account = process_buy_operation(operation, account)

        self.assertEqual(0, tax)
        self.assertEqual(quantity, account.current_stock_quantity)
        # First operation wap == operation unit cost
        self.assertEqual(unit_cost, account.weighted_average_price)
        self.assertEqual(0, account.losses)

    def test_process_buy_operation__second_time(self):
        unit_cost = fake.random_number()
        quantity = fake.random_number()
        second_unit_cost = fake.random_number()
        second_quantity = fake.random_number()
        second_weighted_average_price = round(((quantity * unit_cost) + (second_quantity * second_unit_cost)) / (quantity + second_quantity), 2)
        operation = Operation(op_type = 'buy', unit_cost = unit_cost, quantity = quantity)
        second_operation = Operation(op_type = 'buy', unit_cost = second_unit_cost, quantity = second_quantity)
        account = Account()
        _, account = process_buy_operation(operation, account)
        tax, account = process_buy_operation(second_operation, account)

        self.assertEqual(0, tax)
        self.assertEqual(quantity + second_quantity, account.current_stock_quantity)
        self.assertEqual(second_weighted_average_price, account.weighted_average_price)
        self.assertEqual(0, account.losses)

    def test_calculate_sell_taxes__with_profit(self):
        # Set a minimum of 6 digits to avoid a total amount < 20000 
        current_stock_price = fake.random_number(digits = 6)
        current_stock_quantity = fake.random_number(digits = 6)
        account = Account(current_stock_quantity = current_stock_quantity, current_stock_price = current_stock_price)
        # Forcing a profit: selling half stock by a major price
        ope_quantity = int(current_stock_quantity / 2)
        ope_unit_cost = current_stock_price + fake.random_number()
        operation = Operation( op_type = 'sell', unit_cost = ope_unit_cost, quantity = ope_quantity )
        profit = (ope_quantity * ope_unit_cost) - (ope_quantity * current_stock_price)
        tax, account = calculate_sell_taxes(operation, account)

        self.assertEqual(profit * 0.2, tax)
        self.assertEqual(0, account.losses)
        self.assertEqual(current_stock_quantity - ope_quantity, account.current_stock_quantity)

    def test_calculate_sell_taxes__less_price(self):
        # Set a minimum of 6 digits to avoid a total amount < 20000 
        current_stock_price = fake.random_number(digits = 6)
        current_stock_quantity = fake.random_number(digits = 6)
        account = Account(
            current_stock_quantity = current_stock_quantity,
            current_stock_price = current_stock_price
        )
        current_losses = fake.random_number()
        account.losses = current_losses
        # Forcing a loss: selling half stock by a less price
        ope_quantity = int(current_stock_quantity / 2)
        ope_unit_cost = current_stock_price - fake.random_number(digits = 2)
        operation = Operation( op_type = 'sell', unit_cost = ope_unit_cost, quantity = ope_quantity)
        losses = (ope_quantity * current_stock_price) + current_losses - (ope_quantity * ope_unit_cost)
        tax, account = calculate_sell_taxes(operation, account)

        self.assertGreater(losses, 0)
        self.assertEqual(0, tax)
        self.assertEqual(losses, account.losses)
        self.assertEqual(current_stock_quantity - ope_quantity, account.current_stock_quantity)

    def test_calculate_sell_taxes__less_20000_no_losses(self):
        current_stock_price = fake.random_number(digits = 2)
        current_stock_quantity = fake.random_number(digits = 2)
        account = Account(current_stock_quantity = current_stock_quantity, current_stock_price = current_stock_price)
        # Forcing a profit: selling half stock by a major price
        ope_quantity = int(current_stock_quantity / 2)
        ope_unit_cost = current_stock_price + fake.random_number(digits = 2)
        operation = Operation(op_type = 'sell', unit_cost = ope_unit_cost, quantity = ope_quantity)
        losses = (ope_quantity * current_stock_price) - (ope_quantity * ope_unit_cost)
        tax, account = calculate_sell_taxes(operation, account)

        self.assertLessEqual(ope_quantity * ope_unit_cost, 20000)
        self.assertLessEqual(losses, 0)
        self.assertEqual(0, tax)
        self.assertEqual(0, account.losses)
        self.assertEqual(current_stock_quantity - ope_quantity, account.current_stock_quantity)

    def test_calculate_sell_taxes__less_20000_with_losses(self):
        current_stock_price = fake.random_number(digits = 2)
        current_stock_quantity = fake.random_number(digits = 2)
        account = Account(current_stock_quantity = current_stock_quantity, current_stock_price = current_stock_price)
        # Forcing a profit: selling half stock by a major price
        ope_quantity = int(current_stock_quantity / 2)
        ope_unit_cost = current_stock_price - 1
        operation = Operation(op_type = 'sell', unit_cost = ope_unit_cost, quantity = ope_quantity)
        losses = (ope_quantity * current_stock_price) - (ope_quantity * ope_unit_cost)
        tax, account = calculate_sell_taxes(operation, account)

        self.assertLessEqual(ope_quantity * ope_unit_cost, 20000)
        self.assertGreater(losses, 0)
        self.assertEqual(0, tax)
        self.assertEqual(losses, account.losses)
        self.assertEqual(current_stock_quantity - ope_quantity, account.current_stock_quantity)

    def test_calculate_sell_taxes__profit_with_pass_losses(self):
        # Set a minimum of 6 digits to avoid a total amount < 20000 
        current_stock_price = fake.random_number(digits = 6)
        current_stock_quantity = fake.random_number(digits = 6)
        account = Account(current_stock_quantity = current_stock_quantity, current_stock_price = current_stock_price)
        current_losses = current_stock_price * current_stock_quantity
        account.losses = current_losses
        # Forcing a profit: selling half stock by a major price
        ope_quantity = int(current_stock_quantity / 2)
        ope_unit_cost = current_stock_price + 1
        operation = Operation(op_type = 'sell', unit_cost = ope_unit_cost, quantity = ope_quantity)
        profit = (ope_quantity * current_stock_price) + current_losses - (ope_quantity * ope_unit_cost) 
        tax, account = calculate_sell_taxes(operation, account)

        self.assertEqual(0, tax)
        self.assertEqual(profit, account.losses)
        self.assertEqual(current_stock_quantity - ope_quantity, account.current_stock_quantity)