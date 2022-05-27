from typing import Tuple

from app.domains.operation import Operation
from app.domains.account import Account


def calculate_sell_taxes(operation:Operation, account:Account) -> Tuple[int, Account]:
    total_amount = operation.quantity * operation.unit_cost
    if operation.unit_cost < account.weighted_average_price or total_amount <= 20000:
        losses = ((operation.quantity * account.weighted_average_price) - total_amount)
        if losses > 0:
            account.losses = account.losses + losses
        account.current_stock_quantity = account.current_stock_quantity - operation.quantity
        tax = 0
    else:
        losses = account.losses
        profit = ((operation.quantity * operation.unit_cost)
                    - (operation.quantity * account.weighted_average_price)
                        - losses)
        account.losses = 0
        account.current_stock_quantity = account.current_stock_quantity - operation.quantity
        if profit >= 0:
            tax = profit * 0.2
        else:
            tax = 0
            account.losses = - profit
    return tax, account

def process_buy_operation(operation:Operation, account:Account) -> Tuple[int, Account]:
    account.weighted_average_price = (
        ((account.current_stock_quantity * account.current_stock_price) + (operation.quantity * operation.unit_cost))
        /(account.current_stock_quantity + operation.quantity)
    )
    account.current_stock_quantity = account.current_stock_quantity + operation.quantity
    account.current_stock_price = account.weighted_average_price
    return 0, account