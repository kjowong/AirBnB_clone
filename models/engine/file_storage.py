#!/usr/bin/python3
""" File Storage to save an object to a file """
import datetime
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
        self.__objects[obj.id] = obj

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
                    load_value[k]['updated_at'] = datetime.strptime(load_value[k]['updated_at'], format)
                    load_value[k]['created_at'] = datetime.strptime(load_value[k]['created_at'], format)
                except:
                    pass
                self.__objects[k] = BaseModel(**load_value[k])
