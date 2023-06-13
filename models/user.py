#!/usr/bin/python3
"""
Write a class User that
inherits from BaseModel
"""
import BaseModel


class User(BaseModel):
    """User class declaration"""
    email = str()
    password = str()
    first_name = str()
    last_name = str()
