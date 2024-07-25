from src.models.species import Species
import json

class SpeciesRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, **args):
        new_species = Species(**args)
        self.db_session.add(new_species)
        self.db_session.commit()
        field_dict = {**args}
        print('A species was added to the database with the following fields:')
        print(json.dumps(field_dict, indent = 4))
        return new_species
    
    def delete(self, **args):
        pass