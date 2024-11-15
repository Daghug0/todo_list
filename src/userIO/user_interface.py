#!bin/python3

#This file provides services to ask to the user the operation he wants to perform and the corresponding arguments.

from utils import utils
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

class CollaboratorArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter an owner for your query (Firstname FamilyName) \n", is_option)
        self.id = utils.USER_ID

    def convert_to_object(self) -> utils.Name | None:
        string_splitted = self.string_argument.split(" ", 1)
        if (len(string_splitted) == 2):
            return utils.Name(string_splitted[0].lower(),string_splitted[1].lower())
        else :
            return None

class DateArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter a date for your query (DD/MM/YYYY) \n", is_option)
        self.id = utils.DATE_ID

    def convert_to_object(self) -> datetime.datetime:
        return utils.parse_date(self.string_argument)
    

class TitleArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter the title of the task \n", is_option)
        self.id = utils.TITLE_ID
        
#this function allow to get all the necessary arguments for the app to process it
def get_command() -> tuple[str, dict]:
    objects = {}
    match(input("Type your command (W)rite, (R)ead, (M)odify, (D)elete : ")):
        case "W" | "w":
            crud_operation = "write"
            arg_list = [TitleArgument(False), DateArgument(True), CollaboratorArgument(True)]
        case "R" | "r":
            crud_operation = "read"
            arg_list = [DateArgument(True), CollaboratorArgument(True)]
        case "M" | "m":
            crud_operation = "modify"
            arg_list = [TitleArgument(False), DateArgument(True), CollaboratorArgument(True)]
        case "D" | "d":
            crud_operation = "delete"
            arg_list = [TitleArgument(False)]
        case _:
            print("This instruction is not known, exiting...")
            exit()
    for arg in arg_list:
        object = arg.get_from_user()
        if object != None:
            objects[arg.id] = object
    return crud_operation, objects

def chose_task(list_length):
    print("Several tasks have been found corresponding to the title.")
    str_choice = input("Please choose one among the list by typing the number associated to a task \n")
    try :
        int_choice = int(str_choice)
    except ValueError:
        int_choice = -1
    while int_choice == -1:
        str_choice = input("choice not in the list, please try again\n")
        try :
            int_choice = int(str_choice)
        except ValueError:
            int_choice = -1
    return int_choice
    
def request_operation():
    while True:
        try:
            operation = get_valid_operation()
        except ValueError:
            continue
        break   
    return operation
def get_valid_operation():
    match(input("Choose an operation (W)rite, (R)ead, (M)odify, (D)elete : ")):
        case "W" | "w":
            crud_operation = "write"
        case "R" | "r":
            crud_operation = "read"
        case "M" | "m":
            crud_operation = "modify"
        case "D" | "d":
            crud_operation = "delete"
        case _:
            raise ValueError("This instruction is not known.")

def request_arguments(crud_operation):
    pass