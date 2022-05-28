from typing import Dict


class BasePresenter():

    _use_cases: Dict

    def __init__(self, use_cases: Dict):
        self._use_cases = use_cases

    def start(self):
        raise NotImplemented('Not implemented method')