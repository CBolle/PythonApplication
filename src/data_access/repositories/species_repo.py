# from src.data_access.database import Database
from src.models.species import Species

class SpeciesRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_species(self, **args):
        new_species = Species(**args)
        self.db_session.add(new_species)
        self.db_session.commit()
        print('A species was added to the database with the following fields:')
        for (attribute, value) in new_species.__dict__.items():
            print(f'{attribute}: {value}')
        return new_species