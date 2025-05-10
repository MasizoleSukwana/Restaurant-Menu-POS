from services import SupplierService

class MockSupplier:
    def send_request(self, item): self.sent = item

class MockSupplierRepo:
    def get_supplier_for_item(self, item): return MockSupplier()

class MockStockRepo:
    def update(self, item_id, quantity): self.updated = (item_id, quantity)

def test_send_restock_request():
    service = SupplierService(MockSupplierRepo(), MockStockRepo())
    service.send_restock_request("Tomato")

def test_update_inventory_from_supplier():
    repo = MockStockRepo()
    service = SupplierService(MockSupplierRepo(), repo)
    service.update_inventory_from_supplier("item123", 10)
    assert repo.updated == ("item123", 10)
