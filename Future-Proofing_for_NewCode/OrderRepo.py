from abc import ABC, abstractmethod
import uuid
import json
import os

# --- Domain Entities ---
class Order:
    def __init__(self, items, customer_id, order_type="dine-in"):
        self.order_id = str(uuid.uuid4())
        self.items = items
        self.customer_id = customer_id
        self.status = "Received"
        self.order_type = order_type

class Customer:
    def __init__(self, name, contact):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.contact = contact

class MenuItem:
    def __init__(self, name, price):
        self.item_id = str(uuid.uuid4())
        self.name = name
        self.price = price

# --- Abstract Repository Interfaces ---
class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order: Order): pass

    @abstractmethod
    def get_order(self, order_id: str): pass

    @abstractmethod
    def list_orders(self): pass

# --- In-Memory Repository ---
class InMemoryOrderRepository(OrderRepository):
    def __init__(self): self.storage = {}

    def save_order(self, order):
        self.storage[order.order_id] = order
        return order.order_id

    def get_order(self, order_id):
        return self.storage.get(order_id)

    def list_orders(self):
        return list(self.storage.values())

# --- File System Repository ---
class FileSystemOrderRepository(OrderRepository):
    def __init__(self, directory="orders"):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def _get_path(self, order_id):
        return os.path.join(self.directory, f"{order_id}.json")

    def save_order(self, order):
        path = self._get_path(order.order_id)
        with open(path, "w") as f:
            json.dump(order.__dict__, f)
        return order.order_id

    def get_order(self, order_id):
        path = self._get_path(order_id)
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            data = json.load(f)
            return Order(**data)

    def list_orders(self):
        orders = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".json"):
                with open(os.path.join(self.directory, filename), "r") as f:
                    data = json.load(f)
                    orders.append(Order(**data))
        return orders

# --- Repository Factory ---
class RepositoryFactory:
    @staticmethod
    def get_order_repository(storage_type: str) -> OrderRepository:
        if storage_type == "memory":
            return InMemoryOrderRepository()
        elif storage_type == "filesystem":
            return FileSystemOrderRepository()
        raise ValueError(f"Unsupported storage type: {storage_type}")

# --- Example Usage ---
if __name__ == "__main__":
    # Change storage type to "memory" or "filesystem"
    repo = RepositoryFactory.get_order_repository("filesystem")

    # Create and save order
    order = Order(["Burger", "Fries"], customer_id="cust123", order_type="takeaway")
    repo.save_order(order)

    # List orders
    print("\n--- Orders ---")
    for o in repo.list_orders():
        print(vars(o))
