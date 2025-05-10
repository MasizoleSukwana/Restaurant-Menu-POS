import pytest
from services import PaymentService

class MockPaymentGateway:
    def process(self, method, amount): return True

class MockReceiptService:
    def generate(self, order): order["receipt"] = "done"

class MockOrderRepo:
    def get_order(self, order_id):
        return {"status": "Pending"}
    def save_order(self, order): pass

def test_process_payment_success():
    service = PaymentService(MockPaymentGateway(), MockOrderRepo(), MockReceiptService())
    service.process_payment("order123", "card", 100)

def test_payment_already_paid_raises():
    class PaidOrderRepo:
        def get_order(self, order_id): return {"status": "Paid"}
        def save_order(self, order): pass

    service = PaymentService(MockPaymentGateway(), PaidOrderRepo(), MockReceiptService())
    with pytest.raises(Exception, match="already paid"):
        service.process_payment("order123", "card", 100)
