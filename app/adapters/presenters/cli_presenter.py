import sys, json
from app.domains.operation import Operation

from presenters.base_presenter import BasePresenter
from use_cases.base_use_case import BaseOperationUseCase


class CliPresenter(BasePresenter):

    _lines: list

    def start(self):
        self._lines = []
        for line in sys.stdin:
            if '' == line.rstrip():
                break
            json_list = json.loads(line)
            #TODO
            self._lines.append(map(lambda ope: self._obj_to_operation(ope),json_list))
        use_case = self._use_cases[BaseOperationUseCase]
        result = use_case.process(self._lines)
        print(result)