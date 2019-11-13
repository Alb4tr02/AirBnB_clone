#!/usr/bin/python3
"""
test Place class
"""
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """
    TestPlace Class
    """

    new_instance = Place()

    def test_docs_place(self):
        """
        Test docs
        """

        self.assertIsNotNone(Place.__doc__)

    def test_attributes_type(self):
        """
        Test attributes type
        """
        self.assertTrue(type(self.new_instance.name) is str)
        self.assertTrue(type(self.new_instance.city_id) is str)
        self.assertTrue(type(self.new_instance.user_id) is str)
        self.assertTrue(type(self.new_instance.description) is str)
        self.assertTrue(type(self.new_instance.number_rooms) is int)
        self.assertTrue(type(self.new_instance.number_bathrooms) is int)
        self.assertTrue(type(self.new_instance.max_guest) is int)
        self.assertTrue(type(self.new_instance.price_by_night) is int)
        self.assertTrue(type(self.new_instance.latitude) is float)
        self.assertTrue(type(self.new_instance.longitude) is float)
        self.assertTrue(type(self.new_instance.amenity_ids) is list)
        for key in self.new_instance.amenity_ids:
            self.assertTrue(type(key) is str)

    def test_attributes_place(self):
        """
        Test attributes of place class
        """
        self.assertTrue(hasattr(self.new_instance, "city_id"))
        self.assertTrue(hasattr(self.new_instance, "user_id"))
        self.assertTrue(hasattr(self.new_instance, "name"))
        self.assertTrue(hasattr(self.new_instance, "description"))
        self.assertTrue(hasattr(self.new_instance, "number_rooms"))
        self.assertTrue(hasattr(self.new_instance, "number_bathrooms"))
        self.assertTrue(hasattr(self.new_instance, "max_guest"))
        self.assertTrue(hasattr(self.new_instance, "price_by_night"))
        self.assertTrue(hasattr(self.new_instance, "latitude"))
        self.assertTrue(hasattr(self.new_instance, "longitude"))
        self.assertTrue(hasattr(self.new_instance, "amenity_ids"))

    def test_inheritance_BaseModel(self):
        """
        Test inheritance of Place class
        """

        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(type(self.new_instance), BaseModel))


if __name__ == '__main__':
    unittest.main()
