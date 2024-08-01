from models.landscape import Landscape
from models.foodtype import FoodType

class Enumdict():
    def enumdict(self):
        self.enumdict = {"landscape": Landscape, "food_type": FoodType}
        return self.enumdict