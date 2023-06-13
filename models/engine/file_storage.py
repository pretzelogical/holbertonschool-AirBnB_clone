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
        return FileStorage.__objects

    def new(self, obj):
        """adds an obj and its key in the dict"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to __file_path"""
        with open(FileStorage.__file_path, 'w') as fp:
            out = {}
            for key in FileStorage.__objects:
                out[key] = FileStorage.__objects[key].to_dict()
            json.dump(out, fp)

    def reload(self):
        """Deserializes __file_path to __objects"""
        if os.path.exists(self.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                json_load = json.load(f)
                for key, value in json_load.items():
                    FileStorage.__objects[key] = eval(value['__class__'])(**value)
            return FileStorage.__objects
