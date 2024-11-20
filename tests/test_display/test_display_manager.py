import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'src')))

import unittest
import unittest.mock
import datetime

from src.display.display_manager import DisplayManager

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
    

if __name__ == '__main__':
    unittest.main()
