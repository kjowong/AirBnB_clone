#!/usr/bin/python3
""" init py file """
from models.engine.file_storage import FileStorage
storage = FileStorage()
FileStorage.reload(storage)
