#!/usr/bin/python3
""" creating Amenity Class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialization of self """
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
