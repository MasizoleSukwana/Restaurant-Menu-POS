# Domain Model: Restaurant POS – Ordering Menu System

## Entities, Attributes & Methods

### 1. Customer
- **Attributes**: `customerId`, `name`, `email`, `phone`, `deviceType`
- **Methods**:
  - `viewMenu()`
  - `placeOrder(orderDetails)`

### 2. MenuItem
- **Attributes**: `menuItemId`, `name`, `description`, `price`, `category`, `isAvailable`
- **Methods**:
  - `updateAvailability(status)`
  - `getMenuByCategory(category)`

### 3. Order
- **Attributes**: `orderId`, `customerId`, `orderDateTime`, `status`, `isOffline`
- **Methods**:
  - `updateStatus(newStatus)`
  - `syncOfflineOrder()`

### 4. OrderItem
- **Attributes**: `orderItemId`, `orderId`, `menuItemId`, `quantity`, `customization`
- **Methods**:
  - `calculateItemTotal()`
  - `applyCustomization(customOptions)`

### 5. Payment
- **Attributes**: `paymentId`, `orderId`, `paymentMethod`, `paymentStatus`, `transactionId`, `timestamp`
- **Methods**:
  - `processPayment()`
  - `generateReceipt()`

### 6. KitchenDisplay
- **Attributes**: `displayId`, `currentOrderId`
- **Methods**:
  - `showNextOrder()`
  - `refreshDisplay()`

### 7. Waiter
- **Attributes**: `waiterId`, `name`, `assignedTable`, `accessLevel`
- **Methods**:
  - `viewReadyOrders()`
  - `deliverOrder(orderId)`

### 8. Chef
- **Attributes**: `chefId`, `name`, `station`
- **Methods**:
  - `viewIncomingOrders()`
  - `updateOrderStatus(orderId, status)`

### 9. ITAdmin
- **Attributes**: `adminId`, `name`, `email`, `role`
- **Methods**:
  - `viewSystemLogs()`
  - `createUserProfile(userType, userDetails)`

### 10. Manager
- **Attributes**: `managerId`, `name`, `email`
- **Methods**:
  - `viewOfflineOrders()`
  - `checkStockLevels()`

### 11. Supplier
- **Attributes**: `supplierId`, `name`, `contact`, `productList`
- **Methods**:
  - `receiveStockRequest(stockItem)`
  - `updateProductList(productData)`

### 12. StockItem
- **Attributes**: `stockItemId`, `name`, `quantityAvailable`, `reorderThreshold`, `supplierId`
- **Methods**:
  - `checkReorderStatus()`
  - `adjustQuantity(amount)`

### 13. PaymentIntegrationLog
- **Attributes**: `logId`, `paymentId`, `errorMessage`, `timestamp`, `isResolved`
- **Methods**:
  - `markAsResolved()`
  - `notifyFinanceTeam()`
