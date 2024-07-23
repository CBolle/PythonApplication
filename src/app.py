from src.views.view import View
from src.data_access.services.animal_service import *
from src.data_access.services.species_service import *

class App():
    view = View()
    def __init__(self):
        while True:
            self.view.display_main_menu()
            main_choice = int(input("Which menu would you like to visit?: "))
            choices = {1: "species", 2: "animal", 3: "feeding", 4: "zookeeper"}

            if main_choice in choices:
                self.run_submenu(choices[main_choice])
            elif main_choice == 5:
                print("Exiting the programm ...")
                break
            else:
                print("Invalid choice, please try again.")

    def run_submenu(self, menu_type):
        while True:
            self.view.display_sub_menu(menu_type)
            services = {"animal": Animal_Service(), "species": Species_Service()}
           
            try:
                service = services[menu_type]
            except:
                print("This service is not yet available.")
            
            choice = input("What action would you like to perform?: ")

            if choice == '1':
                service.add()
            elif choice == '2':
                # service.delete()
                pass
            elif choice == '3':
                # service.edit()
                pass
            elif choice == '4':
                # service.viewall()
                pass
            elif choice == '5':
                # Go Back to the main menu
                break
            else:
                print("Invalid choice, please try again 2.")