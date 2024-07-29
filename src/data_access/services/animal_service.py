from src.data_access.repositories.species_repo import AnimalRepository
from src.models.animal import Animal
from src.models.landscape import Landscape
from src.data_access.database import database
from src.data_access.services.service import Service
from sqlalchemy.inspection import inspect
import json

class AnimalService(Service):
    def __init__(self):
        super().__init__()
        self.repo = AnimalRepository(database.get_session())

    def get_all_active(self):
        all_animals = self.repo.get_all_active()
        print("Species currently in your zoo:")
        for animal in all_animals:
            print(json.dumps(animal.to_dict()))


    def add(self):
        self.args = self.getinputdict(Animal)
        animal = Animal(**self.args)
        try:
            self.repo.add(animal)
            print(f'The following animal was added to the database:\n{json.dumps(self.args, indent = 4)}')
        except:
            print("Something went wrong when you wanted to add the animal to the database.")

    def update_species(self):
        species = input("Which animal would you like to update? Please choose from the list below.")
        print(self.repo.get_all_active())
        self.getupdatedict(Animal)


    def delete(self):
        name = input("Which animal would you like to delete? Please choose from the list below.")
        print(self.repo.get_all_active)
        animal_id = int(input('I choose to delete the animal with id: '))
        self.repo.delete(animal_id)