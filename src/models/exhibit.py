from sqlalchemy import Column, Integer, Enum as SqlEnum, Float, inspect
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.landscape import Landscape

class Exhibit(Base):
    __tablename__ = 'exhibit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(Float)
    landscape = Column(SqlEnum(Landscape), nullable=False)

    species = relationship('Species', back_populates='exhibit')

    __table_args__ = {'extend_existing': True}

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    
    def __str__(self):
        return f"Exhibit(id={self.id}, area={self.area}, landscape={self.landscape})"