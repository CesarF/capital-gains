class Operation():

    _op_type:str
    _unit_cost:float
    _quantity:int

    def __init__(self, op_type:str, unit_cost:float, quantity:int):
        self._op_type = op_type
        self._unit_cost = unit_cost
        self._quantity = quantity

    def get_op_type(self) -> str:
        return self._op_type

    def set_op_type(self, op_type):
        self._op_type = op_type

    def get_unit_cost(self) -> float:
        return self._unit_cost

    def set_unit_cost(self, unit_cost):
        self._unit_cost = unit_cost

    def get_quantity(self) -> int:
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

    op_type = property(get_op_type, set_op_type)
    unit_cost = property(get_unit_cost, set_unit_cost)
    quantity = property(get_quantity, set_quantity)


def json_to_operation(json_obj:dict) -> Operation:
    return Operation(
        op_type   = json_obj['operation'],
        unit_cost = json_obj['unit-cost'],
        quantity  = json_obj['quantity']
    )

def operation_to_json(operation:Operation) -> dict:
    return {
        'operation': operation.op_type,
        'unit-cost': operation.unit_cost,
        'quantity': operation.quantity
    }