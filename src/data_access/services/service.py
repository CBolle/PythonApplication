from sqlalchemy.types import String, Integer, Float, Enum, Date, Boolean
from sqlalchemy.inspection import inspect
from datetime import date, datetime
from enum import Enum
from src.models.landscape import Landscape
from src.models.food_type import FoodType


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
        keylist = [[column.name, column.type, bool(column.foreign_keys)] for column in inspect(Class).c]
        for i in range(len(keylist)):
            keyname = keylist[i][0]
            keytype = keylist[i][1]
            isforeignkey = keylist[i][2]

            if keyname in ["id", "active"]:  # Skip fields that do not require input
                continue
             
            for type_i in self.typedict.keys(): #Add types to dictionairies.py if your type is not found
                if isinstance(keytype, type_i):
                    if isforeignkey:
                        from src.data_access.services.servicedict import Servicedict
                        servicedict = Servicedict().servicedict()
                        service = servicedict[keyname[:-3]] #removes _id from the name
                        service.getAllActive()

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
                        if keyname == 'food_type':
                            print('Which food type will your exhibit have? Choose from:')
                            for name in FoodType.__members__:
                                print(name)
                            while True:
                                testinput = self.typedict[type_i](input(f'{keyname}: ')).upper()
                                if testinput in FoodType.__members__:
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
        # Collect key information as a list of lists: [name, type, is_foreign_key]
        keylist = [[column.name, column.type, bool(column.foreign_keys)] for column in inspect(Class).c]
        
        # Prompt for the ID to update
        id = int(input("Which id do you want to update?: "))

        while True:
            # Display available fields to update, excluding 'id' and 'active'
            print("Available fields to update:")
            available_fields = [keyname for keyname, _, _ in keylist if keyname not in ["id"]]
            if not available_fields:
                print("No fields available to update.")
                break
            for keyname in available_fields:
                print(f"- {keyname}")

            keyname = input("Enter the field name you want to update (or 'done' to finish): ").strip()
            if keyname == 'done':
                break
            
            # Find the key information from keylist
            key_info = next((item for item in keylist if item[0] == keyname), None)
            if not key_info:
                print("Invalid field name or field cannot be updated. Please try again.")
                continue
            
            keytype = key_info[1]
            isforeignkey = key_info[2]

            # Handle foreign key fields
            if isforeignkey:
                from src.data_access.services.servicedict import Servicedict
                servicedict = Servicedict().servicedict()
                service = servicedict.get(keyname[:-3])  # Removes _id from the name
                service.getAllActive()

            # Handle different types
            if isinstance(keytype, Enum):
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
            elif isinstance(keytype, Boolean):
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

    # def verifyInput(self, keytype, keyname):
    #     while True:
    #         try:
    #             userinput = self.typedict[type(keytype)](input(f'{keyname}: ').strip())
    #             return userinput
    #         except (ValueError, TypeError) as e:
    #             print(f"Invalid input. Error: {e}. Please try again.")

    def verifyInput(self, keytype, keyname):
        """
        Verifies and returns the user input based on the type of field.
        Handles different types like string, integer, float, date, and boolean.
        """
        while True:
            try:
                # Handling for SQLAlchemy Date type
                if isinstance(keytype, Date):
                    date_str = input(f'{keyname} (format YYYY-MM-DD): ').strip()
                    inputval = datetime.strptime(date_str, '%Y-%m-%d').date()
                # Handling for SQLAlchemy Enum type
                elif isinstance(keytype, Enum):
                    print(f'Valid options for {keyname}: {", ".join([e.name for e in keytype.enum_class])}')
                    enum_input = input(f'{keyname}: ').strip()
                    if enum_input in [e.name for e in keytype.enum_class]:
                        inputval = keytype.enum_class[enum_input]
                    else:
                        raise ValueError("Invalid enum value")
                else:
                    # General handling for other types
                    inputval = self.typedict[type(keytype)](input(f'{keyname}: ').strip())
                return inputval
            except (ValueError, TypeError) as e:
                print(f"Invalid input. Error: {e}. Please try again.")

