#!/usr/bin/python3
"""Unittest module for the FileStorage class"""

import re
import json
import os
import unittest
from datetime import datetime
import sys
sys.path.append("..")
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """tests the file storage module"""

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_instance(self):
        """Tests object formation of the storage class"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_instance_without_args(self):
        """tests the instantiation without arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_instance_with_more_args(self):
        """Tests instantiation method with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(str(e.exception), msg)

    # def help_test_all(self, classname):
    #     """Helper tests all() method for classname."""
    #     self.resetStorage()
    #     self.assertEqual(storage.all(), {})

    #     o = storage.classes()[classname]()
    #     storage.new(o)
    #     key = "{}.{}".format(type(o).__name__, o.id)
    #     self.assertTrue(key in storage.all())
    #     self.assertEqual(storage.all()[key], o)

    # def test_all_base_model(self):
    #     """Tests all() method for BaseModel."""
    #     self.help_test_all("BaseModel")

    
