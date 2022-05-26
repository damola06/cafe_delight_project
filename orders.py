from products import Product
from couriers import Courier


class Order:
    def __init__(self, database, main_menu):
        self.database = database
        self.main_menu = main_menu
        self.products = Product(self.database, self.main_menu)
        self.couriers = Courier(self.database, self.main_menu)

    def display_list_with_index(self, list):
        for index, value in enumerate(list):
            print(index, value)

    def display_orders_options(self):
        print('''
            [1.] Display order
            [2.] Create new order
            [3.] Update order status
            [4.] Update existing order
            [5.] Delete order 
            ''')

    def display_orders(self):
        orders = self.database.select("SELECT orders.id, orders.customer_name, orders.status,"
                                      " order_statuses.order_status,"
                                      " orders.courier, couriers.name as courier_name,"
                                      " orders.customer_address, orders.items,"
                                      " orders.customer_phone FROM orders LEFT JOIN order_statuses"
                                      " ON orders.status = order_statuses.id LEFT JOIN couriers ON"
                                      " orders.courier = couriers.id ")
        print(*orders, sep="\n")

    def display_order_statuses(self):
        order_statuses = self.database.select("SELECT * FROM order_statuses")
        print(*order_statuses, sep="\n")

    def handle_order_options(self):
        self.display_orders_options()
        selected_option = int(input("Select option 1, 2, 3, 4 0r 5 to proceed, 0 to main menu: "))

        # Back to main menu
        if selected_option == 0:
            self.main_menu()

        # Display order
        if selected_option == 1:
            self.display_orders()
            self.handle_order_options()

        # Create new order
        if selected_option == 2:
            self.products.display_products()

            customer_products = input(
                "Please enter the indexes of the products you want in a comma separated fashion: ")
            customer_name = input("Please enter customer name: ")
            customer_address = input("Please enter customer address: ")
            customer_phone = input("Please enter customer phone: ")

            self.couriers.display_couriers()

            selected_courier = int(input("Please select id of the courier: "))

            status = self.database.selectSingle("SELECT * FROM order_statuses where order_status = 'PREPARING'")
            sql = f"INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items)" \
                  f" VALUES (%s, %s, %s, %s, %s, %s)"
            val = (customer_name, customer_address, customer_phone, selected_courier, status["id"], customer_products)

            self.database.execute(sql, val)

            print("Order added successfully")
            self.handle_order_options()

        # update status of an order_status
        if selected_option == 3:
            self.display_orders()
            # get index of order to be updated
            id_to_be_updated = int(input("Select the id of the order you want to update status for: "))
            self.display_order_statuses()
            # get index of status we want to update to
            chosen_status_id = int(input("Select the id of the new status: "))

            sql = "UPDATE orders SET status = %s WHERE id = %s"
            val = (chosen_status_id, id_to_be_updated)

            self.database.execute(sql, val)

            print("Order status updated successfully")
            self.handle_order_options()

        # Update existing order
        if selected_option == 4:
            self.display_orders()
            id_to_be_updated = int(input("Select the id of the order you want to update status for: "))
            order = self.database.selectSingle(f"SELECT * from orders where id = {id_to_be_updated}")
            for key, value in order.items():
                if key == "status":
                    continue

                if key == "id":
                    continue

                if key == "items":
                    self.products.display_products()
                    selected_items = input("Please enter the ids of the products in a comma separated fashion: ")
                    if selected_items != "":
                        order["items"] = selected_items
                    continue

                if key == "courier":
                    self.couriers.display_couriers()
                    selected_courier = input("Please select id of a courier: ")
                    if selected_courier != "":
                        order['courier'] = selected_courier
                    continue

                new_value = input(f"Please enter {key}: ")
                if new_value == "":
                    new_value = value
                order[key] = new_value

            sql = "UPDATE orders SET customer_name = %s, items = %s, courier = %s, customer_address = %s, " \
                  "customer_phone = %s WHERE id = %s"
            val = (order['customer_name'], order['items'], order['courier'],
                   order['customer_address'], order['customer_phone'],
                   id_to_be_updated)

            self.database.execute(sql, val)

            print("Order updated successfully")
            self.handle_order_options()

        # Delete order
        if selected_option == 5:
            self.display_orders()
            id_to_be_deleted = int(input("Select the id of the order you want to delete: "))
            order = self.database.selectSingle(f"SELECT * FROM orders WHERE id = {id_to_be_deleted}")
            if order is None or len(order) == 0:
                print(f"Order with id {id_to_be_deleted} does not exist")
                self.handle_order_options()

            sql = "DELETE from orders WHERE id = %s"
            val = int(id_to_be_deleted)

            self.database.execute(sql, val)

            print("Order deleted successfully")
            self.handle_order_options()
