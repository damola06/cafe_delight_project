import sys

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
    print(*main_menu, sep="\n")


def display_courier():
    print(f"Current couriers")
    print(*couriers, sep="\n")


def display_orders():
    for index, value in enumerate(orders):
        print(value)

def handle_menu_options():
    display_menu_options()
    selected_option = int(input("Select option 1, 2, 3 or 4 to proceed, 0 to quit: "))

    if selected_option == 0:
        show_main_menu()

    if selected_option == 1:
        display_main_menu()
        handle_menu_options()

    if selected_option == 2:
        new_product = input("Enter product name: ")
        main_menu.append(new_product)
        handle_menu_options()

    if selected_option == 3:
        display_list_with_index(main_menu)  # this means calling the function created above
        index_to_be_updated = int(input("Select the index of the item you want to update: "))
        new_product_name = input("Enter new product name: ")
        main_menu[index_to_be_updated] = new_product_name
        handle_menu_options()

    if selected_option == 4:
        display_list_with_index(main_menu)
        index_to_be_deleted = int(input("Select the index of the item you want to delete: "))
        main_menu.pop(index_to_be_deleted)
        handle_menu_options()


def handle_courier_options():
    display_courier_options()
    selected_option = int(input("Select option 1, 2, 3 or 4 to proceed, 0 to quit: "))

    if selected_option == 0:
        show_main_menu()

    if selected_option == 1:
        display_courier()
        handle_courier_options()

    if selected_option == 2:
        new_courier = input("Enter courier name: ")
        couriers.append(new_courier)
        handle_courier_options()

    if selected_option == 3:
        display_list_with_index(main_menu)  # this means calling the function created above
        index_to_be_updated = int(input("Select the index of the courier you want to update: "))
        new_courier_name = input("Enter new courier name: ")
        couriers[index_to_be_updated] = new_courier_name
        handle_courier_options()

    if selected_option == 4:
        display_list_with_index(main_menu)
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
            "status": "PREPARING"
        }

        orders.append(order)
        handle_order_options()

    if selected_option == 3:
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

            if key == "courier":
                display_list_with_index(couriers)
                selected_courier = int(input("Please select a courier: "))
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
    user_input = int(input("Please enter 0 to quit, 1 to manage menu, 2 to manage couriers and 3 to manage orders: "))

    if user_input == 0:
        write_file("data/products.txt", main_menu)
        write_file("data/couriers.txt", couriers)
        sys.exit()

    if user_input == 1:
        handle_menu_options()  # this calls the function that shows the menu options and handles them

    if user_input == 2:
        handle_courier_options()  # this calls the function that shows the courier options and handles them

    if user_input == 3:
        handle_order_options()  # this calls the function that shows the order options and handles them


def read_file(file_path):
    fileObj = open(file_path, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into a list
    fileObj.close()
    return words


def write_file(file_path, content):
    joined_string = "\n".join(content)
    file = open(file_path, 'w')
    file.write(joined_string)
    file.close()


main_menu = read_file("data/products.txt")

couriers = read_file("data/couriers.txt")

orders = []

order_statuses = ["PREPARING", "OUT_FOR_DELIVERY", "DELIVERED"]

show_main_menu()
