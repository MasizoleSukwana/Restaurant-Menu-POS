class OrderService:
    def __init__(self, order_repository, stock_service, kitchen_display):
        self.order_repository = order_repository
        self.stock_service = stock_service
        self.kitchen_display = kitchen_display

    def place_order(self, customer_id, items, customizations, is_online=True):
        if not items:
            raise ValueError("Cannot place an empty order")

        order = self.order_repository.create_order(customer_id, items, customizations, is_online)
        self.stock_service.reduce_stock(items)

        if is_online:
            self.kitchen_display.show_order(order)

        return order

    def update_order_status(self, order_id, status):
        order = self.order_repository.get_order(order_id)
        order.status = status
        self.order_repository.save_order(order)

        if status == "Ready":
            self.kitchen_display.mark_ready(order_id)
