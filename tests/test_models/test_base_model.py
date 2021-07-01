#!/usr/bin/python3
"""
Unittesting module for BaseModel class
"""
import models
from models.base_model import BaseModel
import os
import unittest
import datetime


class Test_Base_Model(unittest.TestCase):
    """
	Unittesting class
    """

    def test_datetime(self):
        """
        Checks for datetime attributes
        """
        #Test if two instnace has diferent datetime
        my_amenity = Amenity()
        my_amenity_2 = Amenity()
        self.assertNotEqual(my_amenity.created_at, my_amenity_2.created_at)
        self.assertNotEqual(my_amenity.updated_at, my_amenity_2.updated_at)
