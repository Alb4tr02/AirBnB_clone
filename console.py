#!/usr/bin/python3
""" This module create class HBNBCommand.
contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        elif argv[0] in self.class_list and len(argv) == 1:
            print("** instance id missing **")
        else:
            obj_attr = str(argv[0] + "." + argv[1])
            if obj_attr in storage.all():
                print(storage.all()[obj_attr])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        elif argv[0] in self.class_list and len(argv) == 1:
            print("** instance id missing **")
        else:
            obj_attr = str(argv[0] + "." + argv[1])
            if obj_attr in storage.all():
                del (storage.all()[obj_attr])
                storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    """
    Code not be executed when imported
    """
    HBNBCommand().cmdloop()
