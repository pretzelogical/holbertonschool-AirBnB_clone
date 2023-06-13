#!/usr/bin/python3
"""
Write a program called console.py
that contains the entry point of
the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """holberton command class delaration"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()