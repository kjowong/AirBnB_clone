#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
# from datetime import datetime
from uuid import uuid4
from models import storage
from datetime import datetime

format = '%Y-%m-%dT%H:%M:%S.%f'
class BaseModel():
    "class Base Model"
    def __init__(self, *args, **kwargs):
        if kwargs:
            if 'created_at' in kwargs:
                try:
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'], format)
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
        " updates public instance attribute with the current datetime"
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        " returns a dict containing all keys\values of the __dict __"
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict.update({'created_at': datetime.strftime((self.created_at), format)})
        try:
            new_dict.update({'updated_at': datetime.strftime((self.updated_at), format)})
        except:
            pass
        return new_dict

    def __str__(self):
        return "[{}] ({}){}".format(self.__class__.__name__, self.id, self.__dict__)
