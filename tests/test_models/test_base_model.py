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
        """ setup instance of basemodel """
        self.bm = BaseModel()

    def tearDown(self):
        """ tear down of basemodel """
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except BaseException:
                pass

    def test_init(self):
        """ testing initialization """
        self.assertTrue(hasattr(self.bm, "id"))
        self.assertTrue(hasattr(self.bm, "created_at"))

    def test_save(self):
        """ test with save """
        self.assertFalse(hasattr(self.bm, "updated_at"))
        self.bm.save()
        self.assertTrue(hasattr(self.bm, "created_at"))

    def test_to_json(self):
        """ test json """
        to_json_bm = self.bm.to_json()
        self.assertTrue(isinstance(to_json_bm, dict))

    def test_with_args(self, *args, **kwargs):
        """ test with args """
        pass

    def test_save_update(self):
        """ test save update """
        pass




if __name__ == '__main__':
    unittest.main()
