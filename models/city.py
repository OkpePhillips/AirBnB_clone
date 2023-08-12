#!/usr/bin/python3
"""
Defines class 'City'
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Definition for the City class.
    """

    state_id = ""  # will be the State.id
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to inherit BaseModel initialisation.
        """
        super().__init__(**kwargs)
