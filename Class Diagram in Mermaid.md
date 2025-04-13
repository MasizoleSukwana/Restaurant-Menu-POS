````markdown
```mermaid
classDiagram
    class Customer {
        +String customerId
        +String name
        +String email
        +String phone
        +String deviceType
        +viewMenu()
        +placeOrder(orderDetails)
    }

    class MenuItem {
        +String menuItemId
        +String name
        +String description
        +Double price
        +String category
        +Boolean isAvailable
        +updateAvailability(status)
        +getMenuByCategory(category)
    }

    class Order {
        +String orderId
        +String customerId
        +DateTime orderDateTime
        +String status
        +Boolean isOffline
        +updateStatus(newStatus)
        +syncOfflineOrder()
    }

    class OrderItem {
        +String orderItemId
        +String orderId
        +String menuItemId
        +int quantity
        +String customization
        +calculateItemTotal()
        +applyCustomization(customOptions)
    }

    class Payment {
        +String paymentId
        +String orderId
        +String paymentMethod
        +String paymentStatus
        +String transactionId
        +DateTime timestamp
        +processPayment()
        +generateReceipt()
    }

    class KitchenDisplay {
        +String displayId
        +String currentOrderId
        +showNextOrder()
        +refreshDisplay()
    }

    class Waiter {
        +String waiterId
        +String name
        +int assignedTable
        +String accessLevel
        +viewReadyOrders()
        +deliverOrder(orderId)
    }

    class Chef {
        +String chefId
        +String name
        +String station
        +viewIncomingOrders()
        +updateOrderStatus(orderId, status)
    }

    class ITAdmin {
        +String adminId
        +String name
        +String email
        +String role
        +viewSystemLogs()
        +createUserProfile(userType, userDetails)
    }

    class Manager {
        +String managerId
        +String name
        +String email
        +viewOfflineOrders()
        +checkStockLevels()
    }

    class Supplier {
        +String supplierId
        +String name
        +String contact
        +List~Product~ productList
        +receiveStockRequest(stockItem)
        +updateProductList(productData)
    }

    class StockItem {
        +String stockItemId
        +String name
        +int quantityAvailable
        +int reorderThreshold
        +String supplierId
        +checkReorderStatus()
        +adjustQuantity(amount)
    }

    class PaymentIntegrationLog {
        +String logId
        +String paymentId
        +String errorMessage
        +DateTime timestamp
        +Boolean isResolved
        +markAsResolved()
        +notifyFinanceTeam()
    }

    Customer "1" --> "*" Order : places
    Order "1" --> "*" OrderItem : contains
    OrderItem "*" --> "1" MenuItem : references
    Order "1" --> "1" Payment : has
    Chef "1" --> "*" Order : prepares
    KitchenDisplay "1" --> "1" Order : displays
    Waiter "1" --> "*" Order : delivers
    Manager "1" --> "*" StockItem : monitors
    Supplier "1" --> "*" StockItem : provides
    StockItem "1" --> "1" Supplier : is supplied by
    PaymentIntegrationLog "1" --> "1" Payment : logs
    ITAdmin "*" --> "*" Customer : manages
    ITAdmin "*" --> "*" Order : manages
    ITAdmin "*" --> "*" Payment : monitors
```
````
