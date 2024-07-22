from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import importlib
import os
import pkgutil
from src.models.base import Base

class Database():
    DATABASE_URL = "mysql+pymysql://root:@localhost/zoo"

    def __init__(self):
        self.engine = create_engine(Database.DATABASE_URL)
        self.test_connection()
        self.import_models()
        Base.metadata.create_all(self.engine)
   
        
    def test_connection(self):
        try:
        # Try to connect to the database
            with self.engine.connect() as connection:
                print("Database connection successful!")
                self.db = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        except Exception as e:
            print(f"Database connection failed: {e}")

    def import_models(self):
        models_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')

        for module_info in pkgutil.iter_modules([models_path]):
            module_name = module_info.name
            if module_name != 'base':
                importlib.import_module(f'models.{module_name}')