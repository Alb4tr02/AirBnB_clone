#!/usr/bin/python3
""" This module create class User that inherits from BaseModel.
See:
    test_save_reload_user.py file
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = "" 
    first_name = ""
    last_name = ""
