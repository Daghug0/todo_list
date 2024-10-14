#!bin/python3

from dateutil import parser
import datetime

def parse_date_from_string(string_date):
    splitted_string = string_date.split("/")
    #if there is more than 3 field detected, raise an error
    if len(splitted_string) != 3:
        return False, None
    day = splitted_string[0]
    month = splitted_string[1]
    year = splitted_string[2]
    # Raise an error if the conversion has failed
    try :
        date = datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False, None
    return True, date

#print date in DD/MM/YYYY format :
def to_string(self):
    self.strftime('%d/%m/%Y')