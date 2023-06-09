#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from sys import float_info
import unittest
"""Tests for BaseModel"""


class TestBase(unittest.TestCase):
    """Test the base class"""
    def test_instance_creation(self):
        b0 = BaseModel()
        """Test the creation of an instance"""
        self.assertIsInstance(b0, BaseModel)
        self.assertIsInstance(b0.created_at, datetime)
        self.assertIsInstance(b0.updated_at, datetime)
        try: b0.id
        except NameError: self.fail('id not set')

    def test_save(self):
        """Test the save method"""
        b0 = BaseModel()
        prev_time = b0.updated_at
        sleep(float_info.min)
        b0.save()
        self.assertIsNot(prev_time, b0.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        b0 = BaseModel()
        b0_dict = b0.to_dict()
        self.assertIsInstance(b0_dict, dict)
        self.assertIsInstance(b0_dict['updated_at'], str)
        self.assertIsInstance(b0_dict['created_at'], str)

