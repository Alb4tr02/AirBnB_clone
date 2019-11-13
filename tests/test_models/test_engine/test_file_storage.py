#!/usr/bin/python3
"""
Tests for FileStorage Class
"""

from datetime import datetime
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    test for FileStorage
    """

    def test_basic(self):
        """
        Basica tests for FS Class
        """

        storage = FileStorage()
        dit = storage.class_dict
        self.assertIsInstance(dit, dict)
