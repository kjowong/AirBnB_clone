#!/usr/bin/python3
""" File Storage to save an object to a file """
from datetime import datetime
import os
import json


class FileStorage:
    def __init__(self):
        self.__file_path = "./file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = {obj.id: obj}

    def save(self):
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_json
            print("------")
            print(new_dict.get(key))
            print("------")

        for key in new_dict:
            if type(key) is datetime:
                new_dict[key] = str(new_dict.get(key))
        print(new_dict)
        #with open(self.__file_path, "w+", encoding="UTF8"):
         #   return json.dumps(new_dict)

    def reload(self):
        pass
        #if os.path.isfile(self.__file_path):
         #   with open(self.__file_path, "r", encoding="UTF8") as f:
          #      return json.loads(f)
