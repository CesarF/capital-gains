class Tax():

    _value:float

    def __init__(self, value:float):
        self._value = value

    def get_value(self) -> float:
        return self._value

    value = property(get_value, None)

def tax_to_json(tax:Tax) -> dict:
    return {'tax': tax.value}