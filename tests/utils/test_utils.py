import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import datetime
from utils import date_to_string, parse_date, parse_collaborator

class TestDateToString(unittest.TestCase):
    def test_date_to_string_standard_date(self):
        test_date = datetime.datetime(2023, 6, 15)
        expected_result = "15/06/2023"
        self.assertEqual(date_to_string(test_date), expected_result)
    def test_date_to_string_single_digit(self):
        test_date = datetime.datetime(2023, 1, 1)
        expected_result = "01/01/2023"
        self.assertEqual(date_to_string(test_date), expected_result)
    def test_date_to_string_leap_year(self):
        leap_year_date = datetime.datetime(2024, 2, 29)
        result = date_to_string(leap_year_date)
        self.assertEqual(result, '29/02/2024')
    def test_date_to_string_non_datetime_object(self):
        non_datetime_object = "not a datetime"
        with self.assertRaises(AttributeError):
            date_to_string(non_datetime_object)
    
class TestParseDate(unittest.TestCase):
    def test_parse_date_nominal_case(self):
        test_date = "15/06/2023"
        expected_result = datetime.datetime(2023, 6, 15)
        self.assertEqual(parse_date(test_date), expected_result)
    
    def test_parse_date_more_than_three_fields(self):
        test_date = "01/02/2023/04"
        with self.assertRaises(ValueError):
            parse_date(test_date)
    
    def test_parse_date_less_than_three_fields(self):
        test_date = "01/2023"
        with self.assertRaises(ValueError):
            parse_date(test_date)
    
    def test_parse_date_invalid_month(self):
        test_date = "01/13/2023"
        with self.assertRaises(ValueError):
            parse_date(test_date)

class TestParseCollaborator(unittest.TestCase):
    def test_parse_collaborator_valid_input(self):
        collaborator = "John Doe"
        expected_result = ("john", "doe")
        self.assertEqual(parse_collaborator(collaborator), expected_result)
    def test_parse_collaborator_without_space(self):
        collaborator = "John"
        with self.assertRaises(ValueError):
            parse_collaborator(collaborator)
    def test_parse_collaborator_with_more_space(self):
        collaborator = "John de MontMirail"
        expected_result = ("john", "de montmirail")
        self.assertEqual(parse_collaborator(collaborator), expected_result)


if __name__ == '__main__':
    unittest.main()
