#!/usr/bin/python3
""" Entry point to command line interpretor """
import cmd
import os
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """ entry point to hbnb"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self, line):
        "End of the file"
        return True

    def emptyline(self):
        return False

    def do_create(self, line):
        """ Create new instance of BaseModel """
        if not line:
            print("** class name missing **")
        else:
            cmd = line.split()
            if (cmd[0] in classes):
                inst = classes[cmd[0]]()
                inst.save()
                print(inst.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ Show prints the string representation of an instance """
        cmd = line.split()
        if not line:
            print("** class name missing **")
        else:
            if cmd[0] in classes:
                inst = classes[cmd[0]]()
                if not cmd[1]:
                    print("** instance id missing **")
                elif cmd[1]:
                    print(inst.storage)
                else:
                    print("** id doesn't exist **")
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    classes = {"BaseModel": BaseModel}
    HBNBCommand().cmdloop()
