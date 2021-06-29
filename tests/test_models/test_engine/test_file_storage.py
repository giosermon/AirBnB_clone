#!/usr/bin/python3
"""
Unittest module for FileStorage
"""
import models
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os
import unittest


class Test_File_Storage(unittest.TestCase):
    """
	Unittesting class
    """
