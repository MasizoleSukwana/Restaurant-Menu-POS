class PaymentService:
    def __init__(self, payment_gateway, order_repository, receipt_service):
        self.payment_gateway = payment_gateway
        self.order_repository = order_repository
        self.receipt_service = receipt_service

    def process_payment(self, order_id, method, amount):
        order = self.order_repository.get_order(order_id)
        if order.status == "Paid":
            raise Exception("Order already paid")

        success = self.payment_gateway.process(method, amount)
        if success:
            order.status = "Paid"
            self.receipt_service.generate(order)
        else:
            raise Exception("Payment failed")
