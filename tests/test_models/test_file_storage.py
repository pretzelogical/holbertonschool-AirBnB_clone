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
    with open("file.json", 'w'):
        FileStorage._FileStorage__file_path = "file.json"
        FileStorage._FileStorage__objects = {}