#!/usr/bin/python3
"""
test State class
"""
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """
    TestState Class
    """

    new_instance = State()

    def test_docs_state(self):
        """
        Test docs
        """

        self.assertIsNotNone(State.__doc__)

    def test_attributes_type(self):
        """
        Test attributes type
        """
        self.assertTrue(type(self.new_instance.name) is str)

    def test_attributes_state(self):
        """
        Test attributes of state class
        """
        self.assertTrue(hasattr(self.new_instance, "name"))

    def test_inheritance_BaseModel(self):
        """
        Test attributes of state class
        """

        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(type(self.new_instance), BaseModel))


if __name__ == '__main__':
    unittest.main()
