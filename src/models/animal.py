from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean, inspect
from sqlalchemy.orm import relationship, sessionmaker
from src.models.base import Base

class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    date_of_birth = Column(Date)
    species_id = Column(Integer, ForeignKey('species.id'))
    active = Column(Boolean, default=True)
    
    # Relationship to Species
    species = relationship('Species', back_populates='animal')

    __table_args__ = {'extend_existing': True}
    
    def getAge(self):
        return ((datetime.today() - self.date_of_birth))/365.25

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}