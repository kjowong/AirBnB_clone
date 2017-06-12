#!/usr/bin/python3
""" City Class Unittest """
import unittest
import models
from models.city import City


class TestCityClass(unittest.TestCase):
    """ testing city class """

    def test_city_attr(self):
        """ city test """
        self.one = City()
        self.assertTrue(hasattr(self.one, "state_id"))
        self.assertTrue(hasattr(self.one, "name"))
        self.assertFalse(hasattr(self.one, "area"))

    def test_city_value(self):
        """ test city value type """
        self.one = City()
        self.assertEqual(self.one.state_id, "")
        self.assertEqual(self.one.name, "")
        self.assertFalse(self.one.state_id, "CA.94500")

if __name__ == '__main__':
    unittest.main()
