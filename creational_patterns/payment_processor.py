from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

class PaymentFactory:
    @staticmethod
    def get_processor(method):
        if method == "credit":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Invalid payment method")
