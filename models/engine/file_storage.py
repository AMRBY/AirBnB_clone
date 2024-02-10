#!/usr/bin/env python3
"""
FileStorage is a class for objects storage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage serializes instances to a JSON file and deserializes JSON file to instances
    attributes:
        __file_path is JSON file name
        __objects is a dictionnary to store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__ + "." + obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dict_to_file = {}
        for k, v in self.__objects.items():
            dict_to_file[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dict_to_file, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if (self.__file_path != ""):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    obj_file = json.load(f)
                    for k, v in obj_file.items():
                        self.__objects[k] = BaseModel(**v)

            except Exception:
                pass
