import pytest
from services import OrderService

class MockOrderRepo:
    def create_order(self, customer_id, items, customizations, is_online):
        return {"id": "123", "items": items}
    def get_order(self, order_id):
        return type("Order", (), {"status": "Preparing"})
    def save_order(self, order): pass

class MockStockService:
    def reduce_stock(self, items): pass

class MockKitchenDisplay:
    def show_order(self, order): pass
    def mark_ready(self, order_id): pass

def test_place_order_success():
    service = OrderService(MockOrderRepo(), MockStockService(), MockKitchenDisplay())
    result = service.place_order("cust123", ["Pizza"], {}, True)
    assert result["items"] == ["Pizza"]

def test_place_order_empty_fails():
    service = OrderService(MockOrderRepo(), MockStockService(), MockKitchenDisplay())
    with pytest.raises(ValueError):
        service.place_order("cust123", [], {}, True)
