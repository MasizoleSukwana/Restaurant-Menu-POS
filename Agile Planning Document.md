# Overview of Agile Planning - Restaurant-POS Ordering Menu System

The documents provides a guidlines of the core artiefacts for this project to be successful. 
The key elements of our Agile Planning for the **Restaurant-POS for Ordering Menu** system include **User Stories**, **Product Backlog**, and the **Sprint**. 
Below is an overview of each, based on what we intend to do for the project.

---

# 1. User Stories for the Restaurant-POS Ordering Menu System
**Definition**: User stories are short, simple descriptions of a feature or functionality from the perspective of the user or customer. They focus on the value or benefit that the feature will bring.  

**Format**: User stories are often written in the **"As a [role], I want [feature], so that [benefit]"** format.  

**Purpose**: They help clarify the scope of work and ensure the team understands user needs.

**Example**:  
- **As a** Customer,  
- **I want** to browse the menu and the items' descriptions and the pricelist,  
- **So that** I can decide on the food items to order for my meal.

**User Stories**: You can find the single document here:

- [User Stories Table](https://github.com/MasizoleSukwana/Restaurant-Menu-POS/blob/main/User%20Stories%20Table.md)

## User Stories with Acceptance Criteria and Priority

| **User Story ID** | **User Story** | **Acceptance Criteria** | **Priority** |
|------------------|--------------|------------------------|------------|
| **US-01** | As a Customer, I want to view the restaurant’s menu digitally, including item descriptions and prices, so that I can decide what to order conveniently. | - The menu should be accessible via web and mobile devices. <br> - Each item should include a description and price. <br> - The menu should be updated dynamically when changes occur. | **High** |
| **US-02** | As a Customer, I want to customize my orders (e.g., ingredient modifications, portion sizes), so that I can have a meal of my choice. | - Customers can add/remove ingredients from their orders. <br> - Portion sizes should be selectable (small, medium, large). <br> - Customizations should be reflected in the order summary. | **High** |
| **US-03** | As a Customer, I want to check table availability, so that I can decide whether to make a booking. | - Customers should see real-time table availability. <br> - Tables should be marked as available, occupied, or reserved. <br> - Users should be able to proceed with a booking if tables are available. | **Medium** |
| **US-04** | As a Customer, I want to make a payment using various digital payment options, so that I can complete my order seamlessly. | - Payment options should include credit/debit cards, mobile wallets, and contactless payments. <br> - Payment processing should be secure and comply with industry standards. <br> - A confirmation receipt should be generated upon successful payment. | **High** |
| **US-05** | As a Chef, I want to view orders on the kitchen display system, so that I can prepare meals as soon as possible. | - Orders should appear in real-time on the kitchen display. <br> - The system should show order details, including customizations. <br> - The chef should be able to update the order status (e.g., preparing, ready). | **High** |
| **US-06** | As a Waiter, I want to review customer orders, so that I can assist in modifications if necessary. | - Waiters should be able to view all customer orders. <br> - Order details should be editable before preparation. <br> - The system should log any modifications made by waiters. | **Medium** |
| **US-07** | As a Customer, I want to access the system via mobile devices, tablets, and web browsers, so that I can place orders conveniently. | - The system should be responsive across different devices. <br> - The UI should adapt to mobile, tablet, and desktop resolutions. <br> - Users should experience a seamless interface across all platforms. | **High** |
| **US-08** | As a Customer, I want to be able to place an order even when the system is offline, so that I can continue using the service during connectivity issues. | - The system should allow order placement in offline mode. <br> - Orders should be stored locally and synced when online. <br> - Customers should be notified when the order is successfully synced. | **Medium** |
| **US-09** | As a Manager, I want to retrieve orders placed in offline mode, so that they can be accounted for in the order history. | - Orders placed offline should be synced once the system is online. <br> - Managers should have access to a list of offline orders. <br> - The system should log timestamps for offline and sync events. | **Medium** |
| **US-10** | As an IT Admin, I want to have full access to the system, so that I can monitor and fix any system issues. | - IT Admin should have access to system logs and performance metrics. <br> - Admin should receive notifications for system failures. <br> - Admin should be able to troubleshoot and fix technical issues. | **High** |
| **US-11** | As a Manager, I want to be able to view available stock items, so that I can inform the supplier if there are any shortages. | - The system should display real-time stock availability. <br> - Managers should receive low-stock alerts. <br> - The system should generate reports on stock usage trends. | **Medium** |
| **US-12** | As a Finance institution representative, I want to receive alerts when there are payment integration errors and failures, so that I can engage with the IT admins and resolve such issues. | - The system should detect and log payment integration failures in real-time. <br> - Automated alerts should be sent to finance representatives and IT admins. <br> - Alerts should include error details for quick troubleshooting. <br> - A dashboard should display past and ongoing payment issues. | **High** |

---

# 2. Product Backlog for the Restaurant-POS Ordering Menu System
**Definition**: The product backlog is prioritized based on the **user stories** (and sometimes technical tasks) that represent all the work needed to complete the product.

**Purpose**: To help the Agile team focus on the most important tasks first and ensure that all features and requirements are captured.  

**Prioritization**: Backlog items are prioritized using the MoSCoW prioritization (Must-have, Should-have, Could-have, Won’t-have).

**Product Backlog**: You can find the single document here:

- [Product Backlog Table](https://github.com/MasizoleSukwana/Restaurant-Menu-POS/blob/main/Product%20Backlog%20Table.md)

## MoSCoW Prioritization for User Stories

| **ID**  | **User Story** | **MoSCoW Priority** | **Effort Estimate (Days)** | **Reason for Priority** | **Dependency** |
|--------|--------------|--------------------|-------------------------|------------------|------------------|
| **US-01** | As a customer, I want to view the restaurant’s menu digitally, including item descriptions and prices. | **Must-have** | **3 days** | Essential for customers to decide what to order | None |
| **US-02** | As a customer, I want to be able to customize orders (e.g., ingredient modifications, portion sizes) so that I can have a meal of my choice. | **Must-have** | **5 days** | Personalization is a key feature in modern restaurant systems | US-01 |
| **US-03** | As a customer, I want to check table availability so that I can decide whether to make a booking. | **Should-have** | **4 days** | Improves customer convenience but not essential for ordering | None |
| **US-04** | As a customer, I want to be able to make a payment using various digital payment options, including credit/debit cards, mobile wallets, and contactless payments. | **Must-have** | **8 days** | Enables seamless checkout and reduces reliance on cash | US-01 |
| **US-05** | As a chef, I want to be able to view orders on the kitchen display system for preparation as soon as possible. | **Must-have** | **6 days** | Ensures food preparation starts immediately to minimize delays | US-02 |
| **US-06** | As a waiter, I want to be able to review customer orders so that I can assist in modifications if necessary. | **Should-have** | **4 days** | Helps avoid mistakes, but customers can still customize on their own | US-02 |
| **US-07** | As a customer, I want to be able to access the system via mobile devices, tablets, and web browsers. | **Must-have** | **7 days** | Ensures accessibility across different devices | None |
| **US-08** | As a customer, I want to be able to place an order even when the system is offline. | **Could-have** | **10 days** | Adds reliability but requires complex offline data syncing | US-01, US-02 |
| **US-09** | As the manager, I want to be able to retrieve orders placed in offline mode so that they can be accounted for in the order history. | **Should-have** | **6 days** | Ensures financial and inventory records are updated properly | US-08 |
| **US-10** | As an IT Admin, I want to have full access to the system so that I can monitor issues or broken features. | **Must-have** | **5 days** | Necessary for maintaining uptime and troubleshooting | None |
| **US-11** | As a manager, I want to be able to view available stock items so that I can inform the supplier if there are any shortages. | **Should-have** | **5 days** | Helps prevent stockouts and manage restaurant operations smoothly | None |
| **US-12** | As a finance institution representative, I want to receive alerts when there are payment integration errors and failures so that I can engage with the IT admins and resolve such issues. | **Must-have** | **4 days** | Ensures seamless transaction processing and avoids payment issues | US-04, US-10 |
| **US-13** | As a supplier, I want to receive automated stock refill requests so that I can restock items before they run out. | **Could-have** | **7 days** | Automates supply chain management, but manual orders are still possible | US-11 |
| **US-14** | As a chef, I want the system to suggest recipes based on available stock to optimize ingredient use. | **Won’t-have (for now)** | **10 days** | Nice feature but not essential for initial release | US-11 |

## Summary of Prioritization
- **Must-have** (Core functionalities for MVP): **7 stories**
- **Should-have** (Important but not launch-blocking): **4 stories**
- **Could-have** (Nice-to-have, lower priority): **2 stories**
- **Won’t-have (for now)** (Not in current scope): **1 story**  

---

# 3. Sprint 1 - for the Restaurant-POS Ordering Menu System
**Definition**: A sprint is a time-boxed iteration, in our project the sprint is set to (run 2 weeks) in which the  team works to complete a set of items from the product backlog. The goal of each sprint is to produce a potentially shippable product increment.  

**Sprint Planning**: Before a sprint starts, the team holds a **Sprint Planning** meeting where they select user stories from the product backlog (based on priority and team capacity) and break them down into smaller tasks. 

**Sprint Plan**: You can find the single document here:

- [Product Backlog Table](https://github.com/MasizoleSukwana/Restaurant-Menu-POS/blob/main/Sprint%20Planning.md) 

## Sprint Planning - Task Breakdown Table

| **Task ID** | **User Story** | **Task** | **Estimated Duration (Days)** | **Status** |
|------------|--------------|---------|------------------------|---------|
| T-001 | View Restaurant Menu Digitally | Ensure the menu is accessible via web and mobile devices. | 1 | To Do |
| T-002 | View Restaurant Menu Digitally | Display item descriptions and prices. | 1 | To Do |
| T-003 | View Restaurant Menu Digitally | Enable dynamic updates when menu changes occur. | 1 | To Do |
| T-004 | Customize Orders | Allow customers to add/remove ingredients. | 2 | To Do |
| T-005 | Customize Orders | Provide portion size selection (small, medium, large). | 2 | To Do |
| T-006 | Customize Orders | Ensure customizations are reflected in the order summary. | 1 | To Do |
| T-007 | Make Digital Payments | Implement multiple payment options (credit/debit cards, mobile wallets, contactless). | 3 | To Do |
| T-008 | Make Digital Payments | Ensure secure payment processing that complies with industry standards. | 3 | To Do |
| T-009 | Make Digital Payments | Generate a confirmation receipt upon successful payment. | 2 | To Do |
| T-010 | View Orders on Kitchen Display | Display real-time orders on the kitchen display. | 2 | To Do |
| T-011 | View Orders on Kitchen Display | Show order details, including customizations. | 2 | To Do |
| T-012 | View Orders on Kitchen Display | Allow chefs to update order status (preparing, ready). | 2 | To Do |
| T-013 | Access System via Multiple Devices | Ensure system responsiveness across different devices. | 3 | To Do |
| T-014 | Access System via Multiple Devices | Adapt UI for mobile, tablet, and desktop resolutions. | 2 | To Do |
| T-015 | Access System via Multiple Devices | Provide a seamless interface across all platforms. | 2 | To Do |
| T-016 | Full System Access for IT Admin | Grant IT Admin access to system logs and performance metrics. | 2 | To Do |
| T-017 | Full System Access for IT Admin | Enable notifications for system failures. | 2 | To Do |
| T-018 | Full System Access for IT Admin | Provide tools for troubleshooting and fixing technical issues. | 1 | To Do |
| T-019 | Receive Alerts for Payment Integration Errors | Detect and log payment integration failures in real-time. | 1 | To Do |
| T-020 | Receive Alerts for Payment Integration Errors | Send automated alerts to finance representatives and IT admins. | 1 | To Do |
| T-021 | Receive Alerts for Payment Integration Errors | Include error details in alerts for quick troubleshooting. | 1 | To Do |
| T-022 | Receive Alerts for Payment Integration Errors | Develop a dashboard to display past and ongoing payment issues. | 1 | To Do |

---

# **Sprint Goal Summary: Sprint 1 - Digital Menu & Order Processing**

## **Sprint Duration:**  
⏳ 2 Weeks  

## **Goal:**  
The primary objective of this sprint is to establish a seamless **digital menu system** and ensure **order processing functionality** for the restaurant. This includes enabling customers to view the restaurant menu, customize their orders, and make payments while ensuring that kitchen staff can access and process these orders efficiently.  

---

## **Key Deliverables:**  
✅ **Digital Menu Accessibility** (Web & Mobile)  
✅ **Order Customization & Modifications**  
✅ **Payment Integration with Multiple Methods**  
✅ **Real-time Order Display for Kitchen Staff**  
✅ **System Responsiveness Across Devices**  

---

## **Success Criteria:**  
✔ Customers can browse a fully functional digital menu with real-time updates.  
✔ Order customization is available, reflecting modifications before finalizing orders.  
✔ Payment processing works securely, supporting multiple payment options.  
✔ Orders appear on the **Kitchen Display System** instantly for processing.  
✔ IT Admins have access to system logs for monitoring technical issues.  

---

## **Dependencies & Risks:**  
### 🔹 **Dependencies:**  
- Payment integration relies on third-party financial institutions.  
- Kitchen display system setup depends on IT Admin availability.  

### ⚠ **Risks:**  
- Possible **delays in third-party payment API integration**.  
- Potential **UI inconsistencies across devices** during development.

---

## Summary of the Process:
1. **Prioritize the Product Backlog**: The product owner lists all user stories, tasks, and features.
2. **Plan Sprints**: The team selects a subset of backlog items to work on in the next sprint during a sprint planning session.
3. **Work on Sprint Items**: During the sprint, the team collaborates to complete the work, with progress tracked daily.
4. **Review and Reflect**: After the sprint, the team reviews the work completed and reflects on the process to make improvements for the next sprint.
