# This file contains a library to display the results of our queries

from lib import common_types
import datetime
#constants for display max size of each element
ATTR_DISPLAY = {
    common_types.IDX_ID     : 3,
    common_types.TITLE_ID   : 60,
    common_types.DATE_ID    : 10,
    common_types.USER_ID    : 25
}
HEADLINE = {
    common_types.IDX_ID     : common_types.IDX_ID,
    common_types.TITLE_ID   : common_types.TITLE_ID,
    common_types.DATE_ID    : common_types.DATE_ID,
    common_types.USER_ID    : common_types.USER_ID
}

LINE_SIZE = ATTR_DISPLAY[common_types.IDX_ID] + ATTR_DISPLAY[common_types.TITLE_ID] + ATTR_DISPLAY[common_types.DATE_ID] + ATTR_DISPLAY[common_types.USER_ID] + 4

#This function prints all documents returned by a mongoDB query
def print_task_table(tasks_set : list)-> None:
    # print the number of elements found without consuming the cursor
    print(str(len(list(tasks_set.clone()))) + " task(s) have been found corresponding to your query : ")
    print("")
    format_line(HEADLINE)
    print("-"*LINE_SIZE)
    line_idx = 0
    for task in tasks_set:
        format_line(task, line_idx)
        #print(line_idx)
        line_idx += 1

#This function construct a single entry of the table displayed
def format_line(line_info : dict, line_idx : int = None) -> None:
    for key in HEADLINE.keys():
        if key == common_types.IDX_ID and line_idx != None:
            print("{:3d}|".format(line_idx), end="")
        else:
            format_key(key, line_info)
    print("")

#This function print an attribute on the displayed table with the right format
def format_key(key, values : any)-> None:
    if key in values.keys():
        if isinstance(values[key], str):
            raw_string = values[key]
        elif values[key] != None:
            match key:
                case "due_date":
                    raw_string = common_types.date_to_string(values[key])
                case "user":
                    raw_string = common_types.user_to_string(values[key])
        else:
            raw_string = ""
    else:
        raw_string = ""
    attr_len = len(raw_string)
    if attr_len > ATTR_DISPLAY[key]:
        print(raw_string[:ATTR_DISPLAY[key]-1]+"|")
    else:
        print(raw_string + " "*(ATTR_DISPLAY[key] - attr_len) + "|", end="")