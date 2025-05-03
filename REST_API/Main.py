from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="Masi Restaurant POS System")

# ---------------------------
# Data Models
# ---------------------------

class MenuItem(BaseModel):
    id: str
    name: str
    description: str
    price: float
    available: bool

class OrderItem(BaseModel):
    menu_item_id: str
    customizations: Optional[str] = None

class Order(BaseModel):
    id: str
    items: List[OrderItem]
    status: str
    is_offline: bool = False

class Payment(BaseModel):
    order_id: str
    method: str
    amount: float

# ---------------------------
# In-Memory Data
# ---------------------------

menu_db: List[MenuItem] = []
order_db: List[Order] = []
stock_levels = {}
offline_order_queue: List[Order] = []

# ---------------------------
# API Endpoints
# ---------------------------

@app.get("/api/menu", response_model=List[MenuItem])
def get_available_menu():
    return [item for item in menu_db if item.available]

@app.post("/api/menu", response_model=MenuItem)
def add_menu_item(item: MenuItem):
    menu_db.append(item)
    return item

@app.post("/api/orders", response_model=Order)
def place_order(items: List[OrderItem], is_offline: bool = False):
    if not items:
        raise HTTPException(status_code=400, detail="At least one item is required.")
    order = Order(id=str(uuid4()), items=items, status="Pending", is_offline=is_offline)
    if is_offline:
        offline_order_queue.append(order)
    else:
        order_db.append(order)
    return order

@app.put("/api/orders/{order_id}/status")
def update_order_status(order_id: str, status: str):
    for order in order_db:
        if order.id == order_id:
            order.status = status
            return {"message": "Order status updated."}
    raise HTTPException(status_code=404, detail="Order not found.")

@app.post("/api/payment")
def process_payment(payment: Payment):
    for order in order_db:
        if order.id == payment.order_id:
            if order.status in ["Cancelled", "Paid"]:
                raise HTTPException(status_code=400, detail="Invalid order state.")
            order.status = "Paid"
            return {"message": "Payment successful. Receipt sent."}
    raise HTTPException(status_code=404, detail="Order not found.")

@app.get("/api/offline/orders")
def get_offline_orders():
    return offline_order_queue

@app.post("/api/sync/offline")
def sync_offline_orders():
    synced = 0
    for order in offline_order_queue:
        order.is_offline = False
        order_db.append(order)
        synced += 1
    offline_order_queue.clear()
    return {"message": f"{synced} orders synced."}

@app.post("/api/stock/reduce")
def reduce_stock(menu_item_id: str, quantity: int):
    if menu_item_id in stock_levels:
        stock_levels[menu_item_id] -= quantity
        return {"message": "Stock reduced"}
    raise HTTPException(status_code=404, detail="Menu item not found in stock")

@app.get("/api/stock")
def view_stock():
    return stock_levels

@app.post("/api/stock/replenish")
def replenish_stock(menu_item_id: str, quantity: int):
    stock_levels[menu_item_id] = stock_levels.get(menu_item_id, 0) + quantity
    return {"message": "Stock replenished"}
