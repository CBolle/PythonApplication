# from src.models.species import Species
from src.data_access.repositories.species_repo import SpeciesRepository, Species
from src.data_access.database import database
from sqlalchemy.inspection import inspect
from sqlalchemy.types import String, Integer, Date

class Species_Service:
    def __init__(self):
        self.speciesRepo = SpeciesRepository(database.db())
        self.keylist = [[column.name,column.type] for column in inspect(Species).c]

    def add(self, **kwargs):
        self.inputs = []
        self.keys = []
        self.args = {}
        
        for i in range(len(self.keylist)):
            keyname = self.keylist[i][0]
            keytype = self.keylist[i][1]
            self.keys.append(keyname)
            if isinstance(keytype, String):
                self.inputs.append(input(f'{self.keys[i]}: '))
            elif isinstance(keytype, Integer):
                self.inputs.append(int(input(f'{self.keys[i]}: ')))
            # zet hier later meer types neer
            self.args[self.keys[i]] = self.inputs[i]
        
        self.speciesRepo.add_species(**self.args)