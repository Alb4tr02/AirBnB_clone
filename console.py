#!/usr/bin/python3
""" This module create class HBNBCommand.
contains the entry point of the command interpreter
"""


import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel",
                  "User",
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

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        argv = arg.split()
        if len(argv) == 0:
            obj_list = []
            for obj_attr in storage.all():
                key = storage.all()[obj_attr]
                obj_list.append(str(key))
            print(obj_list)
        else:
            obj_list = []
            for obj_attr in storage.all():
                key = storage.all()[obj_attr]
                arg_class = obj_attr.split(".")
                if arg_class[0] == argv[0]:
                    obj_list.append(str(key))
            if argv[0] in self.class_list:
                print(obj_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        argv = shlex.split(arg)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        elif argv[0] in self.class_list and len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) < 3:
            print("** attribute name missing **")
        elif len(argv) < 4:
            print("** value missing **")
        else:
            obj_attr = str(argv[0] + "." + argv[1])
            if obj_attr not in storage.all():
                print("** no instance found **")
            else:
                setattr(storage.all()[obj_attr], argv[2], argv[3])
                storage_update = storage.all()
                storage_update[obj_attr].save()

    def default(self, arg):
        """
        retrieve all instances of a class by using: <class name>.all()
        """
        argv = arg.split(".")
        argv_2 = argv[1].split('"')
        if argv[1] == "all()":
            self.do_all(argv[0])
        elif argv[1] == "count()":
            obj_attr = str(argv[0])
            count = 0
            for key, value in storage.all().items():
                if obj_attr in key:
                    count += 1
            print(count)
        elif argv_2[0] == "show(":
            self.do_show(argv[0] + " " + argv_2[1])
        elif argv_2[0] == "destroy(":
            self.do_destroy(argv[0] + " " + argv_2[1])
        elif argv_2[0] == "update(":
            self.do_update(argv[0] + " " + argv_2[1] + " " + argv_2[3] +
                           " " + argv_2[5])

if __name__ == '__main__':
    """
    Code not be executed when imported
    """
    HBNBCommand().cmdloop()
