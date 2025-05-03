import copy
from threading import Lock
import uuid

# --- In-Memory Datastore ---
restaurant_data = {
    "menu": {},
    "orders": {},
    "payments": {},
    "tables": {},
    "customers": {},
    "config": {}
}

# --- Menu Prototype ---
class MenuItem:
    def __init__(self, name, price, category, allergens=None):
        self.name = name
        self.price = price
        self.category = category
        self.allergens = allergens or []

    def clone(self):
        return copy.deepcopy(self)

# --- Singleton Config ---
class POSConfigManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(POSConfigManager, cls).__new__(cls)
                cls._instance.config = {}
        return cls._instance

    def set_config(self, key, value):
        self.config[key] = value

    def get_config(self, key):
        return self.config.get(key)

# --- Builder Pattern ---
class Pizza:
    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def describe(self):
        return ", ".join(self.ingredients)

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self): self.pizza.add("cheese"); return self
    def add_pepperoni(self): self.pizza.add("pepperoni"); return self
    def add_olives(self): self.pizza.add("olives"); return self
    def build(self): return self.pizza

# --- Factory Pattern for Orders ---
class Order:
    def __init__(self, items, customer_id):
        self.order_id = str(uuid.uuid4())
        self.items = items
        self.customer_id = customer_id
        self.status = "Received"

class DineInOrder(Order): pass
class TakeawayOrder(Order): pass

class OrderFactory:
    @staticmethod
    def create_order(order_type, items, customer_id):
        if order_type == "dine-in":
            return DineInOrder(items, customer_id)
        elif order_type == "takeaway":
            return TakeawayOrder(items, customer_id)
        else:
            raise ValueError("Invalid order type")

# --- Factory Method for Payments ---
class CreditCardProcessor:
    def process_payment(self, amount):
        return f"Credit card payment of ${amount:.2f} processed."

class PayPalProcessor:
    def process_payment(self, amount):
        return f"PayPal payment of ${amount:.2f} processed."

class PaymentFactory:
    @staticmethod
    def get_processor(method):
        if method == "credit":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Invalid payment method")

# --- Populate Menu Items ---
restaurant_data["menu"] = {
    "p1": MenuItem("Cheese Pizza", 8.99, "Pizza", allergens=["dairy"]),
    "p2": MenuItem("Pepperoni Pizza", 9.99, "Pizza"),
    "d1": MenuItem("Chocolate Cake", 4.50, "Dessert", allergens=["gluten", "nuts"]),
}

# --- Sample Order Creation ---
customer_id = "cust001"
order = OrderFactory.create_order("dine-in", ["p1", "d1"], customer_id)
restaurant_data["orders"][order.order_id] = order.__dict__

# --- Payment Processing ---
payment_processor = PaymentFactory.get_processor("credit")
payment_result = payment_processor.process_payment(13.49)
restaurant_data["payments"][order.order_id] = {
    "method": "credit",
    "amount": 13.49,
    "status": "Completed",
    "result": payment_result
}

# --- Add Table & Reservation Info ---
restaurant_data["tables"] = {
    "T1": {"available": False, "customer_id": customer_id},
    "T2": {"available": True, "customer_id": None}
}

# --- Set Configurations via Singleton ---
config = POSConfigManager()
config.set_config("currency", "USD")
restaurant_data["config"] = config.config

# --- Display Final State ---
from pprint import pprint
pprint(restaurant_data)
