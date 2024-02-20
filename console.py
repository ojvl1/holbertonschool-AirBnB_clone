#!/usr/bin/python3
"""Create a class call HBNBCommmand"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print("Exiting the program")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()