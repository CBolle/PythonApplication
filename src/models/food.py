from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean, inspect, Enum
from sqlalchemy.orm import relationship, sessionmaker
from src.models.base import Base
from src.models.food_types import FoodType

class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True, autoincrement=True)
    food_type = Column(Enum(FoodType), nullable = False)
    active = Column(Boolean, default=True)
    
    # Relationship to Species
    foodSpecies = relationship('FoodSpecies', back_populates='food')

    __table_args__ = {'extend_existing': True}

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}