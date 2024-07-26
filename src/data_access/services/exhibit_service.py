from src.data_access.repositories.exhibit_repo import ExhibitRepository
from src.models.exhibit import Exhibit
from src.models.landscape import Landscape
from src.data_access.database import database
from src.data_access.dictionaries import typedict
from sqlalchemy.inspection import inspect

class Exhibit_Service:
    def __init__(self):
        self.repo = ExhibitRepository(database.get_session())
        self.keylist = [[column.name,column.type] for column in inspect(Exhibit).c]

    def get_all(self):
        all = self.repo.get_all()
        print("Exhibits:")
        for item in all:
            print(item)


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
                            print('Which landscape will your exhibit have? Choose from:')
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
        exhibit = Exhibit(**self.args)
        try:
            self.repo.add(exhibit)
            print(f'The following exhibit was added to the database: {exhibit}')
        except:
            print("Something went wrong when you wanted to add the exhibit to the database")


    def delete(self, **kwargs):
        name = input("Which species would you like to delete?: ")
        self.repo.delete_species(**self.args)