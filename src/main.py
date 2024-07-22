from src.views.view import View
from src.data_access.database import Database
from src.models.animal import Animal
import datetime

class Main():
    def __init__(self):
        self.database = Database()
        self.fruitvlieg = Animal(id=1, name="Niek", date_of_birth=datetime.date(2024, 7, 22), species_id=1)
        self.database.add(self.fruitvlieg)
        self.view = View()
        self.view.run()


if __name__ == "__main__":
    main = Main()
    
    