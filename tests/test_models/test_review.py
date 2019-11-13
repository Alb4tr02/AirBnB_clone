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

    def test_attributes_review(self):
        """
        Test attributes of state class
        """

        self.assertTrue(hasattr(self.new_instance, "place_id"))
        self.assertTrue(hasattr(self.new_instance, "user_id"))
        self.assertTrue(hasattr(self.new_instance, "text"))

if __name__ == '__main__':
    unittest.main()
