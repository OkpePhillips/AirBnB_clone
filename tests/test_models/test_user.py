#!/usr/bin/python3
"""
This module tests the User class.
"""


import unittest
from models.user import User
from models.base_model import BaseModel

class Test_User(unittest.TestCase):
    """
    This class defines the test cases for class 'User'
    Inherits unittest.TestCase.

    Since class 'User' inherits base class, tests will be
    more  focused on functions directly interacting with
    the class.
    CREATION INHERITANCE STORAGE RETRIEVAL
    """


# What would happen if an object's dictionary is used to create a new object?
#-> A keyword would be used to update the dictionary using __objects.update()
#   The resulting key <class_name.id> would collide with the instance 
#   already present and an overwrite would occur but with the same values.
#   Forming duplicates would be unlikely.

    def setUp(self):
        """
        Sets a general instance for succeeding testing puropseses.
        """
        
        self.main_inst = User()
        
        self.main_inst.email = "example@mailservice.com"
        self.main_inst.password = "Admin"
        self.main_inst.first_name = "David"
        self.main_inst.last_name = "Malan"

    def test_id(self):
        """
        Method to test the id attribute.
        """
        self.assertTrue(hasattr(self.main_inst, 'id'))
        self.assertIsInstance(self.main_inst.id, str)


    def test_isntance(self):
        """
        Verify if class inherits the BaseModel class.
        """

        self.assertIsInstance(self.main_inst, (BaseModel, User))

    def test_correct_store(self):
        """
        Tests the dictionary created before the storage operation.
        In summary, checks if class specific variables would 
        be written in the json file.
        """

        test_dict = self.main_inst.to_dict()

        self.assertIn("email", test_dict)
        self.assertIn("password", test_dict)
        self.assertIn("first_name", test_dict)
        self.assertIn("last_name", test_dict)


    def test_successful_reload(self):
        """
        Method tests for the successful reload of the main instance(main_ist)
        Instanciation will be done using the main_isnt dictionary.
        """
        
        main_inst_dict = self.main_inst.to_dict()
        reloaded_inst = User(**main_inst_dict)

        self.assertEqual(self.main_inst.id, reloaded_inst.id)

        test_dict = reloaded_inst.to_dict()
            
        self.assertIn("email", test_dict)
        self.assertIn("password", test_dict)
        self.assertIn("first_name", test_dict)
        self.assertIn("last_name", test_dict)

