from data_access.repositories.species_repo import SpeciesRepository
from models.species import Species
from models.landscape import Landscape
from data_access.database import database
from data_access.services.service import Service
from sqlalchemy.inspection import inspect
import json

class SpeciesService(Service):
    def __init__(self):
        super().__init__()
        self.repo = SpeciesRepository(database.get_session())

    def getAllActive(self):
        all_species = self.repo.getAllActive()
        print("Species currently in your zoo:")
        for species in all_species:
            # print(json.dumps(species.toDict()))
            print(species.toDict())

    def add(self):
        self.args = self.getInputdict(Species)
        species = Species(**self.args)
        try:
            self.repo.add(species)
            print(f'The following species was added to the database:\n{json.dumps(self.args, indent = 4)}')
        except:
            print("Something went wrong when you wanted to add the species to the database.")

    def updateById(self):
        print("Please choose from the list below.")
        self.getAllActive()
        args, id = self.getUpdatedict(Species)
        self.repo.updateById(args, id)

    def deleteById(self):
        print("Please choose from the list below.")
        self.getAllActive()
        species_id = int(input('I choose to delete the species with id: '))
        self.repo.deleteById(species_id)