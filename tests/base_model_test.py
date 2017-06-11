#!/usr/bin/python3
<<<<<<< HEAD
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

=======

import unittest
import models
from models import base_model
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
>>>>>>> master
