#!/usr/bin/python3
""" """
from models.state import State
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
        self.name = 'State'
        self.value = State

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default_object(self):
        """ type of object"""
        obj = State()
        self.assertEqual(type(obj), 'State')

    def test_kwargs_normal(self):
        """ obj is not new"""
        obj = State()
        copy = obj.to_dict()
        new = State(**copy)
        self.assertFalse(new is obj)

    def test_kwargs_int_key(self):
        """ update with integer key"""
        obj = State()
        copy = obj.to_dict()
        copy.update({8: 9})
        with self.assertRaises(TypeError):
            new = State(**copy)

    def test_save_to_file(self):
        """ key in json file"""
        obj = State()
        obj.save()
        key = self.name + "." + obj.id
        with open('file.json', 'r') as f:
            string = json.load(f)
            self.assertEqual(string[key], obj.to_dict())

    def test_str_representation(self):
        """ """
        obj = State()
        self.assertEqual(str(obj), '[{}] ({}) <{}>'.format(self.name, obj.id,
                         obj.__dict__))
