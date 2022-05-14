import sys


def display_menu_options():
    print('''
    [1.] Print product list
    [2.] Create new product
    [3.] Update existing product
    [4.] Delete product 
    ''')


def display_main_menu():
    print(f"Current menu")
    print(*main_menu, sep="\n")


def display_menu_with_indexes():
    for index, value in enumerate(main_menu):
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


def show_main_menu():
    user_input = int(input("Please enter 0 to quit or 1 to manage menu: "))

    if user_input == 0:
        sys.exit()

    if user_input == 1:
        handle_menu_options()  # this calls the function that shows the menu options and handles them


main_menu = ["Espresso", "latte", "Iced Coffee", "Bagels",
             "Donuts", "Croissant", "Breakfast Sandwich",
             "Cupcakes", "pie"]

display_main_menu()
show_main_menu()
