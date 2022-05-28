import copy


class Account():

    _current_stock_quantity: int
    _weighted_average_price: float
    _losses: float

    def __init__(self, current_stock_quantity:int = 0, current_stock_price:float = 0):
        self._current_stock_quantity = current_stock_quantity
        self._weighted_average_price = current_stock_price
        self.losses = 0
    
    def get_current_stock_quantity(self) -> int:
        return self._current_stock_quantity

    def set_current_stock_quantity(self, current_stock_quantity:int):
        self._current_stock_quantity = current_stock_quantity

    def get_weighted_average_price(self) -> float:
        return self._weighted_average_price

    def set_weighted_average_price(self, weighted_average_price:float):
        self._weighted_average_price = weighted_average_price

    def get_losses(self) -> float:
        return self._losses

    def set_losses(self, losses:float):
        self._losses = losses

    def clone(self):
        return copy.deepcopy(self)

    current_stock_quantity = property(get_current_stock_quantity, set_current_stock_quantity)
    weighted_average_price = property(get_weighted_average_price, set_weighted_average_price)
    losses = property(get_losses, set_losses)