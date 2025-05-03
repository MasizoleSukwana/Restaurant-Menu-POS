from abc import ABC, abstractmethod
import uuid

# --- Order Entity ---
class Order:
    def __init__(self, items, customer_id, order_type="dine-in"):
        self.order_id = str(uuid.uuid4())
        self.items = items
        self.customer_id = customer_id
        self.status = "Received"
        self.order_type = order_type

# --- Repository Interface ---
class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order: Order):
        pass

    @abstractmethod
    def get_order(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def list_orders(self) -> list:
        pass

# --- In-Memory Repository Implementation ---
class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.storage = {}

    def save_order(self, order: Order):
        self.storage[order.order_id] = order
        return order.order_id

    def get_order(self, order_id: str):
        return self.storage.get(order_id)

    def list_orders(self):
        return list(self.storage.values())

# --- Simulated Database Repository Implementation ---
class DatabaseOrderRepository(OrderRepository):
    def __init__(self):
        self.db_sim = {}

    def save_order(self, order: Order):
        print(f"Simulating save to DB: {order.order_id}")
        self.db_sim[order.order_id] = order
        return order.order_id

    def get_order(self, order_id: str):
        return self.db_sim.get(order_id)

    def list_orders(self):
        return list(self.db_sim.values())

# --- Factory Pattern for Repository Creation ---
class RepositoryFactory:
    @staticmethod
    def get_order_repository(storage_type: str) -> OrderRepository:
        if storage_type == "memory":
            return InMemoryOrderRepository()
        elif storage_type == "database":
            return DatabaseOrderRepository()
        else:
            raise ValueError("Unsupported storage type")

# --- Usage ---
if __name__ == "__main__":
    # Choose your storage type dynamically
    repo = RepositoryFactory.get_order_repository("memory")

    # Create and store an order
    order = Order(items=["Pizza", "Coke"], customer_id="cust123", order_type="takeaway")
    order_id = repo.save_order(order)

    # Retrieve and display
    fetched = repo.get_order(order_id)
    print(f"Retrieved order: {fetched.__dict__}")
