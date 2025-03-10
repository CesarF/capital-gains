from typing import List

from app.domains.operation import Operation
from app.domains.tax import Tax
from app.use_cases.base_use_case import BaseUseCase


class TaxCalculatorUseCase(BaseUseCase):

    def _calculate_operation_taxes(self, operation:Operation) -> Tax:
        tax, account = self._processors.get(operation.op_type)(operation, self._repo.get_element())
        self._repo.set_element(account)
        return Tax(value = tax)

    def _calculate_taxes(self, operations:List[Operation]) -> List[Tax]:
        self._repo.clear()
        taxes = [self._calculate_operation_taxes(operation) for operation in operations]
        return taxes

    def process(self, simulations:List) -> List:
        return [self._calculate_taxes(operations) for operations in simulations]