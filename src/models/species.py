from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker
from src.models.base import Base

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    life_span = Column(Integer)

    animals = relationship('Animal', back_populates='species')

    __table_args__ = {'extend_existing': True}
    