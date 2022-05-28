from typing import List
from app.adapters.presenters.base_presenter import BasePresenter
from app.adapters.repositories.base_repository import BaseRepository
from app.use_cases.base_use_case import BaseUseCase


class MockTaxCalculatorUseCase(BaseUseCase):

    def process(self, simulations: List) -> List:
        return []


class MockAccountRepository(BaseRepository):

    def clear(self):
        pass

    def set_element(self, element):
        pass

    def get_element(self):
        pass
