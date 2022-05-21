import sys
import csv

from products import Product
from couriers import Courier
from orders import Order

class Menu:
    def __init__(self, database):
        self.orders = self.read_file("data/orders.csv")
        self.database = database

    def read_file(self, file_path):
        with open(file_path) as f:
            result = [{k: v for k, v in row.items()}
                      for row in csv.DictReader(f, skipinitialspace=True)]

            return result

    def write_file(self, file_path, content):
        keys = content[0].keys()

        with open(file_path, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(content)

    def show_main_menu(self):
        user_input = int(input("Please enter 0 to quit, 1 to manage products, 2 to manage couriers and 3 to manage orders: "))

        if user_input == 0:
            self.write_file("data/orders.csv", self.orders)
            sys.exit()

        if user_input == 1:
            products = Product(self.database, self.show_main_menu)
            products.handle_product_options()

        if user_input == 2:
            couriers = Courier(self.database, self.show_main_menu)
            couriers.handle_courier_options()

        if user_input == 3:
            orders = Order(self.orders, self.database, self.show_main_menu)
            orders.handle_order_options()