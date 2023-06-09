#!/usr/bin/python3
"""
Write a class BaseModel that
defines all common attributes
/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel():
    """Declaration of BaseModel class"""

    def __init__(self):
        """BaseModel constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the string given"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary of keys/values"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
