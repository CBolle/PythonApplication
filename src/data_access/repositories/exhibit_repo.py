from src.models.exhibit import Exhibit
import json

class ExhibitRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, exhibit):
        self.db_session.add(exhibit)
        self.db_session.commit()

    def get_all(self):
        return self.db_session.query(Exhibit).all()


    def delete(self, **args):
        pass