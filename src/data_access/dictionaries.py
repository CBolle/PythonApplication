from sqlalchemy.types import String, Integer, Float, Enum, Date, Boolean
from sqlalchemy.inspection import inspect
from datetime import date
from enum import Enum
from src.models.landscape import Landscape


def typedict():
    types = [String, Integer, Float, Enum, Date, Boolean]
    pythontypes = [str, int, float, str, date, bool]
    typedict = {}
    for i in range(len(types)):
        typedict[types[i]] = pythontypes[i]
    return typedict

def getinputdict(Class):
    args = {}
    keylist = [[column.name,column.type] for column in inspect(Class).c]
    for i in range(len(keylist)):
        if keylist[i][0] == "id": #Add any other things if they should be auto-incremeneted
            continue

        keyname = keylist[i][0]
        keytype = keylist[i][1]
            
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
                                inputval = testinput
                                break
                            else:
                                print("Try again")
                    # add other enum classes in if-statements if necessary
                else:
                    inputval = typedict()[type_i](input(f'{keyname}: '))
                
        args[keyname] = inputval
    return args