#!/usr/bin/python3
""" This module contains a class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances
"""
import json
import models
from os.path import exists


class FileStorage:
    """
    Class Storage
    """
    
    __objects = {}
    __file_path = "file.json"
    
    def all(self):
            """ returns the dictionary __objects """
            return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
            """ serializes __objects to the JSON file """
            empty_dict = {}
            for key, value in self.__objects.items():
                empty_dict[key] = value.to_dict()
            with open(self.__file_path, "w") as file:
                json.dump(empty_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        content = {}
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                content = json.load(file)
        for key, value in content.items():
            if value['__class__'] in models.classes:
                # ^ check if class exists within 'classes'
                cls = models.classes[value['__class__']]
                # ^ grabs correct class (ex. BaseModel, City...)
                myobj = cls(**value)
                # ^ instantiate object based on correct class...
                # ^ passing value dictionary in as kwargs
                self.__objects[key] = myobj
