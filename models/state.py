#!/usr/bin/python3
"""
Defines class 'State'
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    Class definition for State
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method to inherit BaseModel initialisation.
        """
        super().__init__(**kwargs)
