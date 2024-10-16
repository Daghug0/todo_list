#!bin/python3

from lib import common_types, date_translation
import datetime

class InputArgument():
    def __init__(self, input_message : str, is_option : bool = True, retry_message : str = "Wrong format. "):
        self.input_message = input_message
        self.retry_message = retry_message + input_message
        self.is_option = is_option
        self.object_argument = None

    def convert_to_object(self) -> str:
        return self.string_argument
    
    def is_empty(self) -> bool:
        return self.string_argument == ""
    
    def get_from_user(self):
        self.string_argument = input(self.input_message)
        if self.is_empty() and self.isOption:
            return None
        self.object_argument = self.convert_to_object()
        while self.object_argument == None:
            self.string_argument = input(self.retry_message)
            if self.is_empty() and self.isOption:
                return None
            else :
                self.object_argument = self.convert_to_object()
        return self.object_argument

class PersonArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter an owner for your query (Firstname FamilyName) \n", is_option)

    def convert_to_object(self) -> common_types.Person:
        string_splitted = self.string_argument.split(" ", 1)
        if (len(string_splitted) == 2):
            return common_types.Person(string_splitted[0].lower(),string_splitted[1].lower())
        else :
            return None

class DateArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter a date for your query (DD/MM/YYYY) \n", is_option)

    def convert_to_object(self) -> datetime.datetime:
        return date_translation.parse_date(self.string_argument)
    

class TitleArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter the title of the task \n", is_option)

    
        
        
        
def get_command():
    match(input("Type your command :(W)rite or (R)ead: ")):
        case "W" | "w":
            arg_list = [TitleArgument(False), DateArgument(True), PersonArgument(True)]
            object_list = []
            for arg in arg_list:
                object_list.append(arg.get_from_user())
            return object_list
            
        case "R" | "r":
            arg_list = [DateArgument(True), PersonArgument(True)]
            object_list = []
            for arg in arg_list():
                object_list.append(arg.get_from_user())
            #query = common_types.Readquery(*object_list)
            return object_list
