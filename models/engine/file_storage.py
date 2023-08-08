#!/usr/bin/env python3

"""
Module defines class 'FileStorage'
"""


import json


class FileStorage:
    """
    This class handles serialization and deserialization of instances
    to and from JSON formats.
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
        # Stores objects in format { <ClassName>.id: object }

    def all(self):
        """
        Return dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Set obj with key <obj class name>.id
        """
        self.__objects.update(
                {f"{type(obj).__name__}.{obj.id}": obj.to_dict()}
                )

    def save(self):
        """
        Serialize self.__objects to JSON put in path {self.__file_path}
        """

        with open(self.__file_path, "w") as file:
            # Raises OSError on path absence.
            json.dump(self.__objects, file)

    def reload(self):
        """
        Deserialize JSON file to self.__objects.
        """

        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)

        except OSError:
            pass

    def instance_edit(self, obj):
        """
        Edits instance dictionary representation in 
        __objects once model update method is called.
        """

        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj.to_dict()
