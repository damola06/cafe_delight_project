from products import Product
from couriers import Courier

class Order:
    def __init__(self, orders, database, main_menu):
        self.orders = orders
        self.database = database
        self.main_menu = main_menu
        self.order_statuses = ["PREPARING", "OUT_FOR_DELIVERY", "DELIVERED"]
        self.products = Product(self.database, self.main_menu)
        self.couriers = Courier(self.database, self.main_menu)

    def display_list_with_index(self, list):
        for index, value in enumerate(list):
            print(index, value)

    def display_orders_options(self):
        print('''
            [1.] Print order list
            [2.] Create new order
            [3.] Update order status
            [4.] Update existing order
            [5.] Delete order 
            ''')

    def display_orders(self):
        for index, value in enumerate(self.orders):
            print(value)

    def handle_order_options(self):
        self.display_orders_options()
        selected_option = int(input("Select option 1, 2, 3, 4 0r 5 to proceed, 0 to quit: "))

        if selected_option == 0:
            self.main_menu()

        if selected_option == 1:
            self.display_orders()
            self.handle_order_options()

        if selected_option == 2:
            self.products.display_products()

            customer_products = input("Please enter the indexes of the products you want in a comma separated fashion: ")
            customer_name = input("Please enter customer name: ")
            customer_address = input("Please enter customer address: ")
            customer_phone_number = input("Please enter customer phone: ")

            self.couriers.display_couriers()

            selected_courier = int(input("Please select a courier: "))

            order = {
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone_number,
                "courier": selected_courier,
                "status": "PREPARING",
                "items": customer_products
            }

            self.orders.append(order)

            print("Order added successfully")
            self.handle_order_options()

        if selected_option == 3:
            # update status of an order
            self.display_list_with_index(self.orders)  # this means calling the function created above
            # get index of order to be updated
            index_to_be_updated = int(input("Select the index of the order you want to update status for: "))
            self.display_list_with_index(self.order_statuses)
            # get index of status we want to update to
            chosen_status_index = int(input("Select the index of the new status: "))
            # get order using the index
            order = self.orders[index_to_be_updated]
            # get status using the index
            status = self.order_statuses[chosen_status_index]
            # update order's status to the new status
            order['status'] = status
            # update orders list to overwrite old order with newly updated order
            self.orders[index_to_be_updated] = order

            print("Order status updated successfully")
            self.handle_order_options()

        if selected_option == 4:
            self.display_list_with_index(self.orders)  # this means calling the function created above
            index_to_be_updated = int(input("Select the index of the order you want to update status for: "))
            order = self.orders[index_to_be_updated]
            for key, value in order.items():
                if key == "status":
                    continue

                if key == "items":
                    self.products.display_products()
                    selected_items = input("Please enter the indexes of the products in a comma separated fashion: ")
                    if selected_items != "":
                        order["items"] = selected_items
                    continue

                if key == "courier":
                    self.couriers.display_couriers()
                    selected_courier = input("Please select a courier: ")
                    if selected_courier != "":
                        order['courier'] = selected_courier
                    continue

                new_value = input(f"Please enter {key}: ")
                if new_value == "":
                    new_value = value
                order[key] = new_value
            self.orders[index_to_be_updated] = order

            print("Order updated successfully")
            self.handle_order_options()

        if selected_option == 5:
            self.display_list_with_index(self.orders)
            index_to_be_deleted = int(input("Select the index of the order you want to delete: "))
            self.orders.pop(index_to_be_deleted)

            print("Order deleted successfully")
            self.handle_order_options()

