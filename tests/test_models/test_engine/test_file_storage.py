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
        with open("saved.json", 'w'):
            FileStorage._FileStorage__file_path = "saved.json"
            FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """tests the instance"""
        self.assertIsInstance(storage, FileStorage)

    def test__file_path(self):
        """tests for string and if it exists"""
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        """tests the all method"""
        new_obj = FileStorage()
        new_dict = new_obj.all()
        self.assertTrue(type(new_dict == dict))

    def test_new(self):
        """tests the new"""
        test_new = BaseModel()
        test_id = test_new.id
        FileStorage.save(test_new)
        self.assertIs(FileStorage._FileStorage__objects[f"BaseModel.{test_id}"], test_new)

    # def test_save(self):

if __name__ == '__main__':
    unittest.main()