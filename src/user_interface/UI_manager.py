#!bin/python3

#This file provides services to ask to the user the operation he wants to perform and the corresponding arguments.
from .operations import ReadOperation, WriteOperation, DeleteOperation, ModifyOperation
from utils import utils, CustomType

class UIManager():
    def __init__(self):
        pass
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
    
    def request_and_get_idx(list_length : int) -> int:
        print("Several tasks have been found corresponding to the title.")
        str_choice = input("Please choose one among the list by typing the number associated to a task \n")
        while(True):
            try :
                int_choice = int(str_choice)
                if 0 > int_choice or int_choice >= list_length:
                    raise ValueError
            except ValueError:
                print("Not valid, please try again.")
                continue
            break
        return int_choice
    
    def request_all(self) -> None:
        self.request_operation_until_valid()
        self.operation.request_arguments()
        
                
    def request_operation_until_valid(self) -> str:
        while True:
            try:
                self.request_operation()
            except ValueError:
                continue
            break   
    
    def get_operation(self) -> int:
        if isinstance(self.operation, ReadOperation):
            return utils.OperationType.READ
        elif isinstance(self.operation, WriteOperation):
            return utils.OperationType.WRITE
        elif isinstance(self.operation, DeleteOperation):
            return utils.OperationType.DELETE
        elif isinstance(self.operation, ModifyOperation):
            return utils.OperationType.MODIFY
    
    def get_arguments_data(self) -> dict:
        data_list = self.operation.get_arguments()
        data_dict = {}
        for data in data_list:
            if isinstance(data, CustomType):
                data_dict[data.get_corresponding_key()] = data.get_object()
        return data_dict
    def request_operation(self) -> None:
        match(input("Choose an operation (W)rite, (R)ead, (M)odify, (D)elete : ")):
            case "W" | "w":
                self.operation = WriteOperation()
            case "R" | "r":
                self.operation = ReadOperation()
            case "M" | "m":
                self.operation = ModifyOperation()
            case "D" | "d":
                self.operation = DeleteOperation()
            case _:
                raise ValueError("This instruction is not known.")


