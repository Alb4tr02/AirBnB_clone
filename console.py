#!/usr/bin/python3
""" This module create class HBNBCommand.
contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel",
                  "State",
                  "City",
                  "Amenity",
                  "Place",
                  "Review"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF (Ctr^D) to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        An empty line that execute anything
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argv[0] + "()")
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
    """
    Code not be executed when imported
    """
    HBNBCommand().cmdloop()
