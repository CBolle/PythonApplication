from src.data_access.repositories.food_repo import FoodRepository
from src.models.food import Food
from src.models.landscape import Landscape
from src.data_access.database import database
from src.data_access.services.service import Service
from sqlalchemy.inspection import inspect
import json

class FoodService(Service):
    def __init__(self):
        super().__init__()
        self.repo = FoodRepository(database.get_session())

    def getAllActive(self):
        all_food = self.repo.getAllActive()
        print("Food currently in your zoo:")
        for food in all_food:
            # print(json.dumps(food.toDict()))
            print(food.toDict())

    def add(self):
        self.args = self.getInputdict(Food)
        food = Food(**self.args)
        try:
            self.repo.add(food)
            print(f'The following food was added to the database:\n{food.toDict()}')
        except Exception as e:
            print(f"Something went wrong when you wanted to add the food to the database: {e}")

    def updateById(self):
        print("Please choose from the list below.")
        self.getAllActive()
        args, id = self.getUpdatedict(Food)
        self.repo.updateById(args, id)

    def deleteById(self):
        print("Please choose from the list below.")
        self.getAllActive()
        food_id = int(input('I choose to delete the food with id: '))
        self.repo.deleteById(food_id)