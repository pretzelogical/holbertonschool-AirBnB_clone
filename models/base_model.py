#!/usr/bin/python3
"""
Write a class BaseModel that
defines all common attributes
/methods for other classes
"""
import uuid
import datetime

class BaseModel():
    """Declaration of BaseModel class"""
    def __init__(self, id, created_at, updated_at):
        self.__id = id
        self.__created_at = created_at
        self.__updated_at = updated_at

    def id(self):
        self.__id = str(uuid.uuid4())
        return self.__id
