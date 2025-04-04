# Restaurant-POS Ordering Menu - Activity Workflows
- Customer
- Order
- Payment
- Kitchen Display
- Waiter
- Manager
- IT Admin
- Finance Institution Rep
- Supplier

---

# Activity Flow Diagrams

## 1. Customer Browsing the Menu at a Restaurant

```mermaid
flowchart TD
    A[Start] --> B[Browse Menu]
    B --> C{Select Item?}
    C -->|Yes| D[End]
    C -->|No| B
```

## 2. Customer Making an Order at a Restaurant

```mermaid
flowchart TD
    A[Start] --> B[Select Items]
    B --> C{Confirm Order?}
    C -->|Yes| D[Place Order]
    C -->|No| B
    D --> E[Kitchen Prepares Order]
    E --> F[End]
```

## 3. Customer Making a Payment for an Order at a Restaurant

```mermaid
flowchart TD
    A[Start] --> B[Initiate Payment]
    B --> C{Complete Payment?}
    C -->|Yes| D[End]
    C -->|No| B
```

## 4. Kitchen Display System Displaying Orders for a Restaurant

```mermaid
flowchart TD
    A[Start] --> B[Display Order]
    B --> C{Start Preparing Order?}
    C -->|Yes| D[Start Preparing Order]
    D --> E{Complete Preparation?}
    E -->|Yes| F[Serve Order]
    F --> G[End]
```

## 5. Waiter Attending to an Order at a Restaurant

```mermaid
flowchart TD
    A[Start] --> B[Take Order]
    B --> C{Order Ready to Serve?}
    C -->|Yes| D[Serve Order]
    D --> E{Payment Collected?}
    E -->|Yes| F[End]
    C -->|No| B
    E -->|No| D
```

## 6. IT Admin Fixing System Issues for the Restaurant POS

```mermaid
flowchart TD
    A[Start] --> B[Report Issue]
    B --> C{Start Troubleshooting?}
    C -->|Yes| D[Start Troubleshooting]
    D --> E{Issue Fixed?}
    E -->|Yes| F[End]
    C -->|No| B
    E -->|No| D
```

## 7. Finance Institution Rep Receiving Payment Alerts

```mermaid
flowchart TD
    A[Start] --> B[Receive Payment Alert]
    B --> C{Verify Payment?}
    C -->|Yes| D[Process Payment]
    D --> E[End]
    C -->|No| B
```

## 8. Restaurant Manager Managing Stock

```mermaid
flowchart TD
    A[Start] --> B[Monitor Stock Levels]
    B --> C{Place Stock Order?}
    C -->|Yes| D[Place Stock Order]
    D --> E{Stock Received?}
    E -->|Yes| F[End]
    C -->|No| B
    E -->|No| D
```

## 9. Supplier Managing Stock Request from the Restaurant Manager

```mermaid
flowchart TD
    A[Start] --> B[Receive Stock Request]
    B --> C{Place Order?}
    C -->|Yes| D[Place Order]
    D --> E{Stock Delivered?}
    E -->|Yes| F[End]
    C -->|No| B
    E -->|No| D
```
