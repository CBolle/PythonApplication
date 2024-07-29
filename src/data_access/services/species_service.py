from src.data_access.repositories.species_repo import SpeciesRepository
from src.models.species import Species
from src.models.landscape import Landscape
from src.data_access.database import database
from src.data_access.dictionaries import typedict
from sqlalchemy.inspection import inspect
import json

class SpeciesService:
    def __init__(self):
        self.repo = SpeciesRepository(database.get_session())
        self.keylist = [[column.name,column.type] for column in inspect(Species).c]

    def get_all_active(self):
        all_species = self.repo.get_all_active()
        print("Species currently in your zoo:")
        for species in all_species:
            print(json.dumps(species.to_dict()))


    def add(self):
        self.args = {}

        for i in range(len(self.keylist)):
            if self.keylist[i][0] == "id": #Add any other things if they should be auto-incremeneted
                continue

            keyname = self.keylist[i][0]
            keytype = self.keylist[i][1]
                
            for type_i in typedict().keys(): #Add types to dictionairies.py if your type is not found
                if isinstance(keytype, type_i):
                    if type(keytype).__name__ == "Enum":
                        if keyname == 'landscape':
                            print('Which landscape does your species prefer? Choose from:')
                            for name in Landscape.__members__:
                                print(name)
                            while True:
                                testinput = typedict()[type_i](input(f'{keyname}: ')).upper()
                                if testinput in Landscape.__members__:
                                    self.input = testinput
                                    break
                                else:
                                    print("Try again")
                        # add other enum classes in if-statements if necessary
                    else:
                        self.input = typedict()[type_i](input(f'{keyname}: '))
                    
            self.args[keyname] = self.input
        species = Species(**self.args)
        try:
            self.repo.add(species)
            print(f'The following species was added to the database:\n{json.dumps(self.args, indent = 4)}')
        except:
            print("Something went wrong when you wanted to add the species to the database.")

    def update_species(self):
        species = input("Which species would you like to update? Please choose from the list below.")
        print(self.repo.get_all_active)
        species_id = int(input('I choose to update the species with id: '))
        update_dict = {}
        keys = list(input('I want to update these fields (separate by comma): '))
        for key in keys:
            pass # use the getinputdict here!!!


    def delete(self):
        name = input("Which species would you like to delete? Please choose from the list below.")
        print(self.repo.get_all_active)
        species_id = int(input('I choose to delete the species with id: '))
        self.repo.delete(species_id)