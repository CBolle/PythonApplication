from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float, Boolean, inspect
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.landscape import Landscape

class Species(Base):
    options = []
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    normal_name = Column(String(50))
    latin_name = Column(String(100))
    adult_food_daily = Column(Float)
    adult_after = Column(Float)
    landscape = Column(Enum(Landscape), nullable=False)
    exhibit_id = Column(Integer, ForeignKey('exhibit.id'))
    active = Column(Boolean, default=True)

    animal = relationship('Animal', back_populates='species')
    exhibit = relationship('Exhibit', back_populates='species')
    foodSpecies = relationship('FoodSpecies', back_populates='species')

    __table_args__ = {'extend_existing': True}

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}