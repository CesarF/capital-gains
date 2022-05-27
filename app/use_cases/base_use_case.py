from typing import Dict

from app.adapters.repositories.base_repository import BaseRepository


class BaseUseCase():

    _repo: BaseRepository
    _processors: Dict

    def __init__(self, repo:BaseRepository, processors:Dict = None):
        self._repo = repo
        self._processors = processors

    def process(self, simulations:list) -> list:
        raise NotImplemented('Not implemented method')