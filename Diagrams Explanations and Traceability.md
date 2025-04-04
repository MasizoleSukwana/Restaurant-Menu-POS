# State Diagrams and Activity Flow Diagrams Explanations with Traceability

### **Overview**
This markdown file explains the state diagrams, activity flow diagrams, and traces each scenario to the respective user stories and requirements. This approach helps to understand how each role in the restaurant system interacts with the process and how the system meets business needs. The traceability matrix ensures that the system is designed in alignment with user expectations.

## 1. **Customer Browsing the Menu at a Restaurant**

### State Diagram Explanation:

**States**:
- **Browsing Menu**: The customer starts by browsing the restaurant’s menu.
- **Item Selected**: The customer selects an item.

**Transitions**:
- **Browse Menu → Select Item**: The customer browses the menu and then selects an item from it.
- **Select Item → End**: Once the customer has selected an item, they are done browsing and proceed to the next step (e.g., placing an order).
- **Loop**: If the customer doesn’t make a selection, they continue browsing the menu.

### Activity Flow Diagram Explanation:
- The customer starts by browsing the menu.
- The customer selects an item.
- If no item is selected, the customer continues browsing.
- The process ends when an item is selected.

**Traceability**:
- **User Story (US-01)**: As a Customer, I want to view the restaurant’s menu digitally, including item descriptions and prices, so that I can decide what to order conveniently.
- **Requirement**: Digital menu with item descriptions and prices.

---

## 2. **Customer Making an Order at a Restaurant**

### State Diagram Explanation:

**States**:
- **Items Selected**: The customer selects their items from the menu.
- **Order Confirmed**: The customer confirms the order.
- **Order Placed**: The customer places the order for the kitchen to start preparing.

**Transitions**:
- **Select Items → Confirm Order**: After selecting items, the customer confirms the order.
- **Confirm Order → Place Order**: The customer places the order once confirmed.
- **Place Order → Kitchen Prepares Order**: The order is sent to the kitchen for preparation.
- **End**: The flow concludes when the order is placed and preparation begins.

### Activity Flow Diagram Explanation:
- The customer selects items from the menu.
- The customer confirms the order.
- After confirmation, the customer places the order for the kitchen.
- The process ends once the order is placed.

**Traceability**:
- **User Story (US-02)**: As a Customer, I want to customize my orders (e.g., ingredient modifications, portion sizes), so that I can have a meal of my choice.
- **Requirement**: Ability to select and customize menu items.

---

## 3. **Customer Making a Payment for an Order at a Restaurant**

### State Diagram Explanation:

**States**:
- **Payment Initiated**: The customer starts the payment process.
- **Payment Completed**: The payment process is completed.

**Transitions**:
- **Initiate Payment → Complete Payment**: The customer proceeds to make payment.
- **Complete Payment → End**: The payment is completed, and the transaction is finished.

### Activity Flow Diagram Explanation:
- The customer initiates the payment process.
- The customer completes the payment.
- The process ends once the payment is completed.

**Traceability**:
- **User Story (US-04)**: As a Customer, I want to make a payment using various digital payment options, so that I can complete my order seamlessly.
- **Requirement**: Multiple payment options (e.g., credit cards, mobile wallets).

---

## 4. **Kitchen Display System Displaying Orders for a Restaurant**

### State Diagram Explanation:

**States**:
- **Order Displayed**: The kitchen system displays the incoming order.
- **Preparing Order**: The kitchen staff starts preparing the order.
- **Order Prepared**: The kitchen finishes preparing the order.

**Transitions**:
- **Order Displayed → Start Preparing**: The kitchen receives the order and starts preparing it.
- **Start Preparing → Order Prepared**: After preparation, the order is ready to be served.
- **Order Prepared → Serve Order**: The order is served to the customer.
- **End**: The process concludes once the order is served.

### Activity Flow Diagram Explanation:
- The order is displayed in the kitchen system.
- The kitchen starts preparing the order.
- Once the preparation is complete, the order is served to the customer.
- The process ends after serving the order.

**Traceability**:
- **User Story (US-05)**: As a Chef, I want to view orders on the kitchen display system, so that I can prepare meals as soon as possible.
- **Requirement**: Kitchen display system showing orders.

---

## 5. **Waiter Attending to an Order at a Restaurant**

### State Diagram Explanation:

**States**:
- **Order Taken**: The waiter takes the customer’s order.
- **Order Served**: The waiter serves the order to the customer.
- **Payment Collected**: The waiter collects the payment after serving the order.

**Transitions**:
- **Take Order → Serve Order**: The waiter serves the order once it's ready.
- **Serve Order → Collect Payment**: After serving, the waiter collects the payment.
- **Collect Payment → End**: The flow concludes once the payment is collected.

### Activity Flow Diagram Explanation:
- The waiter takes the customer’s order.
- Once the order is ready, the waiter serves the food.
- The waiter collects payment after serving the order.
- The process ends once the payment is collected.

**Traceability**:
- **User Story (US-06)**: As a Waiter, I want to be able to review customer orders so that I can assist in modifications if necessary and deliver orders when they are ready.
- **Requirement**: Order management for waiters to collect, modify, and deliver orders.

---

## 6. **IT Admin Fixing System Issues for the Restaurant POS**

### State Diagram Explanation:

**States**:
- **Issue Reported**: The issue with the system (POS) is reported.
- **Troubleshooting Started**: The IT admin starts troubleshooting the issue.
- **Issue Fixed**: The IT admin resolves the issue.

**Transitions**:
- **Report Issue → Start Troubleshooting**: The admin starts fixing the reported issue.
- **Start Troubleshooting → Issue Fixed**: The IT admin fixes the issue.
- **Issue Fixed → End**: The flow concludes once the issue is resolved.

### Activity Flow Diagram Explanation:
- The system issue is reported.
- The IT admin starts troubleshooting.
- The issue is fixed, and the process ends.

**Traceability**:
- **User Story (US-10)**: As an IT Admin, I want to have full access to the system, so that I can monitor and fix any system issues.
- **Requirement**: System access for IT admins to manage and troubleshoot.

---

## 7. **Finance Institution Rep Receiving Payment Alerts**

### State Diagram Explanation:

**States**:
- **Payment Alert Received**: A payment alert is received by the finance institution representative.
- **Payment Verified**: The finance rep verifies the payment.
- **Payment Processed**: The payment is processed and recorded.

**Transitions**:
- **Receive Payment Alert → Verify Payment**: The finance rep verifies the received payment alert.
- **Verify Payment → Process Payment**: After verification, the payment is processed.
- **Process Payment → End**: The flow concludes once the payment is processed.

### Activity Flow Diagram Explanation:
- The finance institution representative receives the payment alert.
- The payment is verified.
- The payment is processed, and the process ends.

**Traceability**:
- **User Story (US-12)**: As a Finance Institution Representative, I want to receive alerts when there are payment integration errors and failures, so that I can engage with the IT admins and resolve such issues.
- **Requirement**: Payment error notification and verification system.

---

## 8. **Restaurant Manager Managing Stock**

### State Diagram Explanation:

**States**:
- **Stock Monitoring**: The manager monitors the stock levels.
- **Stock Ordered**: The manager orders stock to replenish inventory.
- **Stock Received**: The ordered stock is received.

**Transitions**:
- **Monitor Stock Levels → Place Stock Order**: The manager places an order if the stock levels are low.
- **Place Stock Order → Stock Received**: The ordered stock is delivered.
- **Stock Received → End**: The process ends once the stock is received and inventory is updated.

### Activity Flow Diagram Explanation:
- The restaurant manager monitors the stock levels.
- If needed, the manager places a stock order.
- The stock is received, and the process ends.

**Traceability**:
- **User Story (US-11)**: As a Manager, I want to be able to view available stock items, so that I can inform the supplier if there are any shortages.
- **Requirement**: Stock monitoring and order management.

---

## 9. **Supplier Managing Stock Request from the Restaurant Manager**

### State Diagram Explanation:

**States**:
- **Stock Request Received**: The supplier receives the request from the restaurant manager.
- **Stock Ordered**: The supplier places the order for the requested stock.
- **Stock Delivered**: The stock is delivered to the restaurant.

**Transitions**:
- **Receive Stock Request → Place Stock Order**: The supplier processes the stock order.
- **Place Stock Order → Stock Delivered**: Once the order is fulfilled, the stock is delivered.
- **Stock Delivered → End**: The flow ends after the stock is delivered to the restaurant.

### Activity Flow Diagram Explanation:
- The supplier receives the stock request from the restaurant manager.
- The supplier places the stock order.
- Once delivered, the process ends.

**Traceability**:
- **User Story (US-13)**: As a Supplier, I want to receive stock request alerts from the restaurant manager so that I can process the request accordingly.
- **Requirement**: Stock request notification and fulfillment system.

---
