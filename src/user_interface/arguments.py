#!bin/python3

from utils import Collaborator, Date

class InputArgument():
    def __init__(self, input_message : str, is_option : bool = True, retry_message : str = "Wrong format. "):
        self.input_message = input_message
        self.retry_message = retry_message + input_message
        self.is_option = is_option
        self.data = None
    
    def is_empty(self, input_string) -> bool:
        return input_string == ""
    
    def request_data_until_valid(self) -> None:
        while True:
            try:
                input_string = input(self.input_message)
                self.data = self.convert_string(input_string)
            except ValueError:
                continue
            break
    
    def get_data(self):
        return self.data
    
class CollaboratorArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter an owner for your query (Firstname FamilyName) \n", is_option)
    
    def convert_string(self, input_string : str) -> Collaborator:
        if super().is_empty(input_string) and self.is_option:
            return None
        else:
            return Collaborator(input_string)

class DateArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter a date for your query (DD/MM/YYYY) \n", is_option)

    def convert_string(self, input_string) -> Date | None:
        if super().is_empty(input_string) and self.is_option:
            return None
        else:
            return Date(input_string)
    

class TitleArgument(InputArgument):
    def __init__(self, is_option):
        InputArgument.__init__(self,"Please enter the title of the task \n", is_option)
    
    def convert_string(self, input_string) -> str | None:
        if super().is_empty(input_string):
            if self.is_option:
                return None
            else:
                raise ValueError("Title argument is mandatory")
        else:
            return input_string