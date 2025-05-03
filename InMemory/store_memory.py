# In-memory data storage for the restaurant system

# Menu Items: key = item_id, value = dict with name, price, and availability
menu_items = {
    1: {"name": "Margherita Pizza", "price": 8.99, "available": True},
    2: {"name": "Chicken Burger", "price": 6.49, "available": True},
    3: {"name": "Caesar Salad", "price": 5.99, "available": False},
}

# Orders: key = order_id, value = dict with items, total, and status
orders = {
    1001: {"items": [1, 2], "total": 15.48, "status": "Preparing"},
    1002: {"items": [3], "total": 5.99, "status": "Cancelled"},
}

# Tables: key = table_id, value = dict with availability and current order
tables = {
    1: {"available": False, "order_id": 1001},
    2: {"available": True, "order_id": None},
}

# Example functions to manipulate the in-memory data
def add_menu_item(item_id, name, price, available=True):
    menu_items[item_id] = {"name": name, "price": price, "available": available}

def place_order(order_id, item_ids):
    total = sum(menu_items[i]["price"] for i in item_ids if menu_items[i]["available"])
    orders[order_id] = {"items": item_ids, "total": total, "status": "New"}

def update_table_status(table_id, available, order_id=None):
    tables[table_id] = {"available": available, "order_id": order_id}

# Example usage
add_menu_item(4, "Tandoori Chicken", 9.50)
place_order(1003, [1, 4])
update_table_status(3, False, 1003)
