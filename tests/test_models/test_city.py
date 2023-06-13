#!/usr/bin/python3
"""
testing the city class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests the city class"""

    def test_city_instance(self):
        """tests if city is an instance of Basemodel"""
        test_city = City()
        self.assertIsInstance(test_city, BaseModel)

    def test_city_name_type(self):
        """tests if city name is a string"""
        test2_city = City()
        self.assertTrue(type(test2_city.name) == str)
        self.assertTrue(type(test2_city.state_id) == str)


if __name__ == '__main__':
    unittest.main()