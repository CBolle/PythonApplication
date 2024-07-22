from src.data_access.services.animal_service import Animal_Service

class View():
    def __init__(self):
        pass

    def display_menu(self):
        # Print all options here
        pass

    def add_animal(self):
       self.service = Animal_Service()
       self.service.add_animal()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_animal()
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                print("Exiting programm ...")
                break
            else:
                print("Invalid choice, please try again.")