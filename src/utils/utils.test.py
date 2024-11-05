import unittest
from datetime import datetime
from utils import parse_date

class TestParseDate(unittest.TestCase):
    def test_parse_valid_date(self):
        input_date = "25/12/2023"
        expected_output = datetime(2023, 12, 25)
        self.assertEqual(parse_date(input_date), expected_output)

    def test_parse_date_with_more_than_three_fields(self):
        input_date = "25/12/2023/extra"
        self.assertIsNone(parse_date(input_date))

    def test_parse_date_with_fewer_than_three_fields(self):
        input_date = "25/12"
        self.assertIsNone(parse_date(input_date))

    def test_parse_date_with_non_numeric_values(self):
        input_date = "25/Dec/2023"
        self.assertIsNone(parse_date(input_date))

    def test_parse_date_with_leading_zeros(self):
        input_date = "01/02/2023"
        expected_output = datetime(2023, 2, 1)
        self.assertEqual(parse_date(input_date), expected_output)

if __name__ == '__main__':
    unittest.main()


