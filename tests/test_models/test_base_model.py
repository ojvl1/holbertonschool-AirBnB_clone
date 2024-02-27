#!/usr/bin/python3
""" Unit test module for BaseModel class """

import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


my_model = BaseModel()


class TestBase(unittest.TestCase):
    """ Class for BaseModel tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(type(my_model.id) is str)

    def test_created_at(self):
        """ Unittesting created_at instance """
        self.assertTrue(type(my_model.created_at) is datetime)

    def test_str(self):
        """ Unittesting str method """
        expected_str = "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.to_dict())
        actual_str = str(my_model)

        # Convert datetime objects to ISO format for comparison
        expected_str = expected_str.replace(
            my_model.created_at.isoformat(), str(my_model.created_at))
        expected_str = expected_str.replace(
            my_model.updated_at.isoformat(), str(my_model.updated_at))

        self.assertEqual(actual_str, expected_str)

    def test_to_dict(self):
        """ Unittesting to_dict method """
        my_dict = my_model.to_dict()
        self.assertTrue(type(my_dict["created_at"]) is str)
        self.assertTrue(type(my_dict) is dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertIn("__class__", my_dict.keys())

    def test_save(self):
        """ Unittesting save method """
        my_save = my_model.updated_at
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))
        my_save2 = my_model.updated_at
        self.assertNotEqual(my_save, my_save2)


if __name__ == '__main__':
    unittest.main()
