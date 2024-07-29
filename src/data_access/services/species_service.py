from src.data_access.repositories.species_repo import SpeciesRepository
from src.models.species import Species
from src.models.landscape import Landscape
from src.data_access.database import database
from src.data_access.services.service import Service
from sqlalchemy.inspection import inspect
import json

class SpeciesService(Service):
    def __init__(self):
        super().__init__()
        self.repo = SpeciesRepository(database.get_session())

    def getAllActive(self):
        all_species = self.repo.get_all_active()
        print("Species currently in your zoo:")
        for species in all_species:
            print(json.dumps(species.toDict()))

    def add(self):
        self.args = self.getInputdict(Species)
        species = Species(**self.args)
        try:
            self.repo.add(species)
            print(f'The following species was added to the database:\n{json.dumps(self.args, indent = 4)}')
        except:
            print("Something went wrong when you wanted to add the species to the database.")

    def updateById(self):
        species = input("Which species would you like to update? Please choose from the list below.")
        print(self.repo.getAllActive())
        args, id = self.getUpdatedict(Species)
        species = self.repo.getById(id)
        self.repo.updateById(args, species)

    def delete(self):
        input("Which species would you like to delete? Please choose from the list below.")
        print(self.repo.get_all_active)
        species_id = int(input('I choose to delete the species with id: '))
        self.repo.delete(species_id)
