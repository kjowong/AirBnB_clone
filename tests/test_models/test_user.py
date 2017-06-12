#!/usr/bin/python3
""" User Class Unittest """
import unittest
import models
from models.user import User


class TestUserClass(unittest.TestCase):
    """ testing user class """

    def test_user(self):
        """ user test """
        self.one = User()
        self.assertTrue(hasattr(self.one, "first_name"))
        self.assertTrue(hasattr(self.one, "last_name"))
        self.assertFalse(hasattr(self.one, "middle_name"))

if __name__ == '__main__':
    unittest.main()
