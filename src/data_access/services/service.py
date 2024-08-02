from sqlalchemy.types import String, Integer, Float, Date, Boolean, Enum as SQLEnum
from sqlalchemy.inspection import inspect
from datetime import date, datetime
from models.enumdict import Enumdict
from models.foodtype import FoodType

class Service():
    def __init__(self):
        self.types = [String, Integer, Float, SQLEnum, Date]
        self.pythontypes = [str, int, float, str, date]
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
                                 
            inputval = self.verifyInput(keytype, keyname, isforeignkey)      
            args[keyname] = inputval
        return args
    
    def getUpdatedict(self, Class):
        args = {}
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
            i = 1
            for keyname in available_fields:
                print(f"{i}. {keyname}")
                i+=1

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
            inputval = self.verifyInput(keytype, keyname, isforeignkey)
            
            args[keyname] = inputval
        
        return args, id
   
    def verifyInput(self, keytype, keyname, isforeignkey):
        if isforeignkey:
            from src.data_access.services.servicedict import Servicedict
            servicedict = Servicedict().servicedict()
            service = servicedict[keyname[:-3]] # Removes _id from the name
            service.getAllActive()
        while True:
            try:
                # Handling for SQLAlchemy Date type
                if isinstance(keytype, Date): #isinstance(DATE, Date)
                    date_str = input(f'{keyname} (format YYYY-MM-DD): ').strip()
                    inputval = datetime.strptime(date_str, '%Y-%m-%d').date()
                    return inputval
                elif isinstance(keytype, SQLEnum):
                    if keyname in Enumdict().enumdict():
                        print(f'Which {keyname} do you want? Choose from:')
                        Enumerator = Enumdict().enumdict().get(keyname)
                        print('\n'.join(Enumerator.__members__))
                        while True:
                            inputval = str(input(f'{keyname}: ')).upper()
                            if inputval in Enumerator.__members__:
                                return inputval
                            else:
                                print("Invalid choice, try again.")
                    else:
                        print("This enum type is not found")
                elif isinstance(keytype, Boolean):
                    while True:
                        user_input = input("Should this item be active (yes=1/no=0): ")
                        if user_input == '1':
                            return True
                        elif user_input == '0':
                            return False
                        else:
                            print("Invalid input. Please enter 1 for yes or 0 for no.")
                else:
                    # General handling for other types
                    inputval = self.typedict[type(keytype)](input(f'{keyname}: ').strip())
                    return inputval
            except (ValueError, TypeError) as e:
                print(f"Invalid input. Error: {e}. Please try again.")
        