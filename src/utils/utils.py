# This file provides global variables and types, as well as tools used by other modules.

import datetime

USER_ID = "user"
DATE_ID = "due_date"
TITLE_ID = "title"
IDX_ID = "idx"

def parse_date(string_date : str) -> datetime.datetime:
    splitted_string = string_date.split("/")
    #if there is more than 3 field detected, raise an error
    if len(splitted_string) != 3:
        return None
    day = splitted_string[0]
    month = splitted_string[1]
    year = splitted_string[2]
    # Raise an error if the conversion has failed
    try :
        date = datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return None
    return date

#return date in DD/MM/YYYY format :
def date_to_string(date_object : datetime.datetime) -> str:
    return date_object.strftime('%d/%m/%Y')

#return name in first_name last_name format :
def user_to_string(user_object : dict) -> str:
    first_name = user_object.get("first_name", "ERROR")
    last_name = user_object.get("last_name", "ERROR")
    if isinstance(first_name,str) and isinstance(last_name,str):
        return (first_name + " " + last_name)
    else :
        return ("ERROR")