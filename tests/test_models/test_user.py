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
    def setUp(self):
        """
        Sets a general instance for succeeding testing purposes.
        """

        self.main_inst = User()

        self.main_inst.email = "example@mailservice.com"
        self.main_inst.password = "Admin"
        self.main_inst.first_name = "David"
        self.main_inst.last_name = "Malan"

    def test_correct_store(self):
        """
        Tests the dictionary created before the JSON dump is made.
        Checks if class specific variables are stored.
        """

        test_dict = self.main_inst.to_dict()

        self.assertIn("email", test_dict)
        self.assertIn("password", test_dict)
        self.assertIn("first_name", test_dict)
        self.assertIn("last_name", test_dict)

    def test_successful_reload(self):
        """
        Tests for the successful reload of class specific variables
        effectively restoring an object by cloning its data.
        Instantiation uses the main_inst dictionary.
        """

        main_inst_dict = self.main_inst.to_dict()

        self.assertIn("email", main_inst_dict)
        self.assertIn("password", main_inst_dict)
        self.assertIn("first_name", main_inst_dict)
        self.assertIn("last_name", main_inst_dict)

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
