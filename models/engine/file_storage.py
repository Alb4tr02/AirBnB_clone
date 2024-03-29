#!/usr/bin/python3
""" This module create class FileStorage.
Serializes instances to a JSON file and deserializes JSON file to instances
See:
    test_save_reload_base_model.py file
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    File storage class
    Args:
        file_path: string - path to the JSON file
        objects: dictionary - will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel,
                  "User": User,
                  "Place": Place,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Review": Review}

    def all(self):
        """
        Returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in "__objects" the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__,
                                      obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        my_dict = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            f.write(json.dumps(my_dict))

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_file = json.loads(f.read())
                for key in json_file:
                    a = '__class__'
                    b = json_file[key]
                    c = key
                    self.__objects[c] = self.class_dict[json_file[c][a]](**(b))
