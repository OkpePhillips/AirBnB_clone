#!/usr/bin/env python3
"""
Defines class 'User'
"""


from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        pass
