#!/usr/bin/python3
""" Base Model file """


import uuid
from datetime import datetime
import models 
import json
format_iso = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        '''Class constructor'''
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
                    datatimee = datetime.strptime(value, format_iso)
                    setattr(self, key, datatimee)
                elif key != "__class__":  # class should not be added as attr
                    setattr(self, key, value)  # setting attr for other keys

    def __str__(self):
        """ Method that override the str method and returns a specific string 
            Args: self
            Return: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values
            of __dict__ of the instance '''
        my_dic = dict(self.__dict__) # make variable my_dict
        my_dic["__class__"] = self.__class__.__name__ # add class key with class name of the object
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        return (my_dic)
