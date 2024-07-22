from src.views.view import View
from src.data_access.database import Database

class Main():
    def __init__(self):
        self.database = Database()
        self.view = View()
        self.view.run()


if __name__ == "__main__":
    main = Main()