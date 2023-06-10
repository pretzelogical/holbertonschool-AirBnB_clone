#!/usr/bin/python3
"""
Write a class FileStorage
that serializes instances
to a JSON file and deserializes
JSON file to instances
"""


class FileStorage:
    def __init__(self, __file_path, __objects, ):
        self.__file_path = __file_path
        self.__objects = __objects


    def all(self):
        """returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """adds an obj and its key in the dict"""
        self.__objects[f"{obj}"]