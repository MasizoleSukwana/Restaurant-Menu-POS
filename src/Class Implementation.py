# -------------------------------
# Entity: Customer
# -------------------------------

class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.orders = []

    def browse_menu(self, menu):
        return menu.display_items()

    def place_order(self, order):
        self.orders.append(order)

# -------------------------------
# Entity: Menu
# -------------------------------

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        return [item.get_description() for item in self.items]

# -------------------------------
# Entity: MenuItem
# -------------------------------

class MenuItem:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def get_description(self):
        return f"{self.name}: {self.description} - ${self.price}"

    def update_price(self, new_price):
        self.price = new_price

# -------------------------------
# Entity: Order
# -------------------------------

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.status = "Pending"

    def add_item(self, item):
        self.items.append(item)

    def update_status(self, new_status):
        self.status = new_status

# -------------------------------
# Entity: Payment
# -------------------------------

class Payment:
    def __init__(self, payment_id, order, amount, method):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.method = method
        self.status = "Unpaid"

    def process_payment(self):
        # Dummy processing logic
        self.status = "Paid"

    def cancel_payment(self):
        self.status = "Cancelled"

# -------------------------------
# Entity: ITAdmin
# -------------------------------

class ITAdmin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def create_user_profile(self, user):
        print(f"Creating profile for {user.name}")

    def resolve_issue(self, issue_description):
        print(f"Resolved: {issue_description}")

# -------------------------------
# Entity: Chef
# -------------------------------

class Chef:
    def __init__(self, chef_id, name):
        self.chef_id = chef_id
        self.name = name

    def view_orders(self, kitchen_display):
        return kitchen_display.get_pending_orders()

    def mark_order_ready(self, order):
        order.update_status("Ready")

# -------------------------------
# Entity: KitchenDisplay
# -------------------------------

class KitchenDisplay:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_pending_orders(self):
        return [order for order in self.orders if order.status == "Pending"]
