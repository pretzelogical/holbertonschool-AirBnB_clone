#!/usr/bin/python3
from models.base_model import BaseModel
"""User class that inherits from BaseModel"""


class User(BaseModel):
    """User class declaration"""
    email = str()
    password = str()
    first_name = str()
    last_name = str()
