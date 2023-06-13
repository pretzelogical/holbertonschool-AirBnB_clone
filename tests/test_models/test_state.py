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
        test_state = State()
        self.assertIsNotNone(test_state)

if __name__ == '__main__':
    unittest.main()