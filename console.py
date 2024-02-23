#!/usr/bin/python3
"""Create a class call HBNBCommmand"""


import cmd, json, shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (CRTL - d)"""
        print("Exiting the program")
        return True

    def cmdloop(self):
        try:
            super().cmdloop()
        except KeyboardInterrupt:
            return True

    def do_create(self, arg):
        """Create a new instance"""
        if not arg:
            print("** class name missing **")
        try:
            name = shlex.split(arg)[0]
            new_instance = eval(f"{name}()")
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Display the instance"""
        arg = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif not arg[1]:
            print("** instance id missing **")
        else:
            try:
                with open('file.json', 'r') as file:
                    dict_from_json = json.load(file)
                    name_id = arg[0] + "." + arg[1]
                    if name_id in dict_from_json:
                        obj_dict = dict_from_json[name_id]
                        obj = BaseModel(**obj_dict)
                        print("{}".format(obj))
                    else:
                        print("** no instance found **")
            except FileNotFoundError:
                pass

    def do_destroy(self, arg):
        """Delete the instance"""
        arg = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif not arg[1]:
            print("** instance id missing **")
        else:
            dict_from_storage = storage.all()
            name_id = arg[0] + "." + arg[1]
            if name_id in dict_from_storage:
                del dict_from_storage[name_id]
            else:
                print("** no instance found **")
            storage.save()

    def do_all(self, arg):
        if not arg:
            print("** class doesn't exist **")
        else:
            dict_from_storage = storage.all()
            for all_string in dict_from_storage:
                print(dict_from_storage[all_string])

    def do_update(self, arg):
        arg = shlex.split(arg)
        total_arguments = len(arg)
        arg_dict = {
            0: "** class name missing **",
            1: "** class doesn't exist **",
            2: "** instance id missing **",
            3: "** no instance found **"
        }
        if total_arguments in arg_dict :
            print(f"{arg_dict[total_arguments]}")
        else:
            try:
                dict_from_storage = storage.all()
                name_id = arg[0] + "." + arg[1]
            except:
                if name_id not in dict_from_storage:
                    print("** no instance found **")
            try:
                attribute = arg[2].append(name_id)
                value_att = arg[3].setattr(attribute)
            except:
                if not attribute:
                    print("** attribute name missing **")
                if not value_att:
                    print("** value missing **")

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()