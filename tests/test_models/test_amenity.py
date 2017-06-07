#!/usr/bin/python3
""" Amenity Class Unittest """
import unittest
import models
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """ testing amenity class """

    def test_amenity_attr(self):
        """ amenity test """
        self.one = Amenity()
        self.assertTrue(hasattr(self.one, "name"))
        self.assertFalse(hasattr(self.one, "area"))

    def test_amenity_value(self):
<<<<<<< HEAD
        """ amenity value test """
=======
        """ test amenity value type """
>>>>>>> fabc72676c28bbb1a4c0d91b3741068d6b56aac4
        self.one = Amenity()
        self.assertEqual(self.one.name, "")
        self.assertFalse(self.one.name, "under the bridge")

    def test_amenity_type(self):
        """ amenity test type """
        self.one = Amenity()
        self.assertEqual(type(self.one.name), str)
        self.assertNotEqual(type(self.one.name), list)

if __name__ == '__main__':
    unittest.main()
