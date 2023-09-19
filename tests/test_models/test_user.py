#!/usr/bin/python3
"""module used for testing User
"""
from models import user
from datetime import datetime
import unittest


class TestUser(unittest.TestCase):
    """test cases for user class
    """

    def test_module_documetation(self):
        """test the documentation of a module
        """
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class
        """
        self.assertTrue(len(user.BaseModel.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class
        """
        for method in dir(user.BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_is_init(self):
        """test if an object (instance) from User type
        """
        u = user.User()
        self.assertIsInstance(u, user.User)

    def test_attr_formats(self):
        """test the format of class attributes in Uers class
        """
        u = user.User()
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)

    def test_str_method(self):
        """testing __str__ representation
        """
        b = user.User()
        expected_output = f"[User] ({b.id}) {b.__dict__}"
        self.assertEqual(b.__str__(), expected_output)

    def test_unique_id(self):
        """test if the id is unique
        """
        u1 = user.User()
        u2 = user.User()
        self.assertNotEqual(u1.id, u2.id)

    def test_created_at(self):
        """test if the created_at attr changing
        """
        u = user.User()
        self.assertTrue(u.created_at != datetime.now())

    def test_id_format(self):
        """test if the id format is string
        """
        u = user.User()
        self.assertEqual(type(u.id), str)

    def test_to_dict(self):
        """test to_dict method
        """
        u = user.User()
        my_dict = u.to_dict()
        self.assertEqual(type(my_dict["created_at"]), str)
        self.assertEqual(type(my_dict["updated_at"]), str)
        self.assertEqual(my_dict["__class__"], u.__class__.__name__)
        self.assertEqual(my_dict["id"], u.id)

    def test_kwargs_updated_at(self):
        """check updated_at convert from string to datetime"""
        kwargs = {
            'updated_at': '2023-08-11T18:28:19.430963'
        }
        my_model = user.User(**kwargs)
        self.assertEqual(my_model.updated_at.year, 2023)

    def test_save_updatetime(self):
        """check save update time or not"""
        my_model = user.User()
        old_date = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_date, my_model.updated_at)
