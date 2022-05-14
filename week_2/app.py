import sys


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


def display_main_menu():
    print(f"Current menu")
    print(*main_menu, sep="\n")


def display_courier():
    print(f"Current couriers")
    print(*couriers, sep="\n")


def display_menu_with_indexes():
    for index, value in enumerate(main_menu):
        print(index, value)


def display_courier_with_indexes():
    for index, value in enumerate(couriers):
        print(index, value)


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
        display_menu_with_indexes()  # this means calling the function created above
        index_to_be_updated = int(input("Select the index of the item you want to update: "))
        new_product_name = input("Enter new product name: ")
        main_menu[index_to_be_updated] = new_product_name
        handle_menu_options()

    if selected_option == 4:
        display_menu_with_indexes()
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
        display_courier_with_indexes()  # this means calling the function created above
        index_to_be_updated = int(input("Select the index of the courier you want to update: "))
        new_courier_name = input("Enter new courier name: ")
        couriers[index_to_be_updated] = new_courier_name
        handle_courier_options()

    if selected_option == 4:
        display_courier_with_indexes()
        index_to_be_deleted = int(input("Select the index of the courier you want to delete: "))
        couriers.pop(index_to_be_deleted)
        handle_courier_options()


def show_main_menu():
    user_input = int(input("Please enter 0 to quit, 1 to manage menu or 2 to manage couriers: "))

    if user_input == 0:
        write_file("data/products.txt", main_menu)
        write_file("data/couriers.txt", couriers)
        sys.exit()

    if user_input == 1:
        handle_menu_options()  # this calls the function that shows the menu options and handles them

    if user_input == 2:
        handle_courier_options()  # this calls the function that shows the courier options and handles them


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

show_main_menu()
