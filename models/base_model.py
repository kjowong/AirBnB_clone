#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
from uuid import uuid4
from models import storage
from datetime import datetime


class BaseModel:
    """"class BaseModel"""
    format = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """ initialization self"""
        if kwargs:
            if 'created_at' in kwargs:
                try:
                    kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'],
                        self.format)
                except:
                    pass
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__ = kwargs
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        """ updates public instance attribute with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        """ returns a dict containing all keys\values of the __dict __ """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict.update(
            {'created_at': datetime.strftime((self.created_at), self.format)})
        try:
            new_dict.update({'updated_at': datetime.strftime(
                (self.updated_at), self.format)})
        except:
            pass
        return new_dict

    def __str__(self):
        """ printing string representation of BaseModel """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, str(self.id), self.__dict__)

    def __repr__(self):
        """ format __str__ """
        return self.__str__()
