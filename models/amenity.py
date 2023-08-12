#!/usr/bin/python3
"""
Defines class 'Amenity'
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Definition of the Amenity class.
    Subclasses BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to inherit BaseModel initialisation.
        """
        super().__init__(**kwargs)
