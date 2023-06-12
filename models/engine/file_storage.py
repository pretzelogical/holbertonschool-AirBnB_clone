#!/usr/bin/python3
import json
import os
"""
FileStorage class
that serializes instances
to a JSON file and deserializes
JSON file to instances
"""


class FileStorage:
    """Serializes and deserializes instances"""
    __file_path = "saved.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """adds an obj and its key in the dict"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to __file_path"""
        with open(self.__file_path, 'w') as fp:
            out = {}
            for key, value in self.__objects.items():
                if value.__class__.__name__ == 'BaseModel':
                    out[key] = value.to_dict()
            json.dump(out, fp)

    def reload(self):
        """Deserializes __file_path to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)

