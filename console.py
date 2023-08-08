#!/usr/bin/env python3

"""
Module: Defines entry point for Project console.
      : Defines 'class' HBNBCommand.
"""


import cmd


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
        self.do_quit(line)

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
