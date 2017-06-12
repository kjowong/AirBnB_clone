#!/usr/bin/python3
""" unittest for BaseModel create from dictionary"""

import unittest
import models
import os
from models.engine.file_storage import FileStorage

class TestBaseModelDictStorage(unittest.TestCase):
    """ class testing File Storage """

    def setUp(self):
        """ setup """
        self.ikea = FileStorage()

    def tearDown(self):
        """ tear down"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_file_storage(self):
        """ test for filestorage """
        self.assertTrue(hasattr(self.ikea, "__file_path"))
        self.assertFalse(hasattr(self.ikea, "fake_id"))

    def test_storage_func(self):
        """ test methods in storage """
        self.ikea.new()
        one = self.ikea.name
        two = self.ikea.key
        self.ikea.save()
        self.assertTrue(type(one) is str)
        self.assertFalse(type(two) is int)

if __name__ == '__main__':
    unittest.main()
