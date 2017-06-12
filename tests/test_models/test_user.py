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
        self.assertTrue(hasattr(self.one, "email"))
        self.assertTrue(hasattr(self.one, "password"))
        self.assertEqual(self.one.first_name, "")
        self.assertFalse(self.one.email, "hbnb@holberton.com")

if __name__ == '__main__':
    unittest.main()
