#!/usr/bin/python3

import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    setUp method is a special method in unittest.TestCase that is called before each test method is executed
    """
    def setUp(self):
        self.base_model = BaseModel()
        """
        creating an instance of BaseModel:
        """
        """
        test checks if the id attribute of BaseModel is not None and is an instance of str
        """
    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)
        
        """
        test checks if the created_at attribute of Basemodel is an instance of dttime
        """

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        
        """
        test checks if the updated_at attrbute of Basemodel is an instance of datetime
        """

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)
        
    """
    test checks if the save method of BaseModel updates the updated_at attribute and calls the save method of models.storage
    """        
    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        with patch('models.storage.save') as mock_save:
            self.base_model.save()
            self.assertNotEqual(self.base_model.updated_at, initial_updated_at)
            """
            check if functio mock was called only once
            """
            mock_save.assert_called_once()

    """ 
    returns a dictionary with the key
    """

    def test_to_dict_method(self):
        given_keys = ['id', 'created_at', 'updated_at', '__class__']
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertCountEqual(model_dict.keys(), given_keys)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        
    def test_str_method(self):
        """
        Test the __str__() method
        """
        str_rep = str(self.a.to_dict())
        self.assertIn(self.a.id, str_rep)
        self.assertIn(self.a.__class__.__name__, str_rep)
        self.assertIn(self.a.created_at.isoformat(), str_rep)
        self.assertIn(self.a.updated_at.isoformat(), str_rep)
        
if __name__ == '__main__':
    unittest.main()
    
    
