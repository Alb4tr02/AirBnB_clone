#!/usr/bin/python3
""" This module create class Amenity that inherits from BaseModel.
See:
    test_save_reload_user.py file
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class
    """
    name = ""
