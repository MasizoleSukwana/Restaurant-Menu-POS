## APIs for the Restaurant
This section shows the end points created for the restaurant POS system. 
The section includes the screenshots where i tried to access the SWAGGER Docs.


### Menu Browsing

HTTP Method	Endpoint	Description

GET	/api/menu	Fetch all available menu items

GET	/api/menu/{id}	Fetch a single menu item

POST	/api/menu	Add a new menu item

PUT	/api/menu/{id}	Update a menu item

DELETE	/api/menu/{id}	Delete a menu item


### Order Placement & Management

HTTP Method	Endpoint	Description

POST	/api/orders	Place a new order

GET	/api/orders/{id}	Get order details

PUT	/api/orders/{id}/status	Update the status of an order

POST	/api/orders/{id}/customizations	Add customizations to an order

GET	/api/orders	Get all orders

GET	/api/orders/status/{status}	Filter orders by status


### Payment Processing

HTTP Method	Endpoint	Description

POST	/api/payments	Process payment for an order

GET	/api/payments/{order_id}/receipt	Fetch digital receipt for an order

POST	/api/payments/{id}/retry	Retry a failed payment

GET	/api/payments/errors	View payment integration errors


### Stock Management

HTTP Method	Endpoint	Description

GET	/api/stock	Get stock levels

POST	/api/stock	Add a new stock item

PUT	/api/stock/{id}	Update stock levels

POST	/api/stock/reorder-check	Check and notify for low stock

POST	/api/stock/{id}/reorder	Send reorder request to supplier


### Kitchen Display System

HTTP Method	Endpoint	Description

GET	/api/kitchen/orders	Get all orders in kitchen display

PUT	/api/kitchen/orders/{id}/ack	Acknowledge an order to mark it as 'In Progress'

PUT	/api/kitchen/orders/{id}/ready	Mark order as ready


### Role-based Access

HTTP Method	Endpoint	Description

GET	/api/users/roles/{role}	Get users by role

PUT	/api/users/{id}/role	Update a user's role

GET	/api/logs	Get system logs (admin only)


### Offline Mode Handling

HTTP Method	Endpoint	Description

GET	/api/orders/offline	View all offline orders

POST	/api/orders/sync	Sync offline orders to server

PUT	/api/orders/{id}/approve	Manager approves offline order

DELETE	/api/orders/{id}/discard	Discard an unsynced offline order


### Supplier & Stock Requests

HTTP Method	Endpoint	Description

POST	/api/suppliers/requests	Send manual reorder request to supplier

GET	/api/suppliers/responses	View supplier responses

PUT	/api/stock/restock/{id}	Accept and update stock based on supplier input


### API Swagger Docs NOT Accessible

![image](https://github.com/user-attachments/assets/3880469b-9b07-4866-9656-0557ec3726bb)

### Error Message

![image](https://github.com/user-attachments/assets/b24896ff-b85d-4fe0-a039-685a894f12bc)
