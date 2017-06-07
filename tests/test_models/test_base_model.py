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

    def test_doc_class(self):
        """ test class """
        expected = '"class BaseModel'
        actual = BaseModel.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """ test save """
        expet = ' updates public instance attribute with the current datetime '
        actual = BaseModel.save.__doc__
        self.assertEqual(expet, actual)

    def test_doc_to_json(self):
        """ test json """
        e = ' returns a dict containing all keys\x0balues of the __dict __ '
        actual = BaseModel.to_json.__doc__
        self.assertEqual(e, actual)

    def test_doc_str_(self):
        """ test __str__ """
        expected = ' printing string representation of BaseModel '
        actual = BaseModel.__str__.__doc__
        self.assertEqual(expected, actual)

    def test_doc_repr(self):
        """ test repr """
        expected = ' format __str__ '
        actual = BaseModel.__repr__.__doc__
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
