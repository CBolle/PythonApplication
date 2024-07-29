from src.data_access.repositories.exhibit_repo import ExhibitRepository
from src.models.exhibit import Exhibit

from src.data_access.database import database
from src.data_access.services.service import Service

class ExhibitService(Service):
    def __init__(self):
        super().__init__()
        self.repo = ExhibitRepository(database.get_session())

    def getAll(self):
        all = self.repo.get_all()
        print("Exhibits:")
        for item in all:
            print(item)
        return all

    def getById(self, id):
        return self.repo.getbyid(id)

    def add(self):
        args = self.getInputdict(Exhibit)
        exhibit = Exhibit(**args)
        try:
            self.repo.add(exhibit)
            print(f'The following exhibit was added to the database: {exhibit}')
        except:
            print("Something went wrong when you wanted to add the exhibit to the database")

    def updateById(self):
        args, id = self.getupdatedict(Exhibit)
        exhibit = self.repo.getbyid(id)
        self.repo.updateById(args, exhibit)


    def delete(self, **kwargs):
        name = input("Which species would you like to delete?: ")
        self.repo.delete(**self.args)