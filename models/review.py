#!/usr/bin/python3
"""
Defines class 'Review'
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Definition of the Review class.
    Subclasses BaseModel.
    """

    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Method to inherit BaseModel initialisation.
        """
        super().__init__(**kwargs)
