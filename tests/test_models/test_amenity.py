#!/usr/bin/python3
"""
test Amenity class
"""
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
    TestAmenity Class
    """

    new_instance = Amenity()

    def test_docs_amenity(self):
        """
        Test docs
        """

        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_type(self):
        """
        Test attributes type
        """
        self.assertTrue(type(self.new_instance.name) is str)


    def test_attributes_amenity(self):
        """
        Test attributes of amenity class
        """
        self.assertTrue(hasattr(self.new_instance, "name"))

    def test_inheritance_BaseModel(self):
        """
        Test inheritance of amenity class
        """

        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(type(self.new_instance), BaseModel))

if __name__ == '__main__':
    unittest.main()
