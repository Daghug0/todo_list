import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import unittest.mock as mocker
from src.user_interface.arguments import InputArgument, CollaboratorArgument, DateArgument, TitleArgument
import datetime
class TestCollaboratorArgument(unittest.TestCase):
    def test_collaborator_convert_string_nominal(self):
        argument = CollaboratorArgument(False)
        result = argument.convert_string('John Doe')
        self.assertEqual(str(result), "john doe")
    def test_collaborator_convert_string_invalid(self):
        argument = CollaboratorArgument(False)
        with self.assertRaises(ValueError):
            argument.convert_string('Invalid')
    def test_collaborator_convert_string_mandatory_empty(self):
        argument = CollaboratorArgument(False)
        with self.assertRaises(ValueError):
            argument.convert_string('')
    def test_collaborator_convert_string_optional_empty(self):
        argument = CollaboratorArgument(True)
        self.assertIsNone(argument.convert_string(''))
    def test_collaborator_argument_request_data_nominal(self):
        argument = CollaboratorArgument(False)
        with mocker.patch('builtins.input', return_value='John Doe'):
            argument.request_data_until_valid()
        self.assertEqual(str(argument.get_data()), "john doe")
    def test_collaborator_argument_request_data_valid_input_after_retry(self):
        argument = CollaboratorArgument(False)
        with mocker.patch('builtins.input', side_effect=['123', 'John Doe']):
            argument.request_data_until_valid()
        self.assertEqual(str(argument.get_data()), "john doe")
    def test_collaborator_argument_request_data_option_empty_input(self):
        argument = CollaboratorArgument(True)
        with mocker.patch('builtins.input', return_value=""):
            argument.request_data_until_valid()
            self.assertIsNone(argument.get_data())
    def test_collaborator_argument_request_data_mandatory_empty_input(self):
        argument = CollaboratorArgument(False)
        with mocker.patch('builtins.input', side_effect=['123', 'John Doe']):
            argument.request_data_until_valid()
            self.assertEqual(str(argument.get_data()), "john doe")

class TestDateArgument(unittest.TestCase):
    def test_DateArgument_convert_string_nominal(self):
        argument = DateArgument(False)
        result = argument.convert_string('01/01/2022')
        self.assertEqual(str(result),'01/01/2022')
    def test_date_argument_convert_string_invalid(self):
        argument = DateArgument(False)
        with self.assertRaises(ValueError):
            argument.convert_string('31/02/2022')
    def test_date_argument_convert_string_mandatory_empty(self):
        argument = DateArgument(False)
        with self.assertRaises(ValueError):
            argument.convert_string('')
    def test_date_argument_convert_string_optional_empty(self):
        argument = DateArgument(True)
        self.assertIsNone(argument.convert_string(''))

class TestTitleArgument(unittest.TestCase):
    def test_title_argument_convert_string_nominal(self):
        argument = TitleArgument(False)
        result = argument.convert_string('Test Title')
        self.assertEqual(str(result), "Test Title")
    def test_title_argument_convert_string_mandatory_empty(self):
        argument = TitleArgument(False)
        with self.assertRaises(ValueError):
            argument.convert_string('')
    def test_title_argument_convert_string_optional_empty(self):
        argument = TitleArgument(True)
        self.assertIsNone(argument.convert_string(''))
        
