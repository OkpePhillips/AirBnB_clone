#!/usr/bin/python3
"""
Defines class 'User'
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Class definition for User class.
    Subclasses BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to inherit from BaseModel initialisation.
        """
        super().__init__(**kwargs)
