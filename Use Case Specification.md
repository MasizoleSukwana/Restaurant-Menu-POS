# Actors and Their Roles in the Restaurant POS System - Specification

## 1. Customer
**Role:** The customer interacts with the system to place orders and complete payments. 
**Relation to the System:** Uses the system to browse the menu, order food, and make payments.
**Use Case Relationships:**
- **Browse Menu**: Customers explore available food options.
- **Place Order**: Customers select and confirm their desired food items.
- **Make Payment**: Customers complete transactions through the integrated payment system.
**Concern Addressed**: Customers do not have to wait for waiters to place orders.

### Use Case Specification:
**1. Use Case Name:** Browse Menu  
**Actor:** Customer  
**Precondition:** System is online, and the menu is available  
**Description:** Customers can view available food and drink options  
**Postcondition:** Menu items are displayed for selection  
**Step-by-Step Flow:**
1. Customer accesses the system
2. System displays menu items
3. Customer browses available options
4. Customer selects desired items

**2. Use Case Name:** Place Order  
**Actor:** Customer  
**Precondition:** Customer has selected items from the menu  
**Description:** Customer places an order for selected menu items  
**Postcondition:** Order is placed and sent to the kitchen display system  
**Step-by-Step Flow:**
1. Customer selects items from the menu
2. Customer confirms order
3. System sends order to the kitchen
4. System displays order confirmation

**3. Use Case Name:** Make Payment  
**Actor:** Customer  
**Precondition:** Order has been placed  
**Description:** Customer completes payment for the order  
**Postcondition:** Payment is processed successfully  
**Step-by-Step Flow:**
1. Customer selects a payment method
2. System processes payment
3. System confirms payment completion

## 2. Kitchen Staff
**Role:** The kitchen staff is responsible for viewing, processing, and updating order statuses.
**Relation to the System:** Uses the kitchen display system to manage orders.
**Use Case Relationships:**
- **View Orders**: Kitchen staff access the order list.
- **Process Orders**: Kitchen staff prepare food items.
- **Update Order Status**: Kitchen staff mark orders as completed or in progress.
**Concern Addressed**: Orders are captured accurately to avoid conflicts with customers.

### Use Case Specification:
**4. Use Case Name:** View Orders  
**Actor:** Kitchen Staff  
**Precondition:** Orders have been placed  
**Description:** Kitchen staff can access the list of orders  
**Postcondition:** Orders are displayed on the kitchen display system  
**Step-by-Step Flow:**
1. Kitchen staff logs into the system
2. System displays incoming orders

**5. Use Case Name:** Process Orders  
**Actor:** Kitchen Staff  
**Precondition:** Orders are visible on the display  
**Description:** Kitchen staff prepares food items  
**Postcondition:** Order is prepared  
**Step-by-Step Flow:**
1. Kitchen staff selects an order to process
2. Kitchen staff prepares food

**6. Use Case Name:** Update Order Status  
**Actor:** Kitchen Staff  
**Precondition:** Order has been processed  
**Description:** Kitchen staff updates the system with order status  
**Postcondition:** Order status is updated  
**Step-by-Step Flow:**
1. Kitchen staff marks order as "Ready"

## 3. Waiter
**Role:** The waiter delivers food to customers and assists with payments.
**Relation to the System:** Uses the system to track ready orders and facilitate payments.
**Use Case Relationships:**
- **View Ready Orders**: Waiters check which orders are ready for collection.
- **Collect & Deliver Orders**: Waiters serve customers with their ordered food.
- **Facilitate Payment**: Waiters assist customers with payment processing if needed.
**Concern Addressed**: The workload is reduced, waiters do not have to run around taking orders and mixing them up due to high volumes of customers.

### Use Case Specification:
**7. Use Case Name:** View Ready Orders  
**Actor:** Waiter  
**Precondition:** Kitchen has marked order as "Ready"  
**Description:** Waiter views orders that are ready for collection  
**Postcondition:** Order details are available for collection  
**Step-by-Step Flow:**
1. Waiter logs into the system
2. System displays ready orders

**8. Use Case Name:** Collect & Deliver Orders  
**Actor:** Waiter  
**Precondition:** Orders are marked as "Ready"  
**Description:** Waiter collects and delivers orders to customers  
**Postcondition:** Order is delivered to the customer  
**Step-by-Step Flow:**
1. Waiter selects an order for collection
2. Waiter delivers order to customer

**9. Use Case Name:** Facilitate Payment  
**Actor:** Waiter  
**Precondition:** Customer requests payment assistance  
**Description:** Waiter assists customers with completing payment  
**Postcondition:** Payment is processed successfully  
**Step-by-Step Flow:**
1. Waiter selects customer's order
2. Waiter helps process payment

## 4. Manager
**10. Use Case Name:** Ensure Orders are Captured Correctly  
**Actor:** Manager  
**Precondition:** System is operational  
**Description:** Manager verifies order accuracy  
**Postcondition:** Orders are correctly placed  

## 5. IT Admin
**11. Use Case Name:** Maintain System Uptime  
**Actor:** IT Admin  
**Precondition:** System is online  
**Description:** IT Admin ensures continuous system operation  
**Postcondition:** System remains functional  

## 6. Finance Institution Rep
**12. Use Case Name:** Assist with Payment Integration  
**Actor:** Finance Institution Rep  
**Precondition:** Payment system integration required  
**Description:** Assists in setting up payment processing  
**Postcondition:** Payments are successfully processed  

## 7. Chef
**13. Use Case Name:** Cooks  
**Actor:** Chef  
**Precondition:** Order has been received  
**Description:** Prepares food according to orders  
**Postcondition:** Food is ready  

## 8. Supplier
**14. Use Case Name:** Supplies Products  
**Actor:** Supplier  
**Precondition:** Stock needs replenishment  
**Description:** Supplies ingredients and necessary products  
**Postcondition:** Inventory is updated
