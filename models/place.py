#!/usr/bin/python3
"""
Defines class 'Place'
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Definition of the Place class.
    Subclasses BaseModel.
    """

    city_id = ""  # Takes City.id
    user_id = ""  # User.id
    amenity_ids = []

    name = ""

    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0

    def __init__(self, *args, **kwargs):
        """
        Method to inherit BaseModel initialisation.
        """
        super().__init__(**kwargs)
