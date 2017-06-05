#!/usr/bin/python3
""" File Storage to save an object to a file """
from datetime import datetime
import os
import json

class FileStorage():
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_json()
        for key in new_dict:
            for new_key in new_dict[key]:
                if type(new_dict[key][new_key]) is datetime:
                    new_dict[key][new_key] = str(new_dict[key].get(new_key))
        with open(self.__file_path, "w", encoding="UTF8") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                load_value = json.load(f)
            from models.base_model import BaseModel
            for k in load_value.keys():
                self.__objects[k] = BaseModel(**load_value[k])
