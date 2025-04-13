# Business Logic Rules – POS for Ordering Menu

## 1. Menu Browsing
- A customer must be able to browse the digital menu across all supported devices (mobile, tablet, web).
- Menu items should display their name, description, price, and availability status.
- Only available items are shown in the menu.

## 2. Order Placement
- A customer can place an order that contains one or more menu items.
- Each order can include customizations like ingredient removal or portion size changes.
- An order can only be placed if at least one item is selected.
- Offline orders are saved locally and synchronized once connectivity is restored.

## 3. Order Management
- Orders have the following states: `Pending`, `In Progress`, `Ready`, `Delivered`, `Cancelled`.
- Waiters and kitchen staff can update the status of an order.
- Kitchen staff must acknowledge new orders to change them to "In Progress".
- Ready orders should be visible to waiters for delivery.

## 4. Payment Processing
- Customers can make payments using debit/credit cards, contactless, and mobile wallets.
- A payment must be successfully processed before the order status changes to "Paid".
- If payment fails, the system must alert the customer and retry or cancel the order.
- A digital receipt is generated upon successful payment.

## 5. Stock Management
- Each menu item is linked to one or more stock items.
- When an order is placed, corresponding stock quantities are reduced.
- If stock quantity falls below the reorder threshold, a request is sent to the supplier.
- Stock levels can only be modified by the manager or IT admin.

## 6. Kitchen Display System
- Orders should appear in real-time on the kitchen display upon placement.
- The system must display customizations and special instructions clearly.
- Kitchen staff should be able to mark the order as "Ready" once preparation is complete.

## 7. Role-based Access
- IT Admins have full access to system logs, error reports, and can manage user profiles.
- Managers can view offline orders, check stock, and handle customer or staff issues.
- Waiters can only view and interact with assigned customer orders.

## 8. Payment Integration and Alerts
- Any payment integration failure must generate an alert for the finance institution representative and IT admin.
- All integration errors are logged with timestamps and error codes.
- Resolved issues must be marked and archived for future audit.

## 9. Offline Mode Handling
- Orders placed while offline are queued for automatic sync once connectivity is restored.
- Offline orders are flagged and cannot be paid digitally until synced.
- Managers can view and manually approve or discard unsynced orders.

## 10. Supplier & Stock Requests
- Managers can send manual or automated requests to suppliers for stock replenishment.
- Suppliers update product availability and fulfillment timelines in response.
- Restocked items update the inventory automatically once accepted.
