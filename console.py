#!/usr/bin/python3
""" This module create class HBNBCommand.
contains the entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "

    def do_quit(self, argument):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, argument):
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

if __name__ == '__main__':
    """
    Code not be executed when imported
    """
    HBNBCommand().cmdloop()
