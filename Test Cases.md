# Test Cases for covering the Functional and Non-Functional Requirements

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
|-------------|---------------|-------------|-------|-----------------|--------------|------------------|
| TC_001 | FR_1.1 | Verify customers can view the restaurant’s menu digitally. | 1. Open the system. <br> 2. Navigate to the menu section. | Menu should be displayed with item descriptions and prices. | | |
| TC_002 | FR_1.2 | Verify customers can customize orders. | 1. Select an item from the menu. <br> 2. Click on the customization option. <br> 3. Modify ingredients/portion size. | Order should be updated with modifications. | | |
| TC_003 | FR_1.3 | Verify customers can place orders without waiter intervention. | 1. Select items from the menu. <br> 2. Add items to the cart. <br> 3. Confirm order placement. | Order should be placed successfully. | | |
| TC_004 | FR_1.4 | Verify customers can modify their cart before finalizing the order. | 1. Add an item to the cart. <br> 2. Remove or add another item before finalizing the order. | Items should be updated in the cart accordingly. | | |
| TC_005 | FR_1.5 | Verify real-time order status updates. | 1. Place an order. <br> 2. Check order status in the system. | Order status should change as it progresses (e.g., "Received," "Preparing," "Ready"). | | |
| TC_006 | FR_2.1 | Verify customers can check table availability. | 1. Open the system. <br> 2. Navigate to table booking section. | Available tables should be displayed. | | |
| TC_007 | FR_2.2 | Verify customers can reserve a table. | 1. Select a table. <br> 2. Confirm reservation. | Table should be reserved successfully. | | |
| TC_008 | FR_3.1 | Verify digital payment options. | 1. Proceed to checkout. <br> 2. Select a digital payment method. <br> 3. Complete payment. | Payment should be processed successfully. | | |
| TC_009 | FR_4.1 | Verify orders are sent to the kitchen display. | 1. Place an order. <br> 2. Check the kitchen display system. | Order should appear in the kitchen display. | | |
| TC_010 | NFR_1.1 | Verify the system processes orders within 2 seconds. | 1. Place an order. <br> 2. Measure response time. | Order should be processed in ≤2 seconds. | | |
| TC_011 | NFR_2.1 | Verify AES-256 encryption for payment transactions. | 1. Initiate a payment. <br> 2. Inspect transaction logs for encryption. | Payment data should be encrypted. | | |
| TC_012 | NFR_4.1 | Verify 99.9% uptime. | 1. Monitor system uptime over a period. | System uptime should meet or exceed 99.9%. | | |
| TC_013 | NFR_5.1 | Verify system scalability under high load. | 1. Simulate 200 concurrent users. | System should function normally without lag. | | |
