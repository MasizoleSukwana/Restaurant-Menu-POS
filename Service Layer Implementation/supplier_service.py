class SupplierService:
    def __init__(self, supplier_repository, stock_repository):
        self.supplier_repository = supplier_repository
        self.stock_repository = stock_repository

    def send_restock_request(self, item):
        supplier = self.supplier_repository.get_supplier_for_item(item)
        supplier.send_request(item)

    def update_inventory_from_supplier(self, item_id, quantity):
        self.stock_repository.update(item_id, quantity)
