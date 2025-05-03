from abc import ABC, abstractmethod
import uuid

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

# --- Repository Interfaces ---
class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order: Order): pass

    @abstractmethod
    def get_order(self, order_id: str) -> Order: pass

    @abstractmethod
    def list_orders(self) -> list: pass

class CustomerRepository(ABC):
    @abstractmethod
    def save_customer(self, customer: Customer): pass

    @abstractmethod
    def get_customer(self, customer_id: str) -> Customer: pass

    @abstractmethod
    def list_customers(self) -> list: pass

class MenuRepository(ABC):
    @abstractmethod
    def add_item(self, item: MenuItem): pass

    @abstractmethod
    def get_item(self, item_id: str) -> MenuItem: pass

    @abstractmethod
    def list_items(self) -> list: pass

# --- In-Memory Implementations ---
class InMemoryOrderRepository(OrderRepository):
    def __init__(self): self.storage = {}

    def save_order(self, order: Order):
        self.storage[order.order_id] = order
        return order.order_id

    def get_order(self, order_id: str):
        return self.storage.get(order_id)

    def list_orders(self):
        return list(self.storage.values())

class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self): self.customers = {}

    def save_customer(self, customer: Customer):
        self.customers[customer.customer_id] = customer
        return customer.customer_id

    def get_customer(self, customer_id: str):
        return self.customers.get(customer_id)

    def list_customers(self):
        return list(self.customers.values())

class InMemoryMenuRepository(MenuRepository):
    def __init__(self): self.menu = {}

    def add_item(self, item: MenuItem):
        self.menu[item.item_id] = item
        return item.item_id

    def get_item(self, item_id: str):
        return self.menu.get(item_id)

    def list_items(self):
        return list(self.menu.values())

# --- Simulated Database Repositories ---
class DatabaseOrderRepository(OrderRepository):
    def __init__(self): self.db = {}

    def save_order(self, order: Order):
        print(f"Saving order {order.order_id} to database.")
        self.db[order.order_id] = order
        return order.order_id

    def get_order(self, order_id: str):
        return self.db.get(order_id)

    def list_orders(self):
        return list(self.db.values())

class DatabaseCustomerRepository(CustomerRepository):
    def __init__(self): self.db = {}

    def save_customer(self, customer: Customer):
        print(f"Saving customer {customer.customer_id} to database.")
        self.db[customer.customer_id] = customer
        return customer.customer_id

    def get_customer(self, customer_id: str):
        return self.db.get(customer_id)

    def list_customers(self):
        return list(self.db.values())

class DatabaseMenuRepository(MenuRepository):
    def __init__(self): self.db = {}

    def add_item(self, item: MenuItem):
        print(f"Saving menu item {item.item_id} to database.")
        self.db[item.item_id] = item
        return item.item_id

    def get_item(self, item_id: str):
        return self.db.get(item_id)

    def list_items(self):
        return list(self.db.values())

# --- Repository Factory ---
class RepositoryFactory:
    @staticmethod
    def get_order_repository(storage_type: str) -> OrderRepository:
        if storage_type == "memory":
            return InMemoryOrderRepository()
        elif storage_type == "database":
            return DatabaseOrderRepository()
        raise ValueError("Unsupported storage type")

    @staticmethod
    def get_customer_repository(storage_type: str) -> CustomerRepository:
        if storage_type == "memory":
            return InMemoryCustomerRepository()
        elif storage_type == "database":
            return DatabaseCustomerRepository()
        raise ValueError("Unsupported storage type")

    @staticmethod
    def get_menu_repository(storage_type: str) -> MenuRepository:
        if storage_type == "memory":
            return InMemoryMenuRepository()
        elif storage_type == "database":
            return DatabaseMenuRepository()
        raise ValueError("Unsupported storage type")

# --- Demo Usage ---
if __name__ == "__main__":
    storage = "memory"  # Change to "database" for DB simulation

    order_repo = RepositoryFactory.get_order_repository(storage)
    customer_repo = RepositoryFactory.get_customer_repository(storage)
    menu_repo = RepositoryFactory.get_menu_repository(storage)

    # Add menu item
    pizza = MenuItem("Pizza", 10.99)
    menu_repo.add_item(pizza)

    # Add customer
    customer = Customer("Alice", "1234567890")
    customer_repo.save_customer(customer)

    # Place an order
    order = Order(items=[pizza.name], customer_id=customer.customer_id, order_type="dine-in")
    order_repo.save_order(order)

    # Retrieve data
    print("\n--- Orders ---")
    for o in order_repo.list_orders():
        print(vars(o))

    print("\n--- Customers ---")
    for c in customer_repo.list_customers():
        print(vars(c))

    print("\n--- Menu Items ---")
    for m in menu_repo.list_items():
        print(vars(m))
