from sqlalchemy.types import String, Integer, Float, Enum, Date
from datetime import date
from enum import Enum, auto

def typedict():
    types = [String, Integer, Float, Enum, Date]
    pythontypes = [str, int, float, str, date]
    typedict = {}
    for i in range(len(types)):
        typedict[types[i]] = pythontypes[i]
    return typedict