#!/usr/bin/python3
""" creating City Class """
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """ Class City """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialization """
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
