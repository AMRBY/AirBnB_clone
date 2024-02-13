#!/usr/bin/python3
""" """
from models.user import User
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'User'
        self.value = User

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default_object(self):
        """ type of object"""
        obj = User()
        self.assertEqual(type(obj), 'User')

    def test_kwargs_normal(self):
        """ obj is not new"""
        obj = User()
        copy = obj.to_dict()
        new = User(**copy)
        self.assertFalse(new is obj)

    def test_kwargs_int_key(self):
        """ update with integer key"""
        obj = User()
        copy = obj.to_dict()
        copy.update({8: 9})
        with self.assertRaises(TypeError):
            new = User(**copy)

    def test_save_to_file(self):
        """ key in json file"""
        obj = User()
        obj.save()
        key = self.name + "." + obj.id
        with open('file.json', 'r') as f:
            string = json.load(f)
            self.assertEqual(string[key], obj.to_dict())

    def test_str_representation(self):
        """ """
        obj = User()
        self.assertEqual(str(obj), '[{}] ({}) <{}>'.format(self.name, obj.id,
                         obj.__dict__))
