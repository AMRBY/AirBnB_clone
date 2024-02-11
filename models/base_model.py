#!/usr/bin/python3

import uuid
from datetime import datetime

"""
till we finish the class
"""


class BaseModel:

    """define the attributes and methods"""
    def __init__(self, *args, **kwargs):
        from models import storage
        """
        """
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        from models import storage
        """updates the public instance attribute,
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert the object to a dictionary representation.
        Returns:
            dict: A dictionary containing the object's attributes,
            class name, and ISO-formatted date strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict

    def __str__(self):
        """Custom string representation of the object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
