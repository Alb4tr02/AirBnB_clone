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


if __name__ == '__main__':
    unittest.main()
