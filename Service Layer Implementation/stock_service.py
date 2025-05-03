class StockService:
    def __init__(self, stock_repository, supplier_service):
        self.stock_repository = stock_repository
        self.supplier_service = supplier_service

    def reduce_stock(self, items):
        for item in items:
            self.stock_repository.reduce(item)
            if self.stock_repository.below_threshold(item):
                self.supplier_service.send_restock_request(item)

    def update_stock(self, item_id, quantity):
        self.stock_repository.update(item_id, quantity)
