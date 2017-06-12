#!/usr/bin/python3
""" unittest for BaseModel create from dictionary"""

import unittest
import models
from models.engine.file_storage import FileStorage

class TestBaseModelDictStorage(unittest.TestCase):
    """ class testing File Storage """

    """
    def test_init(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "__class__"))
        self.assertTrue(hasattr(bm, "created_at"))
#        self.assertTrue(hasattr(bm, "updated_at"))
    """

    def test_file_storage(self):
        """ test for filestorage """
        self.storage = FileStorage()
        self.assertTrue(hasattr(self.storage, "__file_path"))
        self.assertFalse(hasattr(self.storage, "fake_id"))

    def test_storage_func(self):
        """ test methods in storage """
        self.storage = FileStorage()
        self.storage.new()
        one = self.storage.name
        two = self.storage.key
        self.storage.save()
        self.assertTrue(type(one) is str)
        self.assertFalse(type(two) is int)

if __name__ == '__main__':
    unittest.main()
