#!/usr/bin/python3
""" This module create Class Base.
The “base” of all other classes in this project
See:
    test_base_model.py file
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiation
        Args:
            id: string - assign with an uuid
            created_at: datetime - assign with the current datetime
            updated_at: datetime - assign with the current datetime
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns class name, id and dict
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a new dictionary containing all keys/values of __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
