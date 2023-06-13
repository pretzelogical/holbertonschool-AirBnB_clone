#!/usr/bin/python
from models.base_model import BaseModel
"""Place class that inherits from BaseModel"""


class Place(BaseModel):
    """Class that represents a place on earth"""
    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guests = int(0)
    price_by_night = int(0)
    latitude = int(0)
    longitude = int(0)
    amenity_ids = []
