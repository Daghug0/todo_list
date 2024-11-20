#!bin/python3
# This file provides global variables and types, as well as tools used by other modules.

import datetime
from enum import Enum

class OperationType(Enum):
    READ = 1
    WRITE = 2
    DELETE = 3
    MODIFY = 4

def parse_date(string_date : str) -> datetime.datetime:
    splitted_string = string_date.split("/")
    #if there is more than 3 field detected, raise an error
    if len(splitted_string) != 3:
        raise ValueError("Wrong number of /")
    day = splitted_string[0]
    month = splitted_string[1]
    year = splitted_string[2]
    # Raise an error if the conversion has failed
    try :
        date = datetime.datetime(int(year), int(month), int(day))
    except ValueError as e:
        raise ValueError(f"Error parsing date: {e}")
    return date

#return date in DD/MM/YYYY format :
def date_to_string(date_object : datetime.datetime) -> str:
    return date_object.strftime('%d/%m/%Y')

def parse_collaborator(collaborator : str) -> tuple:
        string_splitted = collaborator.split(" ", 1)
        if (len(string_splitted) == 2):
            return string_splitted[0].lower(),string_splitted[1].lower()
        else :
            raise ValueError("Invalid collaborator format. Expected format: 'first_name last_name'.")