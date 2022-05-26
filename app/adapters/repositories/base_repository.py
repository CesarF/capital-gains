from typing import Any


class BaseRepository():

    def __init__(self):
        self.clear()

    def clear(self):
        raise NotImplemented('Not implemented method')

    def set_element(self, element:Any):
        raise NotImplemented('Not implemented method')

    def get_element(self) -> Any:
        raise NotImplemented('Not implemented method')