from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from src.data_access.database import Database

Base = declarative_base()

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    life_span = Column(Integer)
    color = Column(String)

    animals = relationship('Animal', back_populates='species')

class Animal(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    date_of_birth = Column(Date)
    species_id = Column(Integer, ForeignKey('species.id'))
    
    # Relationship to Species
    species = relationship('Species', back_populates='animals')

    def get_life_span(self):
        return self.species.life_span
        
    def calculate_age(self, birthdate):
        return ((datetime.today() - birthdate).days)/365.25


