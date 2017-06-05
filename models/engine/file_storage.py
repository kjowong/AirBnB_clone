#!/usr/bin/python3
""" File Storage to save an object to a file """
import os
import json


class FileStorage:
    __file_path = "../../file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects = {obj.id: obj}

    def save(self):
        with open(r"FileStorage.__file_path", "w+", encoding="UTF8") as f:
            return json.dumps(f)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF8") as f:
                return json.load(f)
