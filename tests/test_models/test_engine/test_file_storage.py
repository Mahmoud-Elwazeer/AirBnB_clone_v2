#!/usr/bin/python3
"""Module for file_storage test Cases
"""
from models.engine import file_storage
import unittest
from models.all_models import our_models


class TestFileStorage(unittest.TestCase):
    """test cases for FileStorage class
    """

    def test_module_documetation(self):
        """test the documentation of a module
        """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class
        """
        self.assertTrue(len(file_storage.FileStorage.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class
        """
        for method in dir(file_storage):
            self.assertTrue(len(method.__doc__) > 0)

    def test_private_attrs_1(self):
        file_attr = file_storage.FileStorage.__file_path
        self.assertRaises(AttributeError, file_attr)

    def test_private_attrs(self):
        storage = file_storage.FileStorage()

        with self.assertRaises(AttributeError):
            _ = storage.__file_path

        with self.assertRaises(AttributeError):
            _ = storage.__objects

    def test_all_method(self):
        """test the return type of all method
        """
        f = file_storage.FileStorage()
        self.assertEqual(type(f.all()), dict)

    # def test_new(self):
    #     user = our_models["User"]()
    #     self.storage.new(user)
    #     self.assertIn(f'{user.__class__.__name__}.{user.id}',
    #                   self.storage.all())
