#!bin/python3
from .arguments import DateArgument, CollaboratorArgument, TitleArgument

class Operation():
    def __init__(self):
        self.arguments = []
    def request_arguments(self):
        for argument in self.arguments:
            argument.request_data_until_valid()
    
    def get_arguments(self):
        return [arg.get_data() for arg in self.arguments]

class ReadOperation(Operation):
    def __init__(self):
        super().__init__()
        date = DateArgument(True)
        collaborator = CollaboratorArgument(True)
        self.arguments = [date, collaborator]

class WriteOperation(Operation):
    def __init__(self):
        super().__init__()
        title = TitleArgument(False)
        date = DateArgument(True)
        collaborator = CollaboratorArgument(True)
        self.arguments = [title, date, collaborator]

class DeleteOperation(Operation):
    def __init__(self):
        super().__init__()
        title = TitleArgument(False)
        self.arguments = [title]

class ModifyOperation(Operation):
    def __init__(self):
        super().__init__()
        title = TitleArgument(False)
        date = DateArgument(True)
        collaborator = CollaboratorArgument(True)
        self.arguments = [title, date, collaborator]