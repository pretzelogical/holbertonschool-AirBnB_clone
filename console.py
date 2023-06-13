#!/usr/bin/python3
"""
Write a program called console.py
that contains the entry point of
the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """declaring hbtn command class"""
    def quit(self, arg):
        """method to quit the program"""
        return True

    def EOF(self, arg):
        """method EOF"""
        return True

    def blank_line(self, arg):
        """method for a blank line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()