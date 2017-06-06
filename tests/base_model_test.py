#!/usr/bin/python3
""" unittest for basemode """

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "id2"))
        #self.hasattr(bm, "created_at")
        #self.hasattr(bm, "updated_at")
        #self.hasattr(bm, "name")
        #self.hasattr(bm, "__class__")

if __name__ == '__main__':
    unittest.main()

