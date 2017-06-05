#!/usr/bin/python3
""" Entry point to command line interpretor """
import cmd
import os


class HBNBCommand(cmd.Cmd):
    """ entry point to hbnb"""
#    intro = "Simple command line interpretor"
    prompt = '(hbnb) \n'

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        "End of the file"
        return True

    def emptyline(self):
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
