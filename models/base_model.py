#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""
Class BaseModel that defines all common attributes and
methods for other classes
"""


class BaseModel:
    """Declaration of BaseModel class"""
    def __init__(self, *args, **kwargs):
        """BaseModel constructor
        Kwargs can be passed a dictionary to use for construction
        """
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns the string given"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary of keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
