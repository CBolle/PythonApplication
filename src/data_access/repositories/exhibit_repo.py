from src.models.exhibit import Exhibit
import json

class ExhibitRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, **args):
        new_exhibit = Exhibit(**args)
        self.db_session.add(new_exhibit)
        self.db_session.commit()
        field_dict = {**args}
        print('An exhibit was added to the database with the following fields:')
        print(json.dumps(field_dict, indent = 4))
        return new_exhibit
    
    def read(self, exhibit):
        pass

    def delete(self, **args):
        pass