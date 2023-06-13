#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from time import sleep
from sys import float_info
import json
import unittest
import os
"""Tests for BaseModel"""


class TestBase(unittest.TestCase):
    """Test the base class"""

    def test_instance_creation(self):
        b0 = BaseModel()
        """Test the creation of an instance"""
        self.assertIsInstance(b0, BaseModel)
        self.assertIsInstance(b0.created_at, datetime)
        self.assertIsInstance(b0.updated_at, datetime)
        self.assertIsInstance(b0.id, str)
        test_time = datetime.fromisoformat('1987-03-03T14:05:01.985')
        b1 = BaseModel(id='test', created_at=test_time.isoformat(),
                       updated_at=test_time.isoformat())
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertIsInstance(b1.id, str)
        self.assertEqual(b1.created_at, test_time)

    def test_save(self):
        """Test the save method and also loading from that saved file"""
        if os.path.exists('saved.json'):
            os.remove('saved.json')
        FileStorage._FileStorage__objects.clear()
        b0 = BaseModel()
        prev_time = b0.updated_at
        sleep(float_info.min)
        b0.save()
        self.assertIsNot(prev_time, b0.updated_at)
        storage.reload()
        b0_dict = storage._FileStorage__objects[f"BaseModel.{b0.id}"].to_dict()
        print(b0_dict)
        b0_copy = BaseModel(**b0_dict)
        self.assertIsInstance(b0_copy, BaseModel)
        self.assertEqual(b0.id, b0_copy.id)
        self.assertEqual(b0.created_at, b0_copy.created_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        b0 = BaseModel()
        b0_dict = b0.to_dict()
        self.assertIsInstance(b0_dict, dict)
        self.assertIsInstance(b0_dict['updated_at'], str)
        self.assertIsInstance(b0_dict['created_at'], str)
        self.assertEqual(b0.id, b0_dict['id'])
        self.assertEqual(b0.__class__.__name__, b0_dict['__class__'])
        self.assertEqual(b0.updated_at.isoformat(), b0_dict['updated_at'])

    def test_recreate_instance(self):
        """Test if an instance can be recreated using to_dict()"""
        b0 = BaseModel()
        b3 = BaseModel(**b0.to_dict())
        self.assertEqual(b0.created_at, b3.created_at)
        self.assertEqual(b0.id, b3.id)

    def test__str__(self):
        """test to the __str__ method"""
        b0 = BaseModel()
        self.assertEqual(b0.__str__(), "[" + b0.__class__.__name__ + "]"
                         " (" + b0.id + ") " + str(b0.__dict__))
