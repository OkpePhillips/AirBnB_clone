#!/usr/bin/python3
"""
This Module tests the '' class.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
from models.amenity import Amenity

class TestReview(unittest.TestCase):
    """
    Class tests all 'Review' features.
    """
    def test_id(self):
        """
        Method to test the id attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)


    def test_place_id(self):
        """ Test place_id attribute. """
        self.review = Review()
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """ Test user_id. """
        self.review = Review()
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """ Test text attribute. """
        self.review = Review()
        self.assertEqual(self.review.text, "")
