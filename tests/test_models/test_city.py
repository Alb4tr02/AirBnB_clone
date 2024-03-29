#!/usr/bin/python3
"""
test City class
"""
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
    TestCity Class
    """

    new_instance = City()

    def test_docs_city(self):
        """
        Test docs
        """

        self.assertIsNotNone(City.__doc__)

    def test_attributes_type(self):
        """
        Test attributes type
        """
        self.assertTrue(type(self.new_instance.state_id) is str)
        self.assertTrue(type(self.new_instance.name) is str)

    def test_attributes_city(self):
        """
        Test attributes of City class
        """

        self.assertTrue(hasattr(self.new_instance, "state_id"))
        self.assertTrue(hasattr(self.new_instance, "name"))

    def test_inheritance_BaseModel(self):
        """
        Test inheritance of city class
        """

        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(type(self.new_instance), BaseModel))

if __name__ == '__main__':
    unittest.main()
