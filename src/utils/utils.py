# This file provides global variables and types, as well as tools used by other modules.

import datetime
from enum import Enum

class OperationType(Enum):
    READ = 1
    WRITE = 2
    DELETE = 3
    MODIFY = 4

USER_ID = "collaborator_name"
DATE_ID = "due_date"
TITLE_ID = "title"
IDX_ID = "idx"

def parse_date(string_date : str) -> datetime.datetime:
    splitted_string = string_date.split("/")
    #if there is more than 3 field detected, raise an error
    if len(splitted_string) != 3:
        return None
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
        string_splitted = collaborator.string_argument.split(" ", 1)
        if (len(string_splitted) == 2):
            return string_splitted[0].lower(),string_splitted[1].lower()
        else :
            raise ValueError("Invalid collaborator format. Expected format: 'first_name last_name'.")
    
class Collaborator():
    def __init__(self, name):
        self.key = "collaborator_name"
        if isinstance(dict, name):
            self.init_from_dict(name)
        elif isinstance(str, name):
            self.first_name,self.last_name = parse_collaborator(name)
        else:
            raise SystemExit("Either string or dict must be provided.")
    def init_from_dict(self, dict_name : dict):
        if "first_name" in dict_name.keys() and "last_name" in dict_name.keys():
            self.first_name = dict_name["first_name"]
            self.last_name = dict_name["last_name"]
        else :
            raise ValueError("Invalid dictionary format. Expected keys: first_name and last_name.")

    def get_dict(self):
        return {"first_name": self.first_name, "last_name": self.last_name}
    def get_string(self):
        return self.first_name + " " + self.last_name

class Date():
    def __init__(self, date):
        self.key = "due_date"
        if isinstance(str,date):
            self.date = parse_date(date)
        elif isinstance(datetime.datetime, date):
            self.init_from_dict(date)
        else:
            raise SystemExit("Either string or datetime or dict_date must be provided.")

    def init_from_dict(self, date : datetime.datetime):
        self.date = date

    def get_object(self):
        return self.date
    def get_string(self):
        return date_to_string(self.date)
