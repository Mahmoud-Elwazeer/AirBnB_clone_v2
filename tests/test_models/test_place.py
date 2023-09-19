#!/usr/bin/python3
"""module used for testing Place
"""
from models import place
from datetime import datetime
import unittest


class TestPlace(unittest.TestCase):
    """test cases for place class
    """

    def test_module_documetation(self):
        """test the documentation of a module
        """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class
        """
        self.assertTrue(len(place.BaseModel.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class
        """
        for method in dir(place.BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_is_init(self):
        """test if an object (instance) from Place type
        """
        u = place.Place()
        self.assertIsInstance(u, place.Place)

    def test_attr_formats(self):
        """test the format of class attributes in Uers class
        """
        u = place.Place()
        self.assertIsInstance(u.city_id, str)
        self.assertIsInstance(u.user_id, str)
        self.assertIsInstance(u.description, str)
        self.assertIsInstance(u.name, str)

    def test_attr_formats_2(self):
        """test the format of class attributes in Uers class
        """
        u = place.Place()
        self.assertIsInstance(u.number_rooms, int)
        self.assertIsInstance(u.number_bathrooms, int)
        self.assertIsInstance(u.max_guest, int)
        self.assertIsInstance(u.price_by_night, int)

    def test_attr_format_3(self):
        """test the format of class attributes in Uers class
        """
        u = place.Place()
        self.assertIsInstance(u.latitude, float)
        self.assertIsInstance(u.longitude, float)
        self.assertIsInstance(u.amenity_ids, list)

    def test_str_method(self):
        """testing __str__ representation
        """
        b = place.Place()
        expected_output = f"[Place] ({b.id}) {b.__dict__}"
        self.assertEqual(b.__str__(), expected_output)

    def test_unique_id(self):
        """test if the id is unique
        """
        u1 = place.Place()
        u2 = place.Place()
        self.assertNotEqual(u1.id, u2.id)

    def test_created_at(self):
        """test if the created_at attr changing
        """
        u = place.Place()
        self.assertTrue(u.created_at != datetime.now())

    def test_id_format(self):
        """test if the id format is string
        """
        u = place.Place()
        self.assertEqual(type(u.id), str)

    def test_to_dict(self):
        """test to_dict method
        """
        u = place.Place()
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
        my_model = place.Place(**kwargs)
        self.assertEqual(my_model.updated_at.year, 2023)

    def test_save_updatetime(self):
        """check save update time or not"""
        my_model = place.Place()
        old_date = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_date, my_model.updated_at)
