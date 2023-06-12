#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
from sys import float_info
import json
import unittest
from models import storage


def test_load():
    print(storage._FileStorage__objects)

test_load()
