from sqlalchemy.types import String, Integer, Float, Enum, Date, Boolean
from sqlalchemy.inspection import inspect
from datetime import date
from enum import Enum
from src.models.landscape import Landscape


class Service():
    def __init__(self):
        self.types = [String, Integer, Float, Enum, Date, Boolean]
        self.pythontypes = [str, int, float, str, date, bool]
        self.typedict = {}
        self.filltypedict()

    def filltypedict(self):
        for i in range(len(self.types)):
            self.typedict[self.types[i]] = self.pythontypes[i]
        return self.typedict

    def getinputdict(self, Class):
        args = {}
        keylist = [[column.name,column.type] for column in inspect(Class).c]
        for i in range(len(keylist)):
            keyname = keylist[i][0]
            keytype = keylist[i][1]

            if keyname == "id" or keyname == "active": #Add any other things if they should be auto-incremeneted
                continue
             
            for type_i in self.typedict.keys(): #Add types to dictionairies.py if your type is not found
                if isinstance(keytype, type_i):
                    if type(keytype).__name__ == "Enum":
                        if keyname == 'landscape':
                            print('Which landscape will your exhibit have? Choose from:')
                            for name in Landscape.__members__:
                                print(name)
                            while True:
                                testinput = self.typedict[type_i](input(f'{keyname}: ')).upper()
                                if testinput in Landscape.__members__:
                                    inputval = testinput
                                    break
                                else:
                                    print("Try again")
                        # add other enum classes in if-statements if necessary
                    else:
                        inputval = self.typedict[type_i](input(f'{keyname}: '))
                    
            args[keyname] = inputval
        return args