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

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = str(datetime.now().isoformat())
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = str(datetime.now().isoformat())

    def to_dict(self):
        dictionary = self.__dict__
        dictionary.update({"__class__": self.__class__.__name__})
        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
