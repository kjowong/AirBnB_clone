#!/usr/bin/python3
""" creating User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initialization """
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
