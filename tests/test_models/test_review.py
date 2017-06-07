#!/usr/bin/python3
""" Review Class Unittest """
import unittest
import models
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """ testing review class """

    def test_review_attr(self):
        """ review test """
        self.one = Review()
        self.assertTrue(hasattr(self.one, "place_id"))
        self.assertTrue(hasattr(self.one, "user_id"))
        self.assertTrue(hasattr(self.one, "text"))
        self.assertFalse(hasattr(self.one, "area"))

    def test_review_value(self):
        """ test review value """
        self.one = Review()
        self.assertEqual(self.one.place_id, "")
        self.assertEqual(self.one.user_id, "")
        self.assertEqual(self.one.text, "")
        self.assertFalse(self.one.text, "hole in the wall")

    def test_review_type(self):
        """ test review value type """
        self.one = Review()
        self.assertEqual(type(self.one.place_id), str)
        self.assertEqual(type(self.one.user_id), str)
        self.assertNotEqual(type(self.one.text), int)

if __name__ == '__main__':
    unittest.main()
