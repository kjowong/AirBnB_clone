#!/usr/bin/python3
""" review class that inherits from BaseModel"""
from models.base_model import BaseModel
from models.base_model import Place
from models.base_model import User


class Review(BaseModel):
    """ defining Review Class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initializing """
        if kwargs is not None:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
