from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database():
    DATABASE_URL = "mysql+pymysql://root:@localhost/zoo"

    def __init__(self):
        self.engine = create_engine(Database.DATABASE_URL)
        self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
        try:
        # Try to connect to the database
            with self.engine.connect() as connection:
                print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")