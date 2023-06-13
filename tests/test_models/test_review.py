#!/usr/bin/python3
"""
testing the review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests the review class"""

    def test_review_instance(self):
        """tests if review is an instance of Basemodel"""
        test_review = Review()
        self.assertIsInstance(test_review, BaseModel)

    def test_review_name_type(self):
        """tests if review attributes are what they are suppost to be"""
        test2_review = Review()
        self.assertTrue(type(test2_review.text) == str)
        self.assertTrue(type(test2_review.place_id) == str)
        self.assertTrue(type(test2_review.user_id) == str)

if __name__ == '__main__':
    unittest.main()