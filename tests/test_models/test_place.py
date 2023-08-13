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
        self.assertIsInstance(base_model.id, str)s
