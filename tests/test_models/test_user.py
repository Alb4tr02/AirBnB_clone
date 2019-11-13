#!/usr/bin/python3
"""
test User class
"""
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    TestUser Class
    """

    new_instance = User()
    new_instance.name = "Holberton"

    def test_docs_user(self):
        """
        Test docs
        """

        self.assertIsNotNone(User.__doc__)

    def test_attributes_user_types(self):
        """
        Tests attributes types
        """

        self.assertEqual(type(self.new_instance.email), str)
        self.assertEqual(type(self.new_instance.last_name), str)
        self.assertEqual(type(self.new_instance.first_name), str)
        self.assertEqual(type(self.new_instance.password), str)

    def test_attributes_user(self):
        """
        Test attributes of User class
        """

        self.assertTrue(hasattr(self.new_instance, 'email'))
        self.assertTrue(hasattr(self.new_instance, 'password'))
        self.assertTrue(hasattr(self.new_instance, 'first_name'))
        self.assertTrue(hasattr(self.new_instance, 'last_name'))

if __name__ == '__main__':
    unittest.main()
