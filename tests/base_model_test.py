#!/usr/bin/python3

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
