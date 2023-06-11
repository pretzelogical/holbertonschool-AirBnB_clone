#!/usr/bin/python3
"""
Write a class User that inherits from BaseModel
"""
from base_model import BaseModel


class User(BaseModel):
    """declaring User class"""

    email = str()
    password = str()
    first_name = str()
    last_name = str()
