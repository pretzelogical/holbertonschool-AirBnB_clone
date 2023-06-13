#!/usr/bin/python
from models.base_model import BaseModel
"""Review class that inherits from BaseModel"""


class Review(BaseModel):
    """Class that represents a review on a website"""
    place_id = str()
    user_id = str()
    text = str()
