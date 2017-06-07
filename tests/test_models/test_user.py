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

    def test_user_value(self):
        """ test user value """
        self.one = User()
        self.assertEqual(self.one.first_name, "")
        self.assertNotEqual(self.one.email, "hbnb@holberton.com")
        self.assertEqual(self.one.password, "")
        self.assertEqual(self.one.last_name, "")

    def test_user_type(self):
        """ testing user type """
        self.one = User()
        self.assertEqual(type(self.one.email), str)
        self.assertEqual(type(self.one.password), str)
        self.assertNotEqual(type(self.one.first_name), int)
        self.assertNotEqual(type(self.one.last_name), list)

if __name__ == '__main__':
    unittest.main()
