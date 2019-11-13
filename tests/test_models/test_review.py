#!/usr/bin/python3
"""
test Review class
"""
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """
    TestReview Class
    """

    new_instance = Review()

    def test_docs_review(self):
        """
        Test docs
        """

        self.assertIsNotNone(Review.__doc__)

    def test_attributes_type(self):
        """
        Test attributes type
        """
        self.assertTrue(type(self.new_instance.place_id) is str)
        self.assertTrue(type(self.new_instance.user_id) is str)
        self.assertTrue(type(self.new_instance.text) is str)

    def test_attributes_review(self):
        """
        Test attributes of state class
        """

        self.assertTrue(hasattr(self.new_instance, "place_id"))
        self.assertTrue(hasattr(self.new_instance, "user_id"))
        self.assertTrue(hasattr(self.new_instance, "text"))

    def test_inheritance_BaseModel(self):
        """
        Test inheritance of Review class
        """

        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(type(self.new_instance), BaseModel))

if __name__ == '__main__':
    unittest.main()
