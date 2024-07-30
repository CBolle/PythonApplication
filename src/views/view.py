class View:
    def __init__(self):
        print("Welcome to the Zoo Management System")

    def displayOverviewMenu(self):
        pass

    def displayMainMenu(self):
        print("Main Menu")
        print("1. Overview")
        print("2. Database")
        print("3. Exit the programm")

    def displayCrudMenus(self):
        print("CRUD Menus")
        print("1. Species")
        print("2. Animal")
        print("3. Zookeeper")
        print("4. Exhibit")
        print("5. Food")
        print("6. Go Back")

    def displayCrudMenu(self, menuType):
        print("\n")
        if menuType == "species":
            print("Species")
        elif menuType == "animal":
            print("Animal")
        elif menuType == "zookeeper":
            print("Zookeeper")
        elif menuType == "exhibit":
            print("Exhibit")
        elif menuType == "food":
            print("food")
        else:
            print("Unknown Menu Type")
            return

        print("1. Add {}".format(menuType))
        print("2. Delete {}".format(menuType))
        print("3. Edit {}".format(menuType))
        print("4. View all {}s".format(menuType))
        print("5. Go Back")