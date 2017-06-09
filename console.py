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
        """ create function """
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
        """ show function """
        if not line:
            print("** class name missing **")
        else:
            cmd = line.split()
            flag = 0
            if (cmd[0] in classes):
                if (len(cmd) < 2):
                    print("** instance id missing **")
                else:
                    obj = storage.all()
                    new = str(cmd[0]) + "." + str(cmd[1])
                    for key in obj.keys():
                        if (new == key):
                            print(obj[key])
                            flag = 1
                    if (flag == 0):
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    classes = {"BaseModel": BaseModel}
    HBNBCommand().cmdloop()
