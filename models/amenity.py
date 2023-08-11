#!/usr/bin/env python3
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
        super().__init__(**kwargs)
