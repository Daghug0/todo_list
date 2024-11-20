import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'src')))

import unittest
from src.utils import Collaborator, Date, Title
import datetime

class TestCollaborator(unittest.TestCase):
    def test_collaborator_init_with_name(self):
        collaborator = Collaborator("John Doe")
        self.assertEqual(str(collaborator), "john doe")
    
    def test_collaborator_init_with_dict(self):
        expected_result = {"first_name": "john", "last_name": "doe"}
        collaborator = Collaborator({   "first_name" : "John",
                                        "last_name" : "Doe"})
        self.assertEqual(collaborator.get_object(), expected_result) 
    def test_collaborator_init_with_invalid_dict_key(self):
        with self.assertRaises(ValueError):
            collaborator = Collaborator({"invalid_key" : "John Doe"})
    def test_collaborator_init_with_invalid_dict_value(self):
        with self.assertRaises(ValueError):
            collaborator = Collaborator({"first_name" : 123,
                                        "last_name" : "Doe"})
    def test_collaborator_get_corresponding_key(self):
        collaborator = Collaborator("John Doe")
        self.assertEqual(collaborator.get_corresponding_key(), "collaborator_name")

class TestDate(unittest.TestCase):
    def test_date_init_with_valid_string(self):
        date = Date("01/01/2022")
        self.assertEqual(str(date), "01/01/2022")
    def test_date_init_with_valid_datetime(self):
        date = Date(datetime.datetime(2022, 1, 1))
        self.assertEqual(date.get_object(), datetime.datetime(2022, 1, 1))

class TestTitle(unittest.TestCase):
    def test_title_init_with_valid_string(self):
        title = Title("Test Title")
        self.assertEqual(str(title), "Test Title")
    def test_title_init_with_invalid_input(self):
        with self.assertRaises(SystemExit):
            title = Title(123)