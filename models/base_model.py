#!/usr/bin/python3

"""
Defines classs 'BaseModel'.
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Definition of the BaseModel class Subclassed by most classes further along.
    """

    def __init__(self, *args, **kwargs = None):

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__
        dictionary.update({"__class__": self.__class__.__name__})

        dictionary["created_at"] = str(dictionary["created_at"].isoformat())
        dictionary["updated_at"] = str(dictionary["updated_at"].isoformat())

        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
