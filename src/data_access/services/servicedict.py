from data_access.services.animal_service import AnimalService
from data_access.services.exhibit_service import ExhibitService
from data_access.services.species_service import SpeciesService
from data_access.services.food_service import FoodService

class Servicedict():
    def servicedict(self):
        self.servicedict = {"animal": AnimalService(), "species": SpeciesService(), "exhibit": ExhibitService(), "food": FoodService()}
        return self.servicedict