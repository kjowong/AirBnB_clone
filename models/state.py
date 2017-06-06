#!/usr/bin/python3
""" state class that inherits from BaseModel"""
from models.base_model import BaseModel


class State:
    """ defining state class """
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
