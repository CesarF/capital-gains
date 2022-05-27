class Account():

    _current_stock_quantity: int
    _current_stock_price: float
    _weighted_average_price: float
    losses: float

    def __init__(self, current_stock_quantity:int = 0, current_stock_price:float = 0):
        self._current_stock_quantity = current_stock_quantity
        self._current_stock_price = current_stock_price
        self._weighted_average_price = 0
        self.losses = 0
    
    def get_current_stock_quantity(self) -> int:
        return self._current_stock_quantity

    def set_current_stock_quantity(self, current_stock_quantity:int):
        self._current_stock_quantity = current_stock_quantity
    
    def get_current_stock_price(self) -> float:
        return self._current_stock_price

    def set_current_stock_price(self, current_stock_price:float):
        self._current_stock_price = current_stock_price

    def get_weighted_average_price(self) -> float:
        return self._weighted_average_price

    def set_weighted_average_price(self, weighted_average_price:float):
        self._weighted_average_price = weighted_average_price

    current_stock_quantity = property(get_current_stock_quantity, set_current_stock_quantity)
    current_stock_price = property(get_current_stock_price, set_current_stock_price)
    weighted_average_price = property(get_weighted_average_price, set_weighted_average_price)