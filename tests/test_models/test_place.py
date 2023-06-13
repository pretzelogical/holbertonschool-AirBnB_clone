#!/usr/bin/python3
"""
testing the place class
"""
import unittest
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests the place class"""

    def test_place_instance(self):
        """tests if place is an instance of Basemodel"""
        test_place = Place()
        self.assertIsInstance(test_place, BaseModel)

    def test_place_name_type(self):
        """tests if place attributes are what they are suppost to be"""
        test2_place = Place()
        self.assertTrue(type(test2_place.name) == str)
        self.assertTrue(type(test2_place.city_id) == str)
        self.assertTrue(type(test2_place.user_id) == str)
        self.assertTrue(type(test2_place.description) == str)
        self.assertTrue(type(test2_place.number_rooms) == int)
        self.assertTrue(type(test2_place.number_bathrooms) == int)
        self.assertTrue(type(test2_place.max_guests) == int)
        self.assertTrue(type(test2_place.price_by_night) == int)
        self.assertTrue(type(Place.latitude) == int)
        self.assertTrue(type(Place.longitude) == int)
        self.assertTrue(type(Place.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()