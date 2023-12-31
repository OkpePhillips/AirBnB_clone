#!/usr/bin/python3

"""
Defines classs 'BaseModel'.
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Definition of the BaseModel class Subclassed by most classes further along.
    """

    def __init__(self, *args, **kwargs):
        """"
        Method to initialise an instance of BaseModel, using either
        keyword arguments from dictionary representaion or creating the
        instance without any arguments
        """
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    formated_date = datetime.strptime(value,
                                                      "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, formated_date)
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """
        Method to modify the updated_at attribute of an instance of BaseModel.
        """
        self.updated_at = datetime.now()
        # storage.instance_edit(self)
        models.storage.save()

    def to_dict(self):
        """
        Method to create a dictionary representation of an instance of
        BaseModel.
        """

        """
        Note:
        created_at and updated_at must be converted to string object
        in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        you can use isoformat() of datetime object
        """
        dictionary = self.__dict__.copy()
        dictionary.update({"__class__": self.__class__.__name__})

        dictionary["created_at"] = str(dictionary["created_at"].isoformat())
        dictionary["updated_at"] = str(dictionary["updated_at"].isoformat())

        return dictionary

    def __str__(self):
        """
        Magic Method to create a string format of the object attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
