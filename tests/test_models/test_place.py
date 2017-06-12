#!/usr/bin/python3
""" City Class Unittest """
import unittest
import models
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """ testing place class """

    def test_place_attr(self):
        """ place test """
        self.one = Place()
        self.assertTrue(hasattr(self.one, "city_id"))
        self.assertTrue(hasattr(self.one, "user_id"))
        self.assertTrue(hasattr(self.one, "name"))
        self.assertTrue(hasattr(self.one, "description"))
        self.assertTrue(hasattr(self.one, "number_rooms"))
        self.assertTrue(hasattr(self.one, "number_bathrooms"))
        self.assertTrue(hasattr(self.one, "max_guest"))
        self.assertTrue(hasattr(self.one, "price_by_night"))
        self.assertTrue(hasattr(self.one, "latitude"))
        self.assertTrue(hasattr(self.one, "longitude"))
        self.assertTrue(hasattr(self.one, "amenity_ids"))
        self.assertFalse(hasattr(self.one, "area"))

    def test_place_value(self):
        """ place value test """
        self.one = Place()
        self.assertEqual(self.one.city_id, "")
        self.assertEqual(self.one.name, "")
        self.assertFalse(self.one.description, "CA.94500")
        self.assertEqual(self.one.number_rooms, 0)

    def test_place_type(self):
        """ place value type test """
        self.one = Place()
        self.assertEqual(type(self.one.user_id), str)
        self.assertEqual(type(self.one.number_rooms), int)
        self.assertEqual(type(self.one.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
