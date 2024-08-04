from models.exhibit import Exhibit
import json

class ExhibitRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, exhibit):
        self.db_session.add(exhibit)
        self.db_session.commit()

    def getAll(self):
        return self.db_session.query(Exhibit).all()
    
    def getAllActive(self):
        return self.db_session.query(Exhibit).filter_by(active=True)

    def getById(self, id):
        return self.db_session.get(Exhibit, id)
    
    def updateById(self, args, id):
        exhibit = self.getById(id)
        for key, value in args.items():
            if hasattr(exhibit, key):
                setattr(exhibit, key, value)
            else:
                print(f'Exhibit does not have a field {key}.')
        self.db_session.commit()


    def deleteById(self, id):
        self.getById(id).active = False
        self.db_session.commit()