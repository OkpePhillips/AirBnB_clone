#!/usr/bin/python3

"""
Initialize package values.
Preps new storage class instance
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
