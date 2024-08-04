from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.foodtype import FoodType  # Import if needed in this context
from models.landscape import Landscape  # Import if needed in this context

class FoodSpecies(Base):
    __tablename__ = 'food_species'
    food_id = Column(Integer, ForeignKey('food.id'), primary_key=True)
    species_id = Column(Integer, ForeignKey('species.id'), primary_key=True)

    # Define the relationships to the Food and Species classes
    food = relationship('Food', back_populates='foodSpecies')
    species = relationship('Species', back_populates='foodSpecies')

    def toDict(self):
        return {
            'food_id': self.food_id,
            'species_id': self.species_id
        }
