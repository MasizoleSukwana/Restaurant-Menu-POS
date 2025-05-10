import pytest
from services import MenuService

class MockMenuItem:
    def __init__(self, name, available=True):
        self.name = name
        self._available = available
    def is_available(self):
        return self._available

class MockMenuRepo:
    def get_all_items(self):
        return [MockMenuItem("Pizza", True), MockMenuItem("Pasta", False)]

def test_browse_menu_filters_unavailable_items():
    service = MenuService(MockMenuRepo())
    items = service.browse_menu()
    assert len(items) == 1
    assert items[0].name == "Pizza"
