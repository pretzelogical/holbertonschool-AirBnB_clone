#!/usr/bin/python3
"""
testing the amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests the amenity class"""
    def test_amenity_instance(self):
        """tests if amenity is an instance of Basemodel"""
        test_amenity = Amenity()
        self.assertIsInstance(test_amenity, BaseModel)

    def test_amenity_name_type(self):
        """tests if amenity name is a string"""
        test2_amenity = Amenity()
        self.assertTrue(type(test2_amenity.name) == str)


if __name__ == '__main__':
    unittest.main()