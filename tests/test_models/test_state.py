#!/usr/bin/python3
""" State Class Unittest """
import unittest
import models
from models.state import State


class TestStateClass(unittest.TestCase):
    """ testing state class """

    def test_state_attr(self):
        """ state test """
        self.one = State()
        self.assertTrue(hasattr(self.one, "name"))
        self.assertFalse(hasattr(self.one, "area"))

    def test_state_value(self):
        """ test state value """
        self.one = State()
        self.assertEqual(self.one.name, "")
        self.assertFalse(self.one.name, "over the rainbow")

    def test_state_type(self):
        """ test state value type """
        self.one = State()
        self.assertEqual(type(self.one.name), str)
        self.assertNotEqual(type(self.one.name), int)

if __name__ == '__main__':
    unittest.main()
