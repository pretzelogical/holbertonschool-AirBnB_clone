#!/usr/bin/python3
"""
testing the city class
"""
import unittest
import pep8
from models.state import City
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests the city class"""

    def test_city_instance(self):
        """tests if user is an instance of Basemodel"""
        test_city = City()
        self.assertIsInstance(test_city, BaseModel)

    def test_state_name_type(self):
        """tests if states name is a string"""
        test2_city = City()
        self.assertTrue(type(test2_city.name) == str)
        self.assertTrue(type(test2_city.state_id) == str)


if __name__ == '__main__':
    unittest.main()