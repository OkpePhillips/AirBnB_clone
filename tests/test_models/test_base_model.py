#!/usr/bin/python3
"""
Module to test the BaseModel class and its features
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import models


class TestBaseModel(unittest.TestCase):
    """
    Class to test all BaseModel Features.
    """

    def setUp(self):
        """
        Method ran at the start of test.
        """
        pass

    def tearDown(self):
        """
        Method ran at the end of tests.
        """
        pass

    def test_id(self):
        """
        Method to test the id attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)

    def test_created_at(self):
        """
        Method to test the created_at attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at(self):
        """
        Method to test the update_at attribute.
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_created_updated_match(self):
        """
        Method to test that created_at matches updated_at initially.
        """
        base_model = BaseModel()
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_init_unique_id(self):
        """
        Method to test uniqueness of id attribute.
        """
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)
        self.assertIsInstance(base_model_1.id, str)

    def test_kwargs(self):
        """
        Method to test instantiation using kwargs from dictionary.
        """
        data = {
            '__class__': 'BaseModel',
            'id': 'test_id',
            'created_at': '2023-08-10T12:34:56.789012',
            'updated_at': '2023-08-11T01:23:45.678901'
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, 'test_id')
        self.assertEqual(str(base_model.created_at),
                         '2023-08-10 12:34:56.789012')
        self.assertEqual(str(base_model.updated_at),
                         '2023-08-11 01:23:45.678901')

    def test_save_updated_at_modify(self):
        """
        Method to test that save() modifies updated_at.
        """
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.name = 'Test Name'
        base_model.save()
        self.assertNotEqual(base_model.updated_at, initial_updated_at)
    
    def test_save(self):
        test_inst =  BaseModel()
        BaseModel.save(test_inst)

    def test_to_dict_attributes(self):
        """
        Method to test dictionary attributes.
        """
        base_model = BaseModel()
        base_model.name = 'Test Name'
        base_model.number = 123
        dictionary = base_model.to_dict()

        self.assertTrue(isinstance(dictionary, dict))
        self.assertIn('id', dictionary)
        self.assertIn('created_at', dictionary)
        self.assertIn('updated_at', dictionary)
        self.assertIn('name', dictionary)
        self.assertIn('number', dictionary)
        self.assertIn('__class__', dictionary)
        self.assertEqual(dictionary['__class__'], 'BaseModel')

    def test_to_dict_datetime_format(self):
        """
        Method to test date format in to_dict()
        """
        base_model = BaseModel()
        dictionary = base_model.to_dict()

        self.assertEqual(datetime.strptime(dictionary['created_at'],
                                           '%Y-%m-%dT%H:%M:%S.%f'),
                         base_model.created_at)
        self.assertEqual(datetime.strptime(dictionary['updated_at'],
                                           '%Y-%m-%dT%H:%M:%S.%f'),
                         base_model.updated_at)

    def test_str_format(self):
        """
        Method to test __str__ print format.
        """
        base_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(base_model.id,
                                                       base_model.__dict__)
        self.assertEqual(str(base_model), expected_output)
