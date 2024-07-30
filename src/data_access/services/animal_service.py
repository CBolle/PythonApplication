from src.data_access.repositories.animal_repo import AnimalRepository
from src.models.animal import Animal
from src.data_access.database import database
from src.data_access.services.service import Service
from sqlalchemy.inspection import inspect
import json

class AnimalService(Service):
    def __init__(self):
        super().__init__()
        self.repo = AnimalRepository(database.get_session())

    def getAllActive(self):
        all_animals = self.repo.getAllActive()
        print("Animal currently in your zoo:")
        for animal in all_animals:
            # print(json.dumps(animal.toDict()))
            print(animal.toDict())

    def add(self):
        self.args = self.getInputdict(Animal)
        animal = Animal(**self.args)
        try:
            self.repo.add(animal)
            print(f'The following animal was added to the database:\n{json.dumps(self.args, indent = 4)}')
        except:
            print("Something went wrong when you wanted to add the animal to the database.")

    def updateById(self):
        print("Please choose from the list below.")
        print(self.getAllActive())
        args, id = self.getUpdatedict(Animal)
        self.repo.updateById(args, id)

    def deleteById(self):
        print("Please choose from the list below.")
        print(self.getAllActive())
        animal_id = int(input('I choose to delete the animal with id: '))
        self.repo.deleteById(animal_id)