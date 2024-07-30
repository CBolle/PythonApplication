from sqlalchemy.types import String, Integer, Float, Enum, Date, Boolean
from sqlalchemy.inspection import inspect
from datetime import date
from enum import Enum
from src.models.landscape import Landscape


class Service():
    def __init__(self):
        self.types = [String, Integer, Float, Enum, Date, Boolean]
        self.pythontypes = [str, int, float, str, date, bool]
        self.typedict = self.fillTypedict()

    def fillTypedict(self):
        typedict = {}
        for i in range(len(self.types)):
            typedict[self.types[i]] = self.pythontypes[i]
        return typedict

    def getInputdict(self, Class):
        args = {}
        keylist = [[column.name,column.type] for column in inspect(Class).c]
        for i in range(len(keylist)):
            keyname = keylist[i][0]
            keytype = keylist[i][1]

            if keyname in ["id", "active"]:  # Skip fields that do not require input
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
                                    print("Invalid choice, try again.")
                        # add other enum classes in if-statements if necessary
                    else:
                        inputval = self.verifyInput(keytype, keyname)
                    
            args[keyname] = inputval
        return args
    
    def getUpdatedict(self, Class):
        args = {}
        keylist = {column.name: column.type for column in inspect(Class).c}
        id = int(input("Which id do you want to update?: "))

        while True:
            # Display available fields to update, excluding 'id' and 'active'
            print("Available fields to update:")
            available_fields = [keyname for keyname in keylist if keyname not in ["id"]]
            if not available_fields:
                print("No fields available to update.")
                break
            for keyname in available_fields:
                print(f"- {keyname}")

            keyname = input("Enter the field name you want to update (or 'done' to finish): ").strip()
            if keyname == 'done':
                break
            
            if keyname not in keylist or keyname in ["id"]:
                print("Invalid field name or field cannot be updated. Please try again.")
                continue
            
            keytype = keylist[keyname]
            if type(keytype).__name__ == "Enum":
                if keyname == 'landscape':
                    print('Which landscape will your exhibit have? Choose from:')
                    print('\n'.join(Landscape.__members__))
                    while True:
                        testinput = input(f'{keyname}: ').strip().upper()
                        if testinput in Landscape.__members__:
                            inputval = testinput
                            break
                        else:
                            print("Invalid choice, try again.")
                else:
                    print(f"Unsupported Enum type for field {keyname}.")
                    continue
            elif type(keytype).__name__ == "Boolean":
                inputval = self.getBooleanFromInput()
            else:
                inputval = self.verifyInput(keytype, keyname)
            args[keyname] = inputval
        return args, id

    def getBooleanFromInput(self):
        """
        Prompts the user to input 1 or 0 to set the boolean value. Converts 1 to True and 0 to False.
        """
        while True:
            user_input = input("Should this item be active (yes=1/no=0): ")
            
            if user_input == '1':
                return True
            elif user_input == '0':
                return False
            else:
                print("Invalid input. Please enter 1 for yes or 0 for no.")

    def verifyInput(self, keytype, keyname):
        while True:
            try: 
                userinput = self.typedict[type(keytype)](input(f'{keyname}: ').strip())
                return userinput
            except (ValueError, TypeError) as e:
                print(f"Invalid input. Error: {e}. Please try again.")