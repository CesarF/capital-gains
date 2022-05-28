from typing import Tuple

from app.domains.operation import Operation
from app.domains.account import Account


def calculate_sell_taxes(operation:Operation, account:Account) -> Tuple[float, Account]:
    # Create a new account to avoid side effects
    new_account = account.clone()
    total_amount = operation.quantity * operation.unit_cost
    # In case no taxes
    if operation.unit_cost < new_account.weighted_average_price or total_amount <= 20000:
        losses = ((operation.quantity * account.weighted_average_price) - total_amount)
        if losses > 0:
            # If there are losses, they must be accumulated
            new_account.losses = new_account.losses + losses
        # Discount sold stock from account
        new_account.current_stock_quantity = new_account.current_stock_quantity - operation.quantity
        tax = 0
    else:
        # Take into account past losses
        profit = ((operation.quantity * operation.unit_cost)
                    - (operation.quantity * new_account.weighted_average_price)
                        - new_account.losses)
        # Discount sold stock from account
        new_account.current_stock_quantity = new_account.current_stock_quantity - operation.quantity
        if profit >= 0:
            # If there is profit clear losses
            new_account.losses = 0
            tax = profit * 0.2
        else:
            # If there is not profit, that value is the new losses
            tax = 0
            new_account.losses = - profit
    return tax, new_account

def process_buy_operation(operation:Operation, account:Account) -> Tuple[float, Account]:
    # Create a new account to avoid side effects
    new_account = account.clone()
    new_account.weighted_average_price = round(
        ((new_account.current_stock_quantity * new_account.weighted_average_price) + (operation.quantity * operation.unit_cost))
        /(new_account.current_stock_quantity + operation.quantity)
    , 2)
    new_account.current_stock_quantity = new_account.current_stock_quantity + operation.quantity
    return 0, new_account