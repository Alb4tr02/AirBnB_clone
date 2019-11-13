#!/usr/bin/python3
""" This module create class Review that inherits from BaseModel.
See:
    test_save_reload_user.py file
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    """
    place_id = ""
    user_id = ""
    text = ""
