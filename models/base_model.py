#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
import datetime
import uuid


class BaseModel:
    "class Base Model"


    def save(self):
        " updates public instance attribute with the current datetime"

    def to_json(self):
        " returns a dict containing all keys\values of the __dict __"

    def __str__(self):
        
