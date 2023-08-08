#!/usr/bin/env python3

"""
Initialize package values.
Preps new storage class instance
"""


import models.engine.file_storage as file_storage

storage = file_storage.FileStorage()
storage.reload()
