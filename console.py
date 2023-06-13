#!/usr/bin/python3
"""
Write a program called console.py
that contains the entry point of
the command interpreter
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()