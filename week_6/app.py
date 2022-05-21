from menu import Menu
from database import CafeDatabase

database = CafeDatabase()
menu = Menu(database)

menu.show_main_menu()
