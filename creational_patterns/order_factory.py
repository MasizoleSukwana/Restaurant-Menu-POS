class Order:
    def __init__(self, items):
        self.items = items

    def prepare(self):
        return f"Preparing order with items: {', '.join(self.items)}"

class DineInOrder(Order):
    def prepare(self):
        return f"Dine-in order: {super().prepare()}"

class TakeawayOrder(Order):
    def prepare(self):
        return f"Takeaway order: {super().prepare()}"

class OrderFactory:
    @staticmethod
    def create_order(order_type, items):
        if order_type == "dine-in":
            return DineInOrder(items)
        elif order_type == "takeaway":
            return TakeawayOrder(items)
        else:
            raise ValueError("Invalid order type")
