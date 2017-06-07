#!/usr/bin/python3
""" File Storage to save an object to a file """
from datetime import datetime
import os
import json


class FileStorage():
    """ filestorage class """
    __file_path = './file.json'
    __objects = {}

    def all(self):
        """ defining all """
        return (FileStorage.__objects)

    def new(self, obj):
        """ defining new """
        name = str(obj.__class__.__name__)
        key = str(obj.id)
        new_obj = name + '.' + key
        FileStorage.__objects[new_obj] = obj

    def save(self):
        """ defining save """
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, 'w+', encoding='UTF8') as f:
            (json.dump(new_dict, f))

    def reload(self):
        """ defining reload """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF8") as f:
                load_value = json.load(f)
            for k in load_value.keys():
                if (load_value[k]['__class__'] == 'BaseModel'):
                    FileStorage.__objects[k] = BaseModel(**load_value[k])
                elif (load_value[k]['__class__'] == 'User'):
                    FileStorage.__objects[k] = User(**load_value[k])
                elif (load_value[k]['__class__'] == 'State'):
                    FileStorage.__objects[k] = State(**load_value[k])
                elif (load_value[k]['__class__'] == 'Amenity'):
                    FileStorage.__objects[k] = Amenity(**load_value[k])
                elif (load_value[k]['__class__'] == 'Place'):
                    FileStorage.__objects[k] = Place(**load_value[k])
                elif (load_value[k]['__class__'] == 'Review'):
                    FileStorage.__objects[k] = Review(**load_value[k])
                else:
                    print('class doesn\'t exist')
