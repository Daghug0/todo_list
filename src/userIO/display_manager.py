# This file contains a library to display the results of our queries

from utils import utils
import datetime
    
class DisplayManager:
    def __init__(self):
        self.row_sizes = {"idx" : 3,
                          "title" : 60,
                          "due_date" : 10,
                          "owner" : 25}
        self.line_size = sum(self.row_sizes.values()) + len(self.row_sizes) + 1
        self.row_separator = "|"
        self.line_separator = "-"

    def separate_line(self):
        print(self.line_size*"-")
    
    def value_to_string(self,value) -> str:
        if isinstance(value, str):
            return value
        if isinstance(value,int):
            return str(value)
        if isinstance(value, datetime.datetime):
            return utils.date_to_string(value)
        if isinstance(value, dict):
            return utils.user_to_string()

    def print_element(self, string_to_print : str,max_size : int) -> None:
        if (len(string_to_print) >= max_size):
            print(string_to_print[:max_size], end=self.row_separator)
        else:
            print(string_to_print + " "*(max_size - len(string_to_print)), end=self.row_separator)

    def begin_line(self) -> None:
        print(self.row_separator, end ="")
    
    def end_line(self) -> None:
        print("")

    def print_headline(self) -> None:
        self.begin_line()
        for title, max_size in self.row_sizes.items():
            self.print_element(title, max_size)
        self.end_line()
            
    def print_line(self, idx: int, document_to_display : dict):
        self.begin_line()
        for title, max_size in self.row_sizes.items():
            if title == "idx":
                value_to_display = idx
            else:
                value_to_display = document_to_display.get(title, "EMPTY")
            if value_to_display != "EMPTY":
                string_to_display = self.value_to_string(value_to_display)
                self.print_element(string_to_display, max_size)
            else:
                self.print_element("/", max_size)
        self.end_line()

    def create_table(self, documents_to_display : list):
        self.separate_line()
        self.print_headline()
        self.separate_line()
        for index, document in enumerate(documents_to_display):
            self.print_line(index, document)
            self.separate_line()