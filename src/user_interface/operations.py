#!bin/python3
from arguments import DateArgument, CollaboratorArgument, TitleArgument

class Operation():
    def __init__(self):
        self.arguments = []
    def request_arguments(self):
        for argument in self.arguments:
            argument.request_data_until_valid()
    
    def get_arguments(self):
        return [arg.get_data() for arg in self.arguments]

class ReadOperation():
    def __init__(self):
        super().__init__()
        date = DateArgument(True)
        collaborator = CollaboratorArgument(True)
        self.arguments = [date, collaborator]    
