from src.data_access.repositories.exhibit_repo import ExhibitRepository
from src.models.exhibit import Exhibit

from src.data_access.database import database
from src.data_access.dictionaries import getinputdict
from sqlalchemy.inspection import inspect

class Exhibit_Service:
    def __init__(self):
        self.repo = ExhibitRepository(database.get_session())

    def get_all(self):
        all = self.repo.get_all()
        print("Exhibits:")
        for item in all:
            print(item)
        return all

    def getbyid(self, id):
        return self.repo.getbyid(id)

    def add(self):
        self.args = getinputdict(Exhibit)
        exhibit = Exhibit(**self.args)
        try:
            self.repo.add(exhibit)
            print(f'The following exhibit was added to the database: {exhibit}')
        except:
            print("Something went wrong when you wanted to add the exhibit to the database")

    def updatebyid(self, id):
        pass
        # exhibit = self.getbyid(id)
        # field = input()
        # exhibit.[field] = input(f"wat moet {field} worden")

    def delete(self, **kwargs):
        name = input("Which species would you like to delete?: ")
        self.repo.delete_species(**self.args)