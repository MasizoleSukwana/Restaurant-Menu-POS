# Product Backlog for the Restaurant-POS Ordering Menu System

# MoSCoW Prioritization for User Stories

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

## Next Steps
1. Assign **Must-have stories** to Sprint 1 (highest priority).
2. Plan **Should-have and Could-have stories** for later sprints.
3. Reevaluate **Won’t-have stories** for future releases.
