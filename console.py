#!/usr/bin/env python3

"""
Module: Defines entry point for Project console.
      : Defines 'class' HBNBCommand.
"""


import cmd
from models.base_model import BaseModel
import json
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }


class HBNBCommand(cmd.Cmd):
    """
    Subclass Cmd for project console functionality.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Define exit action on console quit inctruction.
        """

        raise SystemExit

    def do_EOF(self, line):
        """
        Define exit action on EOF.
        """

        # Add Line before quit?
        print()
        self.do_quit(line)

    def emptyline(self):
        """ Does nothing when empty line encountered."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves to Json file
        and prints the instance id.
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in class_dict:
            print("** class doesn't exist **")
        else:
            class_type = class_dict[args[0]]
            new_instance = class_type()
            new_instance.save()
            print("{}".format(new_instance.id))

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        storage.reload()
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) == 1:
            class_name = args[0]
            if class_name not in class_dict:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        else:
            class_name = args[0]
            obj_id = args[1]

            if class_name not in class_dict:
                print("** class doesn't exist **")
                return
            else:
                dict_key = f"{class_name}.{obj_id}"
                objects = storage.all()
                if dict_key in objects:
                    obj_instance = objects[dict_key]
                    print(obj_instance)
                else:
                    print("** no instance found **")
                    return

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        It also manages errors appropriately.
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) == 1:
            class_name = args[0]
            if class_name not in class_dict:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        else:
            class_name = args[0]
            obj_id = args[1]

            if class_name not in class_dict:
                print("** class doesn't exist **")
                return
            else:
                dict_key = f"{class_name}.{obj_id}"
                if dict_key in storage.all():
                    del storage.all()[dict_key]
                    storage.save()
                else:
                    print("** no instance found **")
                    return

    def do_all(self, line):
        """
        Prints the string representation of all instances
        based on the class name.
        """
        storage.reload()
        args = line.split()
        objects = storage.all()
        instance_list = []
        if len(args) < 1:
            for instance in objects.values():
                instance_list.append(instance.__str__())
            print(instance_list)
        else:
            class_name = args[0]
            if class_name in class_dict:
                for instance in objects.values():
                    if instance.__class__.__name__ == class_name:
                        instance_list.append(instance.__str__())
                print(instance_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        Method to update the attributes of an instance based on
        the class name and id, saves the changes to the json file
        and handles errors appropriately.
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        storage.reload()
        objects = storage.all()
        obj_key = f"{class_name}.{obj_id}"
        if obj_key not in objects:
            print("** instance not found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3].strip('"\'')
        attr_type = type(attribute_value).__name__
        instance = objects[obj_key]
        setattr(instance, attribute_name, eval(attr_type)(attribute_value))
        instance.save()

    def do_count(self, class_name):
        """
        Method to return the count of instances of a class.
        """
        storage.reload()
        objects = storage.all()
        instance_count = 0
        if class_name in class_dict:
            for instance in objects.values():
                if instance.__class__.__name__ == class_name:
                    instance_count += 1
            print(instance_count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """
        Method to handle commands prefixed by defined method names.
        """
        parts = line.split('.')
        if len(parts) == 2:
            class_name, method_name = parts
            method_name = method_name.strip("()")
            if class_name in class_dict:
                if hasattr(self, f'do_{method_name}'):
                    eval(f"self.do_{method_name}")(class_name)
                    return
            else:
                print("** class doesn't exist **")
        print("*** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
