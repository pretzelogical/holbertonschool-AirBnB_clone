#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import cmd
"""Command line interface for AirBnB clone"""

class_list = {'BaseModel': BaseModel}
error_messages = {'classMiss': '** class name missing **',
                  'classNotExist': "** class doesn't exist **",
                  'idMiss': "** instance id missing **",
                  'idNoInstance': "** no instance found **"}

class HBNBCommand(cmd.Cmd):
    """Command line interface for AirBnB clone"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new BaseModel instance, saves it and prints the id
        ex: create BaseModel
        """
        if not arg:
            print(error_messages['classMiss'])
            return
        for key, value in class_list.items():
            if key == arg:
                new_obj = value()
                new_obj.save()
                print(new_obj.id)
                return
        print(error_messages['classNotExist'])

    def do_show(self, arg):
        """Show an instance ex: show <obj> <id>"""
        if not arg:
            print(error_messages['classMiss'])
            return
        args = self.split_arg(arg)
        name = args[0]
        objects = storage.all()

        if name not in class_list.keys():
            print(error_messages['classNotExist'])
            return

        if len(args) != 2:
            print(error_messages['idMiss'])
            return
        id = args[1]

        try: print(objects[f'{name}.{id}'])
        except: print(error_messages['idNoInstance']); return

    def do_destroy(self, arg):
        """Deletes an instance, and saves the change
        ex: destroy BaseModel 1234-1234
        """
        if not arg:
            print(error_messages['classMiss'])
            return
        args = self.split_arg(arg)
        name = args[0]
        objects = storage.all()

        if name not in class_list.keys():
            print(error_messages['classNotExist'])
            return

        if len(args) != 2:
            print(error_messages['idMiss'])
            return
        id = args[1]

        try: objects.pop(f'{name}.{id}')
        except: print(error_messages['idNoInstance']); return

    def do_all(self, arg):
        """Prints all string representation based on class name"""
        all = storage.all()
        if arg:
            if arg not in class_list.keys():
                print(error_messages['classMiss'])
            for key, val in all.items():
                if isinstance(val, class_list[arg]):
                    print(val)
        else:
            for key, val in all.items():
                print(val)

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
