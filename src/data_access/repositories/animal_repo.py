from src.models.animal import Animal
import json

class AnimalRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, animal):
        self.db_session.add(animal)
        self.db_session.commit()
    
    def getAll(self):
        return self.db_session.query(Animal).all()
    
    def getAllActive(self):
        return self.db_session.query(Animal).filter_by(active=True)
    
    def getById(self, animal_id):
        return self.db_session.get(Animal, animal_id)
    
    def update(self, animal_id, **kwargs):
        animal = self.get_by_id(animal_id)
        for key, value in kwargs.items():
            if hasattr(animal, key):
                setattr(animal, key, value)
            else:
                print(f'Animal does not have a field {key}.')
        self.db_session.commit()
    
    def delete(self, species_id):
        self.db_session.get(Animal, species_id).active = False