#!/usr/bin/python3
""" """
from models.city import City
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
        self.name = 'City'
        self.value = City

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default_object(self):
        """ type of object"""
        obj = City()
        self.assertEqual(type(obj), 'City')

    def test_kwargs_normal(self):
        """ obj is not new"""
        obj = City()
        copy = obj.to_dict()
        new = City(**copy)
        self.assertFalse(new is obj)

    def test_kwargs_int_key(self):
        """ update with integer key"""
        obj = City()
        copy = obj.to_dict()
        copy.update({8: 9})
        with self.assertRaises(TypeError):
            new = City(**copy)

    def test_save_to_file(self):
        """ key in json file"""
        obj = City()
        obj.save()
        key = self.name + "." + obj.id
        with open('file.json', 'r') as f:
            string = json.load(f)
            self.assertEqual(string[key], obj.to_dict())

    def test_str_representation(self):
        """ """
        obj = City()
        self.assertEqual(str(obj), '[{}] ({}) <{}>'.format(self.name, obj.id,
                         obj.__dict__))
