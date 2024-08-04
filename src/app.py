from src.views.view import View
from src.data_access.services.animal_service import AnimalService
from src.data_access.services.species_service import SpeciesService
from src.data_access.services.exhibit_service import ExhibitService
from src.data_access.services.servicedict import Servicedict
from src.data_access.database import database

class App():
    view = View()
    def __init__(self):
        while True:
            self.view.displayMainMenu()
            main_choice = int(input("Which menu would you like to visit?: "))

            if main_choice == 1:
                self.runOverviewMenu()
            elif main_choice == 2:
                self.runCrudMenus()
            elif main_choice == 3:
                database.close_session()
                print("Exiting the programm ...")
                break
            else:
                print("Invalid choice, please try again.")
         
    def runOverviewMenu(self):
        pass        

    def runCrudMenus(self):
        while True:
            self.view.displayCrudMenus()
            crud_choice = int(input("Which CRUD menu would you like to visit?: "))
            crud_choices = {1: "species", 2: "animal", 3: "zookeeper", 4: "exhibit", 5: "food"}
           
            if crud_choice in crud_choices:
                self.runCrudMenu(crud_choices[crud_choice])
            elif crud_choice == 6:
                break
            else:
                print("Invalid choice, please try again.")

    def runCrudMenu(self, menu_type):
        while True:
            services = Servicedict().servicedict()
            try:
                service = services[menu_type] 
                self.view.displayCrudMenu(menu_type)  
                choice = input("What action would you like to perform?: ")
            except:
                print("This service is not yet available, but will be in the near future.")
                break
            else:
                if choice == '1':
                    service.add()
                elif choice == '2':
                    service.deleteById()
                elif choice == '3':
                    service.updateById()
                elif choice == '4':
                    service.getAllActive()
                elif choice == '5':
                    break
                else:
                    print("Invalid choice, please try again.")
            
           

            