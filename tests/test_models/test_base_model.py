#!/usr/bin/python3
"""
test BaseModel class
"""
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel Class
    """

    def test_base_id(self):
        """
        basic tests id
        """

        test_model = BaseModel()
        self.assertIsNotNone(test_model.id)
        test_model.id = "1234"
        self.assertEqual("1234", test_model.id)

    def test_base_time(self):
        """
        basica tests time
        """

        test_model = BaseModel()
        self.assertIsNotNone(test_model.created_at)
        self.assertIsNotNone(test_model.updated_at)
        time = test_model.created_at
        test_model.created_at = datetime(1996, 7, 27)
        self.assertEqual(datetime(1996, 7, 27), test_model.created_at)
        #self.assertEqual(time, test_model.updated_at)
