#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import os
import pep8
import json


class TestFileStorage(unittest.TestCase):
    """tests file storage"""
    def setUp(self):
        """testing file path"""
        with open("file.json", 'w'):
            FileStorage._FileStorage__file_path = "file.json"
            FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """tests the instance"""
        self.assertIsInstance(storage, FileStorage)

if __name__ == '__main__':
    unittest.main()