# Vendor Management System with Performance Metrics

## Objective
The Vendor Management System is a Django-based application integrated with Django REST Framework. Its primary aim was to facilitate efficient vendor management, purchase order tracking, and vendor performance evaluation.

## Installation

To run the RestaurantSite locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/RestaurantSite.git
    ```


2. Install Pipenv (if you haven't already):

    ```bash
    pip install pipenv
    ```

3. Install dependencies using Pipenv:

    ```bash
    pipenv install
    ```

4. Activate the Pipenv shell:

    ```bash
    pipenv shell
    ```


5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the website in your browser at [http://localhost:8000](http://localhost:8000)
7. For testing the API tool used is Insomnia.

## API endpoints documentation and its implementation with screenshots
### Vendor Profile Management:

1. Sending POST request for generating Token for registered user. For user registration used django-admin portal.  [http://localhost:8000/apitoken/](http://localhost:8000/apitoken/)
  ![Generating Token for Registered User](Screenshots/Generating_token_for_registered_user.png)
2. Sendin POST request for registering the vendor using previously generated token. [http://localhost:8000/api/vendors/](http://localhost:8000/api/vendors/)
  ![Registering_vendor_using_previously_generated_token](Screenshots/Registering_vendor_using_previously_generated_token.png)
3. Sending GET request to list all the vendors.  [http://localhost:8000/api/vendors/](http://localhost:8000/api/vendors/)
   ![Fetching_vendors_list](Screenshots/Fetching_vendors_list.png)
4. Sending GET request to list vendor by vendors ID. [http://localhost:8000/api/vendors/1/](http://localhost:8000/api/vendors/1)
   ![Fetching_vendor_by_ID](Screenshots/Fetching_vendor_by_ID.png)
5. Sending PUT request to update the details like address. [http://localhost:8000/api/vendors/1/](http://localhost:8000/api/vendors/1/)
   ![Updating_vendor_deatils](Screenshots/Updated_vendors_deatils.png)
6. Sending DELETE request to delete the vendor by ID.  [http://localhost:8000/api/vendors/1/](http://localhost:8000/api/vendors/1/)
   ![deleting_the_updated_vendor](Screenshots/deleting_the_updated_vendor.png)

### Purchase Order Tracking:
1. Sending POST request for creating purchase order. [http://localhost:8000/api/purchase-orders/](http://localhost:8000/api/purchase-orders/)
   ![Creating_order](Screenshots/Creating_order.png)
2. POST request sent and purchase order has been created. [http://localhost:8000/api/purchase-orders/](http://localhost:8000/api/purchase-orders/)
   ![Order_created](Screenshots/Order_created.png)
3. Sending the GET request and fetching the purchase orders list. [http://localhost:8000/api/purchase-orders/](http://localhost:8000/api/purchase-orders/)
   ![Fetching_purcahse_orders_list](Screenshots/Fetching_purcahse_orders_list.png)
4. Sending GET request and fetching the purchase order by its ID.  [http://localhost:8000/api/purchase-orders/8/](http://localhost:8000/api/purchase-orders/8/)
   ![purchase_order_by_ID](Screenshots/purchase_order_by_ID.png)
5. Sent PUT request and updated the items of previously fetched purchase order. [http://localhost:8000/api/purchase-orders/8/](http://localhost:8000/api/purchase-orders/8/)
   ![updated_previously_fetched_purcahse_order](Screenshots/updated_previously_fetched_purcahse_order.png)

### Vendor Performance Evaluation

1. Sending GET request to fetch performance of vendor by its ID.  [http://localhost:8000/api/2/performance/](http://localhost:8000/api/2/performance/)
   ![Fetching_performance_of_vendors](Screenshots/Fetching_performance_of_vendors.png)
2. Sending PUT request to acknowledge and triggering the average response time. [http://localhost:8000/api/2/performance/](http://localhost:8000/api/2/performance/)
   ![Acknowledging_the_completed_orders](Screenshots/Acknowledging_the_completed_orders.png)
3. Sending GET request to fetch the acknowledged details of vendor and updated average response time. [http://localhost:8000/api/2/performance/](http://localhost:8000/api/2/performance/)
   ![Fetching_vendors_performance_after_acknowledgement](Screenshots/Fetching_vendors_performance_after_acknowledgement.png)

### Data stored in MySQL database
1. Vendor's Data
   ![Accessing_vendors_data_from_mysql_database](Screenshots/Accessing_vendors_data_from_mysql_database.png)
2. Purchase Orders Data
   ![Accessing_Purchase_order_data_from_mysql_database](Screenshots/Accessing_Purchase_order_data_from_mysql_database.png)
3. Historical Performance Data
   ![Accessing_Historical_performance_data_from_mysql_database](Screenshots/Accessing_Historical_performance_data_from_mysql_database.png)


### Django-admin portal
1. Vendor's Data
   ![Django-Admin-Vendors](Screenshots/Django-Admin-Vendors.png)
2. Purchase Orders Data
![Django_admin_Purchase_orders](Screenshots/Django_admin_Purchase_orders.png)
3. Historical Performance Data
![Django_admin_Historical_performance](Screenshots/Django_admin_Historical_performance.png)
## Contribution
- Contributions are welcome! Fork the repository and submit pull requests.

## License
- This project was licensed under the [MIT License](LICENSE).

## Author
- [Shailendra Kumar](https://github.com/shail840)

Feel free to customize this README to fit your project's specific needs. Let me know if you need any further assistance!
