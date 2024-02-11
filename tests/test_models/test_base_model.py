#!/usr/bin/python3
""" """
from models.base_model import BaseModel
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
        self.name = 'BaseModel'
        self.value = BaseModel

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default_object(self):
        """ type of object"""
        obj = BaseModel()
        self.assertEqual(type(obj), 'BaseModel')

    def test_kwargs_normal(self):
        """ obj is not new"""
        obj = BaseModel()
        copy = obj.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is obj)

    def test_kwargs_int_key(self):
        """ update with integer key"""
        obj = BaseModel()
        copy = obj.to_dict()
        copy.update({8: 9})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save_to_file(self):
        """ key in json file"""
        obj = BaseModel()
        obj.save()
        key = self.name + "." + obj.id
        with open('file.json', 'r') as f:
            string = json.load(f)
            self.assertEqual(string[key], obj.to_dict())

    def test_str_representation(self):
        """ """
        obj = BaseModel()
        self.assertEqual(str(obj), '[{}] ({}) <{}>'.format(self.name, obj.id,
                         obj.__dict__))
