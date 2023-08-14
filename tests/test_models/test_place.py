#!/usr/bin/python3
"""
This Module tests the 'Place' class.
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Class tests all 'Place' features.
    """
    def test_id(self):
        """
        Method to test the id attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)

    def test_city_id(self):
        """ test  city_id """
        self.place = Place()
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """ test user_id """
        self.place = Place()
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """ test name """
        self.place = Place()
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """ test description """
        self.place = Place()
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """ Test number_rooms"""
        self.place = Place()
        self.assertEqual(self.place.number_rooms, 0)

    def test_(self):
        """ Test number_bathrooms"""
        self.place = Place()
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """ Test max_guest"""
        self.place = Place()
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """ Test price_by_night"""
        self.place = Place()
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """ Test latitude"""
        self.place = Place()
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """ Test longitude"""
        self.place = Place()
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """ Test """
        self.place = Place()
        self.assertEqual(self.place.amenity_ids, [])
