#!/usr/bin/python3
""" creating City Class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialization """
        if kwargs  is not None:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
