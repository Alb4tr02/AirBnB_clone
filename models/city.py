#!/usr/bin/python3
""" This module create class City that inherits from BaseModel.
See:
    test_save_reload_user.py file
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    """
    state_id = ""
    name = ""
