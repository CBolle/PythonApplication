from data_access.repositories.exhibit_repo import ExhibitRepository
from models.exhibit import Exhibit

from data_access.database import database
from data_access.services.service import Service

class ExhibitService(Service):
    def __init__(self):
        super().__init__()
        self.repo = ExhibitRepository(database.get_session())

    def getAll(self):
        self.all = self.repo.getAll()
        print("Exhibits:")
        for item in self.all:
            print(item)
        return self.all
    
    def getAllActive(self):
        self.allActive = self.repo.getAllActive()
        print("Active Exhibits:")
        for item in self.allActive:
            print(item)
        return self.allActive
    

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
        self.getAll()
        args, id = self.getUpdatedict(Exhibit)
        self.repo.updateById(args, id)


    def deleteById(self):
        self.getAllActive()    
        id = input("Which item would you like to delete (id): ")
        self.repo.deleteById(id)