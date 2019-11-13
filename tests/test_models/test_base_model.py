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
        ut = test_model.updated_at
        test_model.save()
        self.assertNotEqual(ut, test_model.updated_at)

    def test_str(self):
        """
        test str
        """

        test_model = BaseModel()
        id = test_model.id
        srt = test_model.__str__()
        self.assertEqual(srt, "[BaseModel] ({}) {}".
                         format(id, test_model.__dict__))

    def test_to_dict(self):
        """
        test to_dict
        """

        test_model = BaseModel()
        dit = test_model.to_dict()
        up = test_model.updated_at.isoformat()
        self.assertEqual(up, dit['updated_at'])

    def test_from_dict(self):
        """
        test constructor with dict
        """

        test_model = BaseModel()
        dit = test_model.to_dict()
        test_model2 = BaseModel(None, id=dit['id'])
        self.assertEqual(test_model.id, test_model2.id)

if __name__ == '__main__':
    unittest.main()
