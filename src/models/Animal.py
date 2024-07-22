from datetime import datetime

# Dit hieronder is wat ChatGPT suggereert qua structuur: sqlalchemy package inladen en dan op deze manier de relaties duidelijk maken.



# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, sessionmaker

# Base = declarative_base()

# class Species(Base):
#     __tablename__ = 'species'
#     species_id = Column(Integer, primary_key=True)
#     life_span = Column(Integer)
#     color = Column(String)

#     # Optional: Add a relationship to Animal for easy access
#     animals = relationship('Animal', back_populates='species')

# class Animal(Base):
#     __tablename__ = 'animals'
#     id = Column(Integer, primary_key=True)
#     date_of_birth = Column(Date)
#     species_id = Column(Integer, ForeignKey('species.species_id'))
    
#     # Relationship to Species
#     species = relationship('Species', back_populates='animals')

#     def get_life_span(self):
#         return self.species.life_span

# # Example setup and usage

# # Create an SQLite database in memory
# engine = create_engine('sqlite:///:memory:')
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# # Create species
# lion = Species(species_id=1, life_span=15, color='yellow')
# elephant = Species(species_id=2, life_span=60, color='gray')

# # Add species to the database
# session.add(lion)
# session.add(elephant)
# session.commit()

# # Create animals
# leo = Animal(date_of_birth='2010-06-15', species_id=1)  # Referencing species_id
# dumbo = Animal(date_of_birth='2015-03-20', species_id=2)  # Referencing species_id

# # Add animals to the database
# session.add(leo)
# session.add(dumbo)
# session.commit()

# # Query and use models
# leo_from_db = session.query(Animal).filter_by(id=leo.id).one()
# dumbo_from_db = session.query(Animal).filter_by(id=dumbo.id).one()

# print(f"Leo's species life span: {leo_from_db.get_life_span()} years")  # Output: 15
# print(f"Dumbo's species life span: {dumbo_from_db.get_life_span()} years")  # Output: 60
















class Animal():
    # ChatGPT raadt de package sqlalchemy aan, dan ziet deze init er zo uit:
    # species_id = Column(Integer, ForeignKey('species.id'))
    # 









    def __init__(self, species_id, last_fed, date_of_birth):
        self.species_id = species_id
        self.last_fed = last_fed
        self.age = self.calculate_age(date_of_birth)
        self.size_factor = self.age/self.species_id.adult_after
    
    def calculate_age(self, birthdate):
        return ((datetime.today() - birthdate).days)/365.25