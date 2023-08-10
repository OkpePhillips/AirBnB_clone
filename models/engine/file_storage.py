#!/usr/bin/env python3

"""
Module defines class 'FileStorage'
"""


import json
from models.base_model import BaseModel
from models.user import User


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

        """

        ####OLD
        self.__objects.update(
                {f"{type(obj).__name__}.{obj.id}": obj.to_dict()} 
                )   #TODO

        """
        self.__objects.update(
                {f"{type(obj).__name__}.{obj.id}": obj})   


    def save(self):
        """
        Serialize self.__objects to JSON put in path {self.__file_path}
        """

        
        converted_objects = {}

        #  print("SAVING-----")
        #print(self.__objects)
        for ID in self.__objects.keys():
            converted_objects.update(
                {f"{ID}": self.__objects[ID].to_dict()}
                )

        #  print("ENDSAVE\n")
            

        """
        ####OLD
        with open(self.__file_path, "w") as file:
            # Raises OSError on path absence.
            json.dump(self.__objects, file) #TODO

        """

        with open(self.__file_path, "w") as file:
            json.dump(converted_objects, file)
            

    def reload(self):
        """
        Deserialize JSON file to self.__objects.
        """

##TODO............
        try:
            with open(self.__file_path, "r") as file:

                JSON_recovered_dictionaries = json.load(file)

             #   print("Recovered Dictionaries--------")
             #  print(JSON_recovered_dictionaries,end="\n\n" )

            for ID in JSON_recovered_dictionaries.keys():
                obj_class = JSON_recovered_dictionaries[ID]["__class__"]
                self.new(
                        eval(obj_class)(**JSON_recovered_dictionaries[ID])
                        )

           #  print("Recovered and converted objects.--------------")
           #  print(self.__objects,end="\n\n")

        except OSError:
            pass

    def instance_edit(self, obj):
        """
        Edits instance dictionary representation in 
        __objects once model update method is called.
        """

        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj.to_dict()
