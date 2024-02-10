#!/usr/bin/env python3
"""
BaseModel is a base class of the hbnb project
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes
        """
    def __init__(self, *args, **kwargs):
        """__init__ function to initiate attributes
        Attributes:
            id: UUID
            created_at: date and time of creation
            updated_at: date and time of updating
        """
        from models import storage
        if (kwargs == {}):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if (key == "created_at" or key == "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """ str return a string representation of an object"""
        return str("[{}] ({}) <{}>"
                   .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ save update the attribute <update_at>"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to_dict return a dictionnary"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)
        new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
