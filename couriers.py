class Courier:
    def __init__(self, database, main_menu):
        self.database = database
        self.main_menu = main_menu


    def display_courier_options(self):
        print('''
        [1.] Display courier
        [2.] Create new courier
        [3.] Update existing courier
        [4.] Delete courier 
        ''')

    # Display current courier
    def display_couriers(self):
        print("Current couriers")
        couriers = self.database.select("SELECT * FROM couriers")
        print(*couriers, sep="\n")

    def handle_courier_options(self):
        self.display_courier_options()
        selected_option = int(input("Select option 1, 2, 3 or 4 to proceed, 0 to main menu: "))

        # Back to main menu
        if selected_option == 0:
            self.main_menu()

        # Display courier
        if selected_option == 1:
            self.display_couriers()
            self.handle_courier_options()

        # Create new courier
        if selected_option == 2:
            new_courier_name = input("Enter courier name: ")
            new_courier_phone = input("Enter courier phone: ")

            sql = f"INSERT INTO couriers (name, phone) VALUES (%s, %s)"
            val = (new_courier_name, new_courier_phone)

            self.database.execute(sql, val)

            print("Courier added successfully")
            self.handle_courier_options()

        # Update existing courier
        if selected_option == 3:
            self.display_couriers()
            id_to_be_updated = int(input("Select the id of the courier you want to update: "))

            courier = self.database.selectSingle(f"SELECT * FROM couriers WHERE id = {id_to_be_updated}")
            if courier is None or len(courier) == 0:
                print(f"Courier with id {id_to_be_updated} does not exist")
                self.handle_courier_options()

            for key, value in courier.items():
                if key == "id":
                    continue

                new_value = input(f"Please enter {key}: ")
                if new_value == "":
                    new_value = value
                courier[key] = new_value

            sql = "UPDATE couriers SET name = %s, phone = %s WHERE id = %s"
            val = (courier['name'], courier['phone'], id_to_be_updated)

            self.database.execute(sql, val)

            print("Courier updated successfully")

            self.handle_courier_options()

        # Delete courier
        if selected_option == 4:
            self.display_couriers()
            id_to_be_deleted = int(input("Select the id of the courier you want to delete: "))
            courier = self.database.selectSingle(f"SELECT * FROM couriers WHERE id = {id_to_be_deleted}")
            if courier is None or len(courier) == 0:
                print(f"Courier with id {id_to_be_deleted} does not exist")
                self.handle_courier_options()

            sql = "DELETE from couriers WHERE id = %s"
            val = id_to_be_deleted

            self.database.execute(sql, val)

            print("Courier deleted successfully")
            self.handle_courier_options()