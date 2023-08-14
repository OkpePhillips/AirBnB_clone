#!/usr/bin/python3
"""
Test for the Attributes of the class 'User'
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test class for the user attributes.
    """
    def test_user_email(self):
        """
        Checks that email attribute is properly set.
        """
        self.user = User()
        self.assertEqual(self.user.email, "")

    def test_user_password(self):
        """
        Checks that password attribute is properly set.
        """
        self.user = User()
        self.assertEqual(self.user.password, "")

    def test_user_first_name(self):
        """
        Checks that first_name attribute is properly set.
        """
        self.user = User()
        self.assertEqual(self.user.first_name, "")

    def test_user_last_name(self):
        """
        Checks that last_name attribute is properly set.
        """
        self.user = User()
        self.assertEqual(self.user.last_name, "")
