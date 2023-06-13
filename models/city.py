#!/usr/bin/python
from models.base_model import BaseModel
"""City class that inherits from BaseModel"""


class City(BaseModel):
    """Class that represents a city"""
    state_id = str()
    name = str()
