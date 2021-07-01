#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime
import models
import json
format_iso = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """
    BaseModel class
    Defines all common attributes/methods for other classes:
    Instance attributes:
        Public:
            - id
            - created_at
            - updated_at
    Instance methods:
        Public:
            - save(self)
            - to_dict(self)
    Special method:
        - __init__(self)
        - __str__(self)
    """
    def __init__(self, *args, **kwargs):
        """
	Initializes an instance of BaseModel class
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format_iso)
                elif key is "__class__":
                    pass
                elif key is not "__class__":
                    self.__dict__[key] = value
    def __str__(self):
        """
	Returns a string representation of an instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
	Updates the public instance update_at with the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
	Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dic = dict(self.__dict__)
        # make variable my_dict
        my_dic["__class__"] = self.__class__.__name__
        # add class key with class name of the object
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        return (my_dic)
