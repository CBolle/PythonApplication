from src.views.view import View
from src.data_access.database import database
from src.app import App

class Main():
    def __init__(self):
        self.database = database
        self.app = App()


if __name__ == "__main__":
    main = Main()
    
    