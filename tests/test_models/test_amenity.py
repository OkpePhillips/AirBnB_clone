#!/usr/bin/python3
"""
This Module tests the 'Amenity' class.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Class tests all 'Amenity' features.
    """
    def test_id(self):
        """
        Method to test the id attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)
