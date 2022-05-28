import sys, json

from app.domains.operation import json_to_operation
from app.domains.tax import tax_to_json
from app.adapters.presenters.base_presenter import BasePresenter
from app.use_cases.base_use_case import BaseUseCase


class CliPresenter(BasePresenter):

    def start(self):
        simulations = []
        for input_line in sys.stdin:
            if '' == input_line.rstrip():
                break
            json_line = json.loads(input_line)
            simulations.append([json_to_operation(json_obj) for json_obj in json_line])
        use_case = self._use_cases[BaseUseCase]
        simulations_taxes = use_case.process(simulations)
        for simulation_taxes in simulations_taxes:
            simulation_result = [tax_to_json(tax) for tax in simulation_taxes]
            sys.stdout.write(json.dumps(simulation_result))
            sys.stdout.write('\n')