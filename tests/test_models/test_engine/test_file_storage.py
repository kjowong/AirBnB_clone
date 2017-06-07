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

    def test_storage_all(self):
        """ test storage all """

    def test_storage_new(self):
        """ test methods in storage """

    def test_storage_save(self):
        """ test storage save """

    def test_storage_reload(self):
        """ test storage reload """


if __name__ == '__main__':
    unittest.main()
