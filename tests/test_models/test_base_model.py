#!/usr/bin/python3
""" unittest for basemode """

import unittest
import uuid
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ class TestBaseModel """

    def setUp(self):
        bm = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except BaseException:
                pass

    def test_init(self):
        #bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        #self.assertTrue(hasattr(bm, "created_at"))
        #self.assertTrue(hasattr(bm, "updated_at"))
        #self.assertTrue(hasattr(bm, "name"))
        #self.assertTrue(hasattr(bm, "__class__"))

    def test_with_args(self, *args, **kwargs):
        pass  # to be added

    def test_save_init(self):
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertIsNotNone(bm.__objects.get["updated_at"])

    def test_save_update(self):
        str_before = bm.__objects.get["updated_at"]
        bm.save()
        str_after = bm.__objects.get["updated_at"]
        self.assertNotEqual(str_before, str_after)

    def to_json():
        pass


if __name__ == '__main__':
    unittest.main()
