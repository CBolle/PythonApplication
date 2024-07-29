from src.models.exhibit import Exhibit
import json

class ExhibitRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, exhibit):
        self.db_session.add(exhibit)
        self.db_session.commit()

    def getAll(self):
        return self.db_session.query(Exhibit).all()

    def getById(self, id):
        return self.db_session.get(Exhibit, id)
    
    def updateById(self, args, exhibit):
        for key, value in args.items():
            if hasattr(exhibit, key):
                setattr(exhibit, key, value)
            else:
                print(f'Exhibit does not have a field {key}.')
        self.db_session.commit()


    def delete(self, **args):
        pass