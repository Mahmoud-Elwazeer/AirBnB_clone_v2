#!/usr/bin/python3
"""module used for testing basemodel
"""
from models import base_model
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test cases for basemodel class
    """

    def test_module_documetation(self):
        """test the documentation of a module"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class"""
        self.assertTrue(len(base_model.BaseModel.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class"""
        for method in dir(base_model.BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_init(self):
        """test create object from BaseModel"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model, base_model.BaseModel)

    def test_str_id(self):
        """test id -> str"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_unique_id(self):
        """test if the id is unique"""
        b1 = base_model.BaseModel()
        b2 = base_model.BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_kwargs_id(self):
        """check value of id in kwargs"""
        kwargs = {
            'id': '123'
        }
        my_model = base_model.BaseModel(**kwargs)
        self.assertEqual(my_model.id, '123')

    def test_datatime_created_at(self):
        """test created_at -> datetime"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_kwargs_created_at(self):
        """check created_at convert from string to datetime"""
        kwargs = {
            'created_at': '2023-08-11T18:28:19.430925'
        }
        my_model = base_model.BaseModel(**kwargs)
        self.assertEqual(my_model.created_at.year, 2023)

    def test_datatime_updated_at(self):
        """test updated_at -> datetime"""
        my_model = base_model.BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_kwargs_updated_at(self):
        """check updated_at convert from string to datetime"""
        kwargs = {
            'updated_at': '2023-08-11T18:28:19.430963'
        }
        my_model = base_model.BaseModel(**kwargs)
        self.assertEqual(my_model.updated_at.year, 2023)

    def test_str_method(self):
        """testing __str__ representation"""
        my_model = base_model.BaseModel()
        utput = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(my_model.__str__(), utput)

    def test_save_updatetime(self):
        """check save update time or not"""
        my_model = base_model.BaseModel()
        old_date = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_date, my_model.updated_at)
