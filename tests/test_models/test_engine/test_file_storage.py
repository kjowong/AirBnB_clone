#!/usr/bin/python3
""" unittest for BaseModel create from dictionary"""

import unittest
import models
import os
from models import storage
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
            except BaseException:
                pass

    def test_file_storage(self):
        """ test for filestorage """
        self.assertFalse(hasattr(self.ikea, "fake_id"))


if __name__ == '__main__':
    unittest.main()
