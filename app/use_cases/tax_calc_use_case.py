from typing import List

from app.domains.operation import Operation
from app.domains.tax import Tax
from app.use_cases.base_use_case import BaseUseCase


class TaxCalculatorUseCase(BaseUseCase):

    def _calculate_operation_taxes(self, operation:Operation) -> Tax:
        pass

    def _calculate_taxes(self, operations:List[Operation]) -> List[Tax]:
        pass

    def process(self, simulations:list) -> list:
        return []