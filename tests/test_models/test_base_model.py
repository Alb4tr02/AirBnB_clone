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

    def test_base_class(self):
        """
        tests intranet
        """

        test_model = BaseModel()
        test_model.name = "Holberton"
        test_model.my_number = 89
        self.assertIsInstance(test_model, BaseModel)
        self.assertEqual(test_model.name, "Holberton")
        self.assertEqual(test_model.my_number, 89)

    def test_save(self):
        """
        tests save
        """
        test_model = BaseModel()
        id = test_model.id
        ct = test_model.created_at
        ut = test_model.updated_at
    
