#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    "class Base Model"
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = str(datetime.now())

    def save(self):
        " updates public instance attribute with the current datetime"
        self.updated_at = str(datetime.now())

    def to_json(self):
        " returns a dict containing all keys\values of the __dict __"
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__)})
        return new_dict

    def __str__(self):
        return("[{}] ({}) {}". format(self.__class__, self.id, self.__dict__))
