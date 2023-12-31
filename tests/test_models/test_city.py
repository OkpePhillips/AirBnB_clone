#!/usr/bin/python3
"""
This Module tests the 'City' class.
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Class tests all 'City' features.
    """
    def test_id(self):
        """
        Method to test the id attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)

    def test_state_id(self):
        """ Tests state_id. """
        self.city = City()
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        """Tests name attribute"""
        self.city = City()
        self.assertEqual(self.city.name, "")
