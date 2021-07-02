#!/usr/bin/python3
"""
Unittesting module for console
"""
import models
from models.base_model import BaseModel
import os
import unittest
import datetime


class Test_console(unittest.TestCase):
    """Test cases for the console.py file
    """
    clis = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
    storage = FileStorage()
