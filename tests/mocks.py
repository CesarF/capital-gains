from app.adapters.repositories.base_repository import BaseRepository


class MockRepository(BaseRepository):

    def clear(self):
        pass

    def set_element(self, element):
        pass

    def get_element(self):
        pass
