import unittest
import unittest.mock
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from display_manager import DisplayManager

class TestDisplayManager(unittest.TestCase):
    def setUp(self):
        self.display_manager = DisplayManager()
    def test_value_to_string_with_string_input(self):
        display_manager = DisplayManager()
        input_string = "Test String"
        result = display_manager.value_to_string(input_string)
        self.assertEqual(result, input_string)

    def test_value_to_string_with_integer_input(self):
        display_manager = DisplayManager()
        input_integer = 42
        result = display_manager.value_to_string(input_integer)
        self.assertEqual(result, "42")

    def test_value_to_string_with_datetime_input(self):
        display_manager = DisplayManager()
        input_datetime = datetime.datetime(2023, 5, 15, 10, 30)
        expected_result = "2023-05-15"
        with unittest.mock.patch('utils.utils.date_to_string') as mock_date_to_string:
            mock_date_to_string.return_value = expected_result
            result = display_manager.value_to_string(input_datetime)
        self.assertEqual(result, expected_result)
        mock_date_to_string.assert_called_once_with(input_datetime)
    def test_value_to_string_with_dict_input(self):
        display_manager = DisplayManager()
        input_dict = {"name": "John Doe", "age": 30}
        expected_result = "John Doe (30)"
        with unittest.mock.patch('utils.utils.user_to_string') as mock_user_to_string:
            mock_user_to_string.return_value = expected_result
            result = display_manager.value_to_string(input_dict)
        self.assertEqual(result, expected_result)
        mock_user_to_string.assert_called_once_with()
        
    def test_value_to_string_with_empty_dict_input(self):
        display_manager = DisplayManager()
        input_dict = {}
        expected_result = "Empty User"
        with unittest.mock.patch('utils.utils.user_to_string') as mock_user_to_string:
            mock_user_to_string.return_value = expected_result
            result = display_manager.value_to_string(input_dict)
        self.assertEqual(result, expected_result)
        mock_user_to_string.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
