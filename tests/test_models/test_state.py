#!/usr/bin/python3
"""
This Module tests the 'State' class.
"""

import unittest
from models.state import State
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """
    Class tests all 'state' features.
    """
    def test_id(self):
        """
        Method to test the id attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)

    def test_state(self):
        """
        Test name attribute
        """
        state = State()
        self.assertEqual(state.name, "")
