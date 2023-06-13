#!/usr/bin/python3
"""
Write a program called console.py
that contains the entry point of
the command interpreter
"""
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel

class_dict = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """declaring hbtn command class"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """method to quit the program"""
        return True

    def do_EOF(self, arg):
        """method EOF"""
        return True

    def emptyline(self):
        """method for a blank line"""
        pass

    def do_create(self, arg):
        """creates a new instance of basemodel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in class_dict.keys():
            print("** class doesn't exist **")
            return
        created_instance = class_dict[arg]
        created_instance.save()
        print(created_instance.id)

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg not in class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        """for key, value in storage.all().items():"""




if __name__ == '__main__':
    HBNBCommand().cmdloop()