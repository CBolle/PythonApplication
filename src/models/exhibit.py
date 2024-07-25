from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.landscape import Landscape

class Exhibit(Base):
    __tablename__ = 'exhibit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(Float)
    landscape = Column(Enum(Landscape), nullable=False)

    species = relationship('Species', back_populates='exhibit')

    __table_args__ = {'extend_existing': True}