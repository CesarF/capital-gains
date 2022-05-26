class BasePresenter():

    _use_cases: dict

    def __init__(self, use_cases: dict):
        self._use_cases = use_cases

    def start(self):
        raise NotImplemented('Not implemented method')