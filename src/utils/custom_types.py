#!bin/python3
from utils import parse_date, parse_collaborator, date_to_string
import datetime

class CustomType():
    def __init__(self):
        self.key = None
    def get_corresponding_key(self) -> str:
        return self.key

class Collaborator(CustomType):
    def __init__(self, name):
        super().__init__()
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
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Date(CustomType):
    def __init__(self, date):
        super().__init__()
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
    def __str__(self):
        return date_to_string(self.date)

class Title(CustomType):
    def __init__(self, title):
        super().__init__()
        self.key = "title"
        if isinstance(str, title):
            self.title = title
        else: 
            raise SystemExit("String must be provided.")
    def __str__(self):
        return self.title