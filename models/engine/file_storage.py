#!/usr/bin/python3
""" File Storage to save an object to a file """

from datetime import datetime
import os
import json

format = '%Y-%m-%dT%H:%M:%S.%f'

class FileStorage():
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        name = str(obj.__class__.__name__)
        key = str(obj.id)
        new_obj = name + '.' + key
        self.__objects[new_obj] = obj

    def save(self):
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_json()
        with open(self.__file_path, "w", encoding="UTF8") as f:
            (json.dump(new_dict, f))

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                load_value = json.load(f)
            from models.base_model import BaseModel
            for k in load_value.keys():
                try:
                    load_value[k]['updated_at'] = datetime.datetime.strptime(load_value[k]['updated_at'], format)
                    load_value[k]['created_at'] = datetime.datetime.strptime(load_value[k]['created_at'], format)
                except:
                    pass
                if (loaded_value[k]["__class__"] == "BaseModel"):
                    self.__objects[k] = BaseModel(**load_value[k])
                elif (loaded_value[k]["__class__"] == "User"):
                    self.__objects[k] = User(**load_value[k])
                elif (loaded_value[k]["__class__"] == "State"):
                    self.__objects[k] = State(**loaded_value[k])
                elif (loaded_value[k]["__class__"] == "Amenity"):
                    self.__objects[k] = Amenity(**loaded_value[k])
                elif (loaded_value[k]["__class__"] == "Place"):
                    self.__objects[k] = Place(**loaded_value[k])
                elif (loaded_value[k]["__class__"] == "Review"):
                    self.__objects[k] = Review(**loaded_value[k])
                else:
                    print("class doesn't exist")
