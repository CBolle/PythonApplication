from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import importlib
import os
import pkgutil
from src.models.base import Base
from src.models.animal import Animal
from src.models.species import Species

class Database:
    DATABASE_URL = "mysql+pymysql://root:@localhost/zoo"

    def __init__(self):
        self.import_models()
        self.engine = create_engine(Database.DATABASE_URL)
        self.test_connection()
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = self.Session()
        self.imported_modules = []  # List to store imported module names

    def test_connection(self):
        try:
            with self.engine.connect() as connection:
                print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def import_models(self):
        models_path = os.path.join(os.path.dirname(__file__), 'models')
        print(models_path)
 
        for _, module_name, _ in pkgutil.iter_modules([models_path]):
            print(f"Found module: {module_name}")  # Print each detected module name
            if module_name != 'base':
                try:
                    importlib.import_module(f'src.models.{module_name}')
                    self.imported_modules.append(module_name)  # Store imported module name
                    print(f"imported module: {module_name}")
                except ImportError as e:
                    print(f"Error importing module {module_name}: {e}")
                    
    def get_session(self):
        return self.db

    def get_imported_modules(self):
        return ', '.join(self.imported_modules)  # Return the list of module names as a string

database = Database()

if __name__ == "__main__":
    database = Database()
    database.get_imported_modules()