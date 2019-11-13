#!/usr/bin/python3
""" This module create a unique FileStorage instance
See:
    test_save_reload_base_model.py file
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
