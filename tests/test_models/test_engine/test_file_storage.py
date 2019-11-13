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

    def test_class_dict(self):
        """
        Basica tests for FS Class
        """

        storage = FileStorage()
        dit = storage.class_dict
        self.assertIsInstance(dit, dict)

    def test_objects(self):
        """
        test private atribute
        """

        st = FileStorage()
        with self.assertRaises(AttributeError):
            st.__objects

    def test_file_path(self):
        """
        test private atribute
        """

        st = FileStorage()
        with self.assertRaises(AttributeError):
            st.__file_path

    def test_doc_FileStorage(self):
        """
        test doc for class
        """

        self.assertIsNotNone(FileStorage.__doc__)

    def test_doc_FileStorage_all(self):
        """
        test doc for all method
        """

        self.assertIsNotNone(FileStorage.all.__doc__)

    def test_doc_FileStorage_new(self):
        """
        test doc for new method
        """

        self.assertIsNotNone(FileStorage.new.__doc__)

    def test_doc_save(self):
        """
        test doc for save method
        """

        self.assertIsNotNone(FileStorage.save.__doc__)

    def test_doc_reload(self):
        """
        test doc for reload method
        """

        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_FileStorage_all(self):
        """
        test new method
        """

        st = FileStorage()
        with self.assertRaises(TypeError):
            st.all("lol")

    def test_FileStorage_new(self):
        """
        test new method
        """

        st = FileStorage()
        with self.assertRaises(TypeError):
            st.new()

    def test_FileStorage_save(self):
        """
        test save method
        """

        st = FileStorage()
        with self.assertRaises(TypeError):
            st.save("save")

    def test_FileStorage_new(self):
        """
        test reload method
        """

        st = FileStorage()
        with self.assertRaises(TypeError):
            st.reload("reload")
