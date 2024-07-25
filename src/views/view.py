class View():
    def __init__(self):
        pass

    def display_food_menu(self):
        pass

    def display_zookeeper_menu(self):
        pass

    def display_main_menu(self):
        print("Main Menu")
        print("1. Species")
        print("2. Animal")
        print("3. Feeding")
        print("4. Zookeeper")
        print("5. Exhibit")
        print("6. Exit the program")

    def display_sub_menu(self, menu_type):
        print("\n")
        if menu_type == "species":
            print("Species")
        elif menu_type == "animal":
            print("Animal")
        elif menu_type == "zookeeper":
            print("Zookeeper")
        elif menu_type == "feeding":
            print("Feeding")
        elif menu_type == "exhibit":
            print("Exhibit")
        else:
            print("Unknown Menu Type")
            return
            
        print("1. Add {}".format(menu_type))
        print("2. Delete {}".format(menu_type))
        print("3. Edit {}".format(menu_type))
        print("4. View all {}s".format(menu_type))
        print("5. Go Back")