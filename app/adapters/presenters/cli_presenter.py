import sys, json

from app.domains.operation import json_to_operation
from app.domains.tax import tax_to_json
from app.adapters.presenters.base_presenter import BasePresenter


class CliPresenter(BasePresenter):

    _lines: list

    def start(self):
        self._lines = []
        for line in sys.stdin:
            if '' == line.rstrip():
                break
            json_list = json.loads(line)
            self._lines.append(list(map(lambda ope: json_to_operation(ope),json_list)))
        use_case = self._use_cases['taxes']
        taxes = use_case.process(self._lines)
        for simulation_taxes in taxes:
            for tax in simulation_taxes:
                print(tax_to_json(tax), end=' ')
            print()