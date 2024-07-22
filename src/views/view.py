class View():
    def __init__(self):
        pass

    def display_menu(self):
        # Print all options here
        pass

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                pass  #add controller commands here such as controller.show_zookeeper()
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                print("Exiting programm ...")
                break
            else:
                print("Invalid choice, please try again.")