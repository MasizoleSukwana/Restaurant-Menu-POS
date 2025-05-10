from services import StockService

class MockStockRepo:
    def reduce(self, item): pass
    def below_threshold(self, item): return item == "Tomato"
    def update(self, item_id, quantity): self.updated = (item_id, quantity)

class MockSupplierService:
    def send_restock_request(self, item): pass

def test_reduce_stock_triggers_restock():
    service = StockService(MockStockRepo(), MockSupplierService())
    service.reduce_stock(["Tomato", "Cheese"])

def test_update_stock():
    repo = MockStockRepo()
    service = StockService(repo, MockSupplierService())
    service.update_stock("item123", 50)
    assert repo.updated == ("item123", 50)
