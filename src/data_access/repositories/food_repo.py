from src.models.food import Food
import json

class FoodRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, food):
        self.db_session.add(food)
        self.db_session.commit()
    
    def getAll(self):
        return self.db_session.query(Food).all()
    
    def getAllActive(self):
        return self.db_session.query(Food).filter_by(active=True)
    
    def getById(self, food_id):
        return self.db_session.get(Food, food_id)
    
    def updateById(self, args, food_id):
        for key, value in args.items():
            if hasattr(self.getById(food_id), key):
                setattr(self.getById(food_id), key, value)
            else:
                print(f'Food does not have a field {key}.')
        self.db_session.commit()
    
    def deleteById(self, food_id):
        self.getById(food_id).active = False
        self.db_session.commit()