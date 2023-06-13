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
        this_user.email = "test@gmail.com"
        this_user.password = "1234567"
        this_user.first_name = "Derek"
        this_user.last_name = "Webb"
        self.assertTrue(type(this_user.email) == str)
        self.assertTrue(type(this_user.password) == str)
        self.assertTrue(type(this_user.first_name) == str)
        self.assertTrue(type(this_user.last_name) == str)
        self.assertIsNotNone(this_user.email)
        self.assertIsNotNone(this_user.password)
        self.assertIsNotNone(this_user.first_name)
        self.assertIsNotNone(this_user.last_name)

if __name__ == '__main__':
    unittest.main()