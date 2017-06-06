#!/usr/bin/python3
""" creating Place Class """
from models.base_model import BaseModel
from models.base_model import City
from models.base_model import User


class Place(BaseModel):
    """ Class User """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ initialization """
        if kwargs is not None:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
