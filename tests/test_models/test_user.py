#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
import pep8
from models import user
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """tests the user class"""

    def setUp(self):
        """class atributes, kind of"""
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""

    def test_methods(self):
        """tests if attributes are strings"""
        this_user = User()
        self.assertTrue(type(this_user.email) == str)
        self.assertTrue(type(this_user.password) == str)
        self.assertTrue(type(this_user.first_name) == str)
        self.assertTrue(type(this_user.last_name) == str)

if __name__ == '__main__':
    unittest.main()