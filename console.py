#!/usr/bin/python3
from models.base_model import BaseModel
import cmd
"""Command line interface for AirBnB clone"""

class_list = {'BaseModel': BaseModel}

class HBNBCommand(cmd.Cmd):
    """Command line interface for AirBnB clone"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new BaseModel instance, saves it and prints the id"""
        if not arg:
            print('** class name missing **')
            return
        for key, value in class_list.items():
            if key == arg:
                new_obj = value()
                new_obj.save()
                print(new_obj.id)
                return
        print("** class doesn't exist **")

    def do_show_arg(self, arg):
        print(arg)
        if not arg:
            print('no arg')

    def do_quit(self, arg):
        """Quit hbnb shell"""
        return True

    def do_EOF(self, arg):
        """Quit hbnb shell"""
        return True

    @staticmethod
    def split_arg(arg):
        return arg.split(sep=' ')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
