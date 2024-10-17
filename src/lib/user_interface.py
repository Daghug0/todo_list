#!bin/python3

#This file provides services to ask to the user the operation he wants to perform and the corresponding arguments.

from lib import common_types
import datetime

class InputArgument():
    def __init__(self, input_message : str, is_option : bool = True, retry_message : str = "Wrong format. "):
        self.input_message = input_message
        self.retry_message = retry_message + input_message
        self.is_option = is_option
        self.object_argument = None

    def convert_to_object(self) -> str | None:
        if self.string_argument == "":
            return None
        else:
            return self.string_argument
    
    def is_empty(self) -> bool:
        return self.string_argument == ""
    
    def get_from_user(self)-> dict:
        self.string_argument = input(self.input_message)
        if self.is_empty() and self.is_option:
            return None
        self.object_argument = self.convert_to_object()
        while self.object_argument == None:
            self.string_argument = input(self.retry_message)
            if self.is_empty() and self.is_option:
                return None
            else :
                self.object_argument = self.convert_to_object()
        return self.object_argument

class PersonArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter an owner for your query (Firstname FamilyName) \n", is_option)
        self.id = common_types.USER_ID

    def convert_to_object(self) -> dict:
        string_splitted = self.string_argument.split(" ", 1)
        if (len(string_splitted) == 2):
            return {'first_name': string_splitted[0].lower(), 'last_name': string_splitted[1].lower()}
        else :
            return None

class DateArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter a date for your query (DD/MM/YYYY) \n", is_option)
        self.id = common_types.DATE_ID

    def convert_to_object(self) -> datetime.datetime:
        return common_types.parse_date(self.string_argument)
    

class TitleArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter the title of the task \n", is_option)
        self.id = common_types.TITLE_ID
        

def get_command() -> tuple[str, list]:
    objects = {}
    match(input("Type your command :(W)rite or (R)ead: ")):
        case "W" | "w":
            crud_operation = "write"
            arg_list = [TitleArgument(False), DateArgument(True), PersonArgument(True)]
        case "R" | "r":
            crud_operation = "read"
            arg_list = [DateArgument(True), PersonArgument(True)]
        case _:
            print("This instruction is not known, exiting...")
            exit()
    for arg in arg_list:
        object = arg.get_from_user()
        if object != None:
            objects[arg.id] = object
    return crud_operation, objects
