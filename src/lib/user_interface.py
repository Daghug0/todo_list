#!bin/python3

from lib import common_types, date_translation
#This function allow user to prompt his query
# Input     : None
# Output    : Command object initialized from prompted items

class Input_argument():
    def __init__(self, input_message : str, retry_message : str = "Wrong format. "):
        self.input_message = input_message
        self.retry_message = input_message + retry_message

    def convert_to_object(self):
        return True, self.string_argument
    
    def get_from_user(self):
        self.string_argument = input(self.input_message)
        if self.is_empty():
            return None
        self.object_argument = self.convert_to_object()
        while self.object_argument == None:
            self.string_argument = input(self.retry_message)
            if self.is_empty():
                return None
            else :
                self.object_argument = self.convert_to_object()
        return self.object_argument






        


    def is_empty(self):
        return self.string_argument == ""

class Person_argument(Input_argument):

class Date_argument(Input_argument):
    def __init__(self):
        Input_argument.__init__("Please enter the title of the task", "")
    

class Title_argument(Input_argument):
    def __init__(self):
        Input_argument.__init__("Please enter the title of the task", "")
    
    def 


class ID_argument(Input_argument):

    
        
        
        
def get_command():
    match(input("Type your command :(W)rite or (R)ead: ")):
        case "W" | "w":
            title = get_title()
            owner = get_owner()
            due_date = get_date()

            query = common_types.Readquery(owner, due_date)
            return query
            
        case "R" | "r":
            owner = get_owner()
            due_date = get_date()
            query = common_types.Readquery(owner, due_date)
            return query


    #owner = get_owner_from_user()
    owner = None
    due_date = get_date()
    cmd = common_types.UserCommand(owner, due_date)
    return cmd

def get_owner():
    string_owner = input('Type owner (only alpha characters)\n')
    if string_owner == "":
        return None
    string_splitted = string_owner.split(None, 1)
    isNameValid = (len(string_splitted) == 2)
    while not isNameValid:
        string_owner = input('Incorrect Name format, Type owner (with a space between firstname and family name)\n')
        if string_owner == "":
            return None
        string_splitted = string_owner.split(None, 1)
        isNameValid = (len(string_splitted) == 2)
    return common_types.Person(string_splitted[0],string_splitted[1])

def get_date():
    string_due_date = input('Type due date (format DD/MM/YYYY)\n')
    if (string_due_date) == "":
        return None
    else:
        isDateValid,due_date = date_translation.parse_date_from_string(string_due_date)
    while (not isDateValid):
        string_due_date = input('Incorrect date format, Type due date (format DD/MM/YYYY)\n')
        if (string_due_date) == "":
            return None
        else :
            isDateValid,due_date = date_translation.parse_date_from_string(string_due_date)
    return due_date