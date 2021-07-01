#!/usr/bin/python3
"""
Unittest module for FileStorage
"""
import models
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os
import unittest
import datetime


class Test_File_Storage(unittest.TestCase):
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
