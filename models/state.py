#!/usr/bin/python3
""" This module create class State that inherits from BaseModel.
See:
    test_save_reload_user.py file
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class
    """
    name = ""
