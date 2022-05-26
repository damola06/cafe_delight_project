import sys

from products import Product
from couriers import Courier
from orders import Order


class Menu:
    def __init__(self, database):
        self.database = database

    def show_main_menu(self):
        user_input = int(input("Please enter 0 to quit, 1 to manage products,2 to manage couriers, 3 to manage orders: "))

        if user_input == 0:
            sys.exit()

        # To manage products
        if user_input == 1:
            products = Product(self.database, self.show_main_menu)
            products.handle_product_options()

        # To manage couriers
        if user_input == 2:
            couriers = Courier(self.database, self.show_main_menu)
            couriers.handle_courier_options()

        # To manage orders
        if user_input == 3:
            orders = Order(self.database, self.show_main_menu)
            orders.handle_order_options()
