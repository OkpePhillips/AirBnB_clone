#!/usr/bin/python3
"""
Module to test file storage.
"""
import unittest
from models import FileStorage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage as fs
from models.user import User
import os
import json
import models

class Test_File_Storage(unittest.TestCase):
    """
    This class defines the test cases for class 'FileStorage'.
    Inherits unittest.TestCase.
    """
    def setUp(self):
        """Method ran at start of test """
        self.storage = FileStorage()

    def tearDown(self):
        """ Method ran after test to free resources. """
        if self.storage is not None:
            try:
                os.remove(self.storage._FileStorage__file_path)
            except FileNotFoundError:
                pass

    def test_object_store(self):
        """
        Tests whether the FileStorage __objects variable:
        1. is a dictionary
        2. contains at least one object properly formatted created from
            the BaseModel object created by the test method.
        """

        test_inst = BaseModel()
        test_id =  f"BaseModel.{test_inst.id}"

        #self.assertTrue(type(fs.__objects) == dict)

        self.assertTrue(len(models.storage._FileStorage__objects) > 0)

        self.assertTrue(test_id in models.storage.all())

        self.assertIsNotNone(FileStorage.all)
        # Latest Change HERE


    def test_file_path(self):
        """ Method to check file_path attribute. """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_objects_initialized_empty_dictionary(self):
        """Method to check objects initialised empty dictionary."""
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertEqual(len(storage._FileStorage__objects), 0)

    def test_all_returns_correct_dictionary(self):
        """Method to check correct dictionary is returned. """
        base_model = BaseModel()
        user = User()
        self.storage.new(base_model)
        self.storage.new(user)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn(f"BaseModel.{base_model.id}", all_objects)
        self.assertIn(f"User.{user.id}", all_objects)

    def test_new_method(self):
        """ Method to check new() saves all objects. """
        base_model = BaseModel()
        user = User()
        self.storage.new(base_model)
        self.storage.new(user)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn(f"BaseModel.{base_model.id}", all_objects)
        self.assertIn(f"User.{user.id}", all_objects)

    def test_save_method(self):
        """ Method to check save creates a json file. """
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as file:
            file_content = file.read()
            self.assertIn(f"BaseModel.{base_model.id}", file_content)
            self.assertIn("created_at", file_content)
            self.assertIn("updated_at", file_content)

    def test_reload_method(self):
        """ Method to check that all objects are reloaded. """
        test_data = {
            "BaseModel.1": {
                "__class__": "BaseModel",
                "id": "1",
                "created_at": "2023-08-10T12:34:56.789",
                "updated_at": "2023-08-10T12:34:56.789"
            },
        }
        with open(self.storage._FileStorage__file_path, "w") as file:
            json.dump(test_data, file)
        self.storage.reload()
        loaded_objects = self.storage.all()
        self.assertEqual(len(loaded_objects), len(test_data))
        for obj_id, obj_data in test_data.items():
            self.assertTrue(obj_id in loaded_objects)
            self.assertEqual(loaded_objects[obj_id].__class__.__name__,
                             obj_data["__class__"])
