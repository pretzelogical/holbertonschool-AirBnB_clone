#!/usr/bin/python3
"""
testing the state class
"""
import unittest
import pep8
from models import state
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """tests the state class"""

    def test_state_instance(self):
        """tests if user is an instance of Basemodel"""
        test_state = State()
        self.assertIsInstance(test_state, BaseModel)

    def test_state_name_type(self):
        """tests if states name is a string"""
        test2_state = State()
        self.assertTrue(type(test2_state.name) == str)


if __name__ == '__main__':
    unittest.main()