from app.adapters.repositories.account_repository import State


class BaseUseCase():

    _state: State

    def __init__(self, state:State):
        self._state = state

    def process(self, simulations:list) -> list:
        raise NotImplemented('Not implemented method')