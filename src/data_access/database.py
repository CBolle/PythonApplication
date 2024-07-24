from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import importlib
import os
import pkgutil
from src.models.base import Base

class Database:
    DATABASE_URL = "mysql+pymysql://root:@localhost/zoo"

    def __init__(self):
        self.engine = create_engine(Database.DATABASE_URL)
        self.test_connection()
        self.import_models()
        Base.metadata.create_all(self.engine)
        self.db = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def test_connection(self):
        try:
            with self.engine.connect() as connection:
                print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def import_models(self):
        models_path = os.path.join(os.path.dirname(__file__), 'models')

        for _, module_name, _ in pkgutil.iter_modules([models_path]):
            if module_name not in ['__init__', 'base']:
                try:
                    print(f"imported module: {module_name}")
                    importlib.import_module(f'src.models.{module_name}')
                except ImportError as e:
                    print(f"Error importing module {module_name}: {e}")
    def get_session(self):
        return self.db
        
database = Database()