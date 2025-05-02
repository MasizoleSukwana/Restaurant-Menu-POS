import unittest
from threading import Thread
import copy

# Core classes (normally import these from your modules)

class Order:
    def __init__(self, items): self.items = items
class DineInOrder(Order): pass
class TakeawayOrder(Order): pass
class OrderFactory:
    @staticmethod
    def create_order(order_type, items):
        if order_type == "dine-in": return DineInOrder(items)
        elif order_type == "takeaway": return TakeawayOrder(items)
        else: raise ValueError("Invalid order type")

class CreditCardProcessor:
    def process_payment(self, amount): return f"Processing credit card payment of ${amount}"
class PayPalProcessor:
    def process_payment(self, amount): return f"Processing PayPal payment of ${amount}"
class PaymentFactory:
    @staticmethod
    def get_processor(method):
        if method == "credit": return CreditCardProcessor()
        elif method == "paypal": return PayPalProcessor()
        else: raise ValueError("Invalid payment method")

class Pizza:
    def __init__(self): self.ingredients = []
    def add(self, ingredient): self.ingredients.append(ingredient)
    def describe(self): return ", ".join(self.ingredients)
class PizzaBuilder:
    def __init__(self): self.pizza = Pizza()
    def add_cheese(self): self.pizza.add("cheese"); return self
    def add_pepperoni(self): self.pizza.add("pepperoni"); return self
    def build(self): return self.pizza

class MenuItem:
    def __init__(self, name, price): self.name = name; self.price = price
    def clone(self): return copy.deepcopy(self)

class POSConfigManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(POSConfigManager, cls).__new__(cls)
            cls._instance.config = {}
        return cls._instance
    def set_config(self, key, value): self.config[key] = value
    def get_config(self, key): return self.config.get(key)

# Unit Tests

class TestCreationalPatterns(unittest.TestCase):

    def test_order_factory_valid(self):
        order = OrderFactory.create_order("dine-in", ["burger"])
        self.assertIsInstance(order, DineInOrder)
        self.assertEqual(order.items, ["burger"])

    def test_order_factory_invalid(self):
        with self.assertRaises(ValueError):
            OrderFactory.create_order("invalid", [])

    def test_payment_factory_credit(self):
        processor = PaymentFactory.get_processor("credit")
        self.assertIsInstance(processor, CreditCardProcessor)
        self.assertEqual(processor.process_payment(20), "Processing credit card payment of $20")

    def test_payment_factory_invalid(self):
        with self.assertRaises(ValueError):
            PaymentFactory.get_processor("bitcoin")

    def test_pizza_builder(self):
        pizza = PizzaBuilder().add_cheese().add_pepperoni().build()
        self.assertIn("cheese", pizza.describe())
        self.assertIn("pepperoni", pizza.describe())

    def test_empty_pizza_builder(self):
        pizza = PizzaBuilder().build()
        self.assertEqual(pizza.describe(), "")

    def test_prototype_clone(self):
        item = MenuItem("Pasta", 12.99)
        clone = item.clone()
        self.assertNotEqual(id(item), id(clone))
        self.assertEqual(clone.name, "Pasta")

    def test_singleton_instance(self):
        config1 = POSConfigManager()
        config1.set_config("theme", "dark")
        config2 = POSConfigManager()
        self.assertEqual(config2.get_config("theme"), "dark")

    def test_singleton_thread_safety(self):
        ids = []

        def get_instance_id():
            instance = POSConfigManager()
            ids.append(id(instance))

        threads = [Thread(target=get_instance_id) for _ in range(5)]
        for t in threads: t.start()
        for t in threads: t.join()

        self.assertTrue(all(i == ids[0] for i in ids))

if __name__ == "__main__":
    unittest.main()
