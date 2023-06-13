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
"""tests for file stoage"""

class TestStorage(unittest.TestCase):
    """testing the storage class"""
    def test_file_path(self):
        """tests class attribute __file_path"""
        with open("file.json", 'w'):
            FileStorage._
