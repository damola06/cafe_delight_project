class Product:
    def __init__(self, database, main_menu):
        self.database = database
        self.main_menu = main_menu

    def display_product_options(self):
        print('''
            [1.] Display product
            [2.] Create new product
            [3.] Update existing product
            [4.] Delete product 
            ''')

    # Display current menu
    def display_products(self):
        print("Current menu")
        products = self.database.select("SELECT * FROM products")
        print(*products, sep="\n")

    def handle_product_options(self):
        self.display_product_options()
        selected_option = int(input("Select option 1, 2, 3 or 4 to proceed, 0 to main menu: "))

        # To quit app
        if selected_option == 0:
            self.main_menu()

        # Display product
        if selected_option == 1:
            self.display_products()
            self.handle_product_options()

        # Create new product
        if selected_option == 2:
            new_product_name = input("Enter product name: ")
            new_product_price = input("Enter product price: ")

            sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
            val = (new_product_name, new_product_price)

            self.database.execute(sql, val)

            print("Product added successfully")
            self.handle_product_options()

        # Update existing product
        if selected_option == 3:
            self.display_products()
            id_to_be_updated = int(input("Select the id of the item you want to update: "))

            product = self.database.selectSingle(f"SELECT * FROM products WHERE id = {id_to_be_updated}")
            if product is None or len(product) == 0:
                # product is empty
                print(f"Product with id {id_to_be_updated} does not exist")
                self.handle_product_options()

            for key, value in product.items():
                if key == "id":
                    continue

                new_value = input(f"Please enter {key}: ")
                if new_value == "":
                    new_value = value

                product[key] = new_value

            sql = "UPDATE products SET name = %s, price = %s WHERE id = %s"
            val = (product['name'], product['price'], id_to_be_updated)

            self.database.execute(sql, val)

            print("Product updated successfully")
            self.handle_product_options()

        # Delete product
        if selected_option == 4:
            self.display_products()
            id_to_be_deleted = int(input("Select the id of the product you want to delete: "))
            product = self.database.selectSingle(f"SELECT * FROM products WHERE id = {id_to_be_deleted}")
            if product is None or len(product) == 0:
                print(f"Product with id {id_to_be_deleted} does not exist")
                self.handle_product_options()

            sql = "DELETE from products  WHERE id = %s"
            val = id_to_be_deleted

            self.database.execute(sql, val)

            print("Product deleted successfully")
            self.handle_product_options()
