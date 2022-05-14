import sys
import csv


def display_list_with_index(list):
    for index, value in enumerate(list):
        print(index, value)


def display_menu_options():
    print('''
    [1.] Print product list
    [2.] Create new product
    [3.] Update existing product
    [4.] Delete product 
    ''')


def display_courier_options():
    print('''
    [1.] Print courier list
    [2.] Create new courier
    [3.] Update existing courier
    [4.] Delete courier 
    ''')


def display_orders_options():
    print('''
    [1.] Print order list
    [2.] Create new order
    [3.] Update order status
    [4.] Update existing order
    [5.] Delete order 
    ''')


def display_main_menu():
    print(f"Current menu")
    print(*products, sep="\n")


def display_courier():
    print(f"Current couriers")
    print(*couriers, sep="\n")


def display_orders():
    for index, value in enumerate(orders):
        print(value)


def handle_product_options():
    display_menu_options()
    selected_option = int(input("Select option 1, 2, 3 or 4 to proceed, 0 to quit: "))

    if selected_option == 0:
        show_main_menu()

    if selected_option == 1:
        display_main_menu()
        handle_product_options()

    if selected_option == 2:
        new_product_name = input("Enter product name: ")
        new_product_price = input("Enter product price: ")

        product = {
            "name": new_product_name,
            "price": new_product_price
        }

        products.append(product)
        handle_product_options()

    if selected_option == 3:
        display_list_with_index(products)  # this means calling the function created above
        index_to_be_updated = int(input("Select the index of the item you want to update: "))

        product = products[index_to_be_updated]
        for key, value in product.items():
            new_value = input(f"Please enter {key}: ")
            if new_value == "":
                new_value = value
            product[key] = new_value
        products[index_to_be_updated] = product
        handle_product_options()

    if selected_option == 4:
        display_list_with_index(products)
        index_to_be_deleted = int(input("Select the index of the item you want to delete: "))
        products.pop(index_to_be_deleted)
        handle_product_options()


def handle_courier_options():
    display_courier_options()
    selected_option = int(input("Select option 1, 2, 3 or 4 to proceed, 0 to quit: "))

    if selected_option == 0:
        show_main_menu()

    if selected_option == 1:
        display_courier()
        handle_courier_options()

    if selected_option == 2:
        new_courier_name = input("Enter courier name: ")
        new_courier_phone = input("Enter courier phone: ")

        new_courier = {
            "name": new_courier_name,
            "phone": new_courier_phone
        }

        couriers.append(new_courier)
        handle_courier_options()

    if selected_option == 3:
        display_list_with_index(couriers)  # this means calling the function created above
        index_to_be_updated = int(input("Select the index of the courier you want to update: "))

        courier = couriers[index_to_be_updated]
        for key, value in courier.items():
            new_value = input(f"Please enter {key}: ")
            if new_value == "":
                new_value = value
            courier[key] = new_value
        couriers[index_to_be_updated] = courier

        handle_courier_options()

    if selected_option == 4:
        display_list_with_index(products)
        index_to_be_deleted = int(input("Select the index of the courier you want to delete: "))
        couriers.pop(index_to_be_deleted)
        handle_courier_options()


def handle_order_options():
    display_orders_options()
    selected_option = int(input("Select option 1, 2, 3, 4 0r 5 to proceed, 0 to quit: "))

    if selected_option == 0:
        show_main_menu()

    if selected_option == 1:
        display_orders()
        handle_order_options()

    if selected_option == 2:
        display_list_with_index(products)
        customer_products = input("Please enter the indexes of the products you want in a comma separated fashion: ")
        customer_name = input("Please enter customer name: ")
        customer_address = input("Please enter customer address: ")
        customer_phone_number = input("Please enter customer phone: ")
        display_list_with_index(couriers)
        selected_courier = int(input("Please select a courier: "))

        order = {
            "customer_name": customer_name,
            "customer_address": customer_address,
            "customer_phone": customer_phone_number,
            "courier": selected_courier,
            "status": "PREPARING",
            "items": customer_products
        }

        orders.append(order)
        handle_order_options()

    if selected_option == 3:
        # update status of an order
        display_list_with_index(orders)  # this means calling the function created above
        # get index of order to be updated
        index_to_be_updated = int(input("Select the index of the order you want to update status for: "))
        display_list_with_index(order_statuses)
        # get index of status we want to update to
        chosen_status_index = int(input("Select the index of the new status: "))
        # get order using the index
        order = orders[index_to_be_updated]
        # get status using the index
        status = order_statuses[chosen_status_index]
        # update order's status to the new status
        order['status'] = status
        # update orders list to overwrite old order with newly updated order
        orders[index_to_be_updated] = order
        handle_order_options()

    if selected_option == 4:
        display_list_with_index(orders)  # this means calling the function created above
        index_to_be_updated = int(input("Select the index of the order you want to update status for: "))
        order = orders[index_to_be_updated]
        for key, value in order.items():
            if key == "status":
                continue

            if key == "items":
                display_list_with_index(products)
                selected_items = input("Please enter the indexes of the products in a comma separated fashion: ")
                if selected_items != "":
                    order["items"] = selected_items
                continue

            if key == "courier":
                display_list_with_index(couriers)
                selected_courier = input("Please select a courier: ")
                if selected_courier != "":
                    order['courier'] = selected_courier
                continue

            new_value = input(f"Please enter {key}: ")
            if new_value == "":
                new_value = value
            order[key] = new_value
        orders[index_to_be_updated] = order
        handle_order_options()

    if selected_option == 5:
        display_list_with_index(orders)
        index_to_be_deleted = int(input("Select the index of the order you want to delete: "))
        orders.pop(index_to_be_deleted)
        handle_order_options()


def show_main_menu():
    user_input = int(input("Please enter 0 to quit, 1 to manage products, 2 to manage couriers and 3 to manage orders: "))

    if user_input == 0:
        write_file("data/products.csv", products)
        write_file("data/couriers.csv", couriers)
        write_file("data/orders.csv", orders)
        sys.exit()

    if user_input == 1:
        handle_product_options()  # this calls the function that shows the menu options and handles them

    if user_input == 2:
        handle_courier_options()  # this calls the function that shows the courier options and handles them

    if user_input == 3:
        handle_order_options()  # this calls the function that shows the order options and handles them


def read_file(file_path):
    with open(file_path) as f:
        result = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]

        return result


def write_file(file_path, content):
    keys = content[0].keys()

    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(content)


products = read_file("data/products.csv")

couriers = read_file("data/couriers.csv")

orders = read_file("data/orders.csv")

order_statuses = ["PREPARING", "OUT_FOR_DELIVERY", "DELIVERED"]

show_main_menu()
