#!/usr/bin/python3
""" Unittesting for the <file_storage> class """

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ A class to unittest <file_storage> """

    def test_obj_dict(self):
        """ Tests if <objects> is dict """
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_file_path(self):
        """ Tests if <file_path> does or does not exist """
        my_file_path = FileStorage._FileStorage__file_path
        self.assertTrue(type(my_file_path) is str)
        if not os.path.exists(my_file_path):
            my_model = BaseModel()
        self.assertTrue(os.path.exists(my_file_path))
