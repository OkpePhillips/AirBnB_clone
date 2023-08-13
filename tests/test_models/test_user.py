#!/usr/bin/python3

"""
This module contains the test class for class 'User'.
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class defines the test cases for class 'User'
    Inherits unittest.Testcase.

    Since this class inherits BaseModel, tests will be more focused
    on functions drectly interacting with the information processing
    for the class.
    Core tests are done for the BaseModel class already.
    Shoutout Godwin!
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
        Instanciation uses the main_inst dictionary.
        """

        main_inst_dict = self.main_inst.to_dict()

        self.assertIn("email", main_inst_dict)
        self.assertIn("password", main_inst_dict)
        self.assertIn("first_name", main_inst_dict)
        self.assertIn("last_name", main_inst_dict)
