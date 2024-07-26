from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import importlib
import os
import pkgutil
from src.models.base import Base
from src.models.animal import Animal
from src.models.species import Species
from src.models.exhibit import Exhibit
from src.models.landscape import Landscape

class Database:
    DATABASE_URL = "mysql+pymysql://root:@localhost/zoo"

    def __init__(self):
        self.engine = create_engine(Database.DATABASE_URL)
        self.test_connection()

    def test_connection(self):
        try:
            with self.engine.connect() as connection:
                print("Database connection successful!")
                Base.metadata.create_all(self.engine)
                self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
                self.db = self.Session()
        except Exception as e:
            print(f"Database connection failed: {e}")
                    
    def get_session(self):
        return self.db

    def close_session(self):
        self.db.close()

database = Database()

if __name__ == "__main__":
    database.get_imported_modules()