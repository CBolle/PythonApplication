from src.models.species import Species
import json

class SpeciesRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, species):
        self.db_session.add(species)
        self.db_session.commit()
    
    def getAll(self):
        return self.db_session.query(Species).all()
    
    def getAllActive(self):
        return self.db_session.query(Species).filter_by(active=True)
    
    def getById(self, species_id):
        return self.db_session.get(Species, species_id)
    
    def updateById(self, args, species_id):
        for key, value in args.items():
            if hasattr(self.getById(species_id), key):
                setattr(self.getById(species_id), key, value)
            else:
                print(f'Species does not have a field {key}.')
        self.db_session.commit()
    
    def deleteById(self, species_id):
        self.getById(species_id).active = False
        self.db_session.commit()