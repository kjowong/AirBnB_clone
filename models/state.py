#!/usr/bin/python3
""" state class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """ defining state class """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialization self """
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
