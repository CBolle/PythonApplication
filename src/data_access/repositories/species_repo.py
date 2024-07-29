from src.models.species import Species
import json

class SpeciesRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, species):
        self.db_session.add(species)
        self.db_session.commit()
    
    def get_all(self):
        return self.db_session.query(Species).all()
    
    def get_all_active(self):
        return self.db_session.query(Species).filter_by(active=True)
    
    def get_by_id(self, species_id):
        return self.db_session.get(Species, species_id)
    
    def update(self, species_id, **kwargs):
        species = SpeciesRepository.get_by_id(species_id)
        for key, value in kwargs.items():
            if hasattr(species, key):
                setattr(species, key, value)
            else:
                print(f'Species does not have a field {key}.')
        self.db_session.commit()
    
    def delete(self, species_id):
        self.db_session.get(Species, species_id).active = False