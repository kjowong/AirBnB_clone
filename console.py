#!/usr/bin/python3
""" Entry point to command line interpretor """
import cmd
import os
from models.base_model import BaseModel
from models  import storage
from models.engine.file_storage import FileStorage

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
            if cmd[0] is None:
                print("** class name missing **")
            elif (cmd[0] in classes):
                inst = classes[cmd[0]]()
                inst.save()
                print(inst.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        if not line:
            print("** class name missing **")
        else:
            s = line.split()

            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except Exception:
                print("** instance id missing **")
            else:
                if s[0] in classes:
                    obj = storage.all()
                    key = str(s[0]) + '.' + str(s[1])
                    print(obj[key])
                else:
                    print("** class doesn't exist **")

        """

        if not line:
            print("** class name missing **")
        else:
            cmd = line.split()
            if cmd[0] is None:
                print("** class name missing **")
            elif (cmd[0] in classes):
                obj = storage.all()
                if (len(cmd) < 2):
                    print("** instance id missing **")
                else:
                    new = str(cmd[0]) + "." + str(cmd[1])
                    for key in obj.keys():
                        if (new == key):
                            print(obj[new])
            else:
                print("** class doesn't exist **")
    def do_destroy(self, line):
        """ destroy function """
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
                            del obj[key]
                            flag = 1
                            break
                    storage.save()
                    if (flag == 0):
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """ print all instances function """
        if not line:
            print("** class doesn't exist **")
        else:
            cmd = line.split()
            if (cmd[0] in classes):
                obj = storage.all()
                for key in obj.keys():
                    print(obj[key])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ updates an instance based on the class and id """
        if not line:
            print("** class doesn't exist **")
        else:
            cmd = line.split()
            if (cmd[0] in classes):
                if (len(cmd) < 2):
                    print("** instance id missing **")
                elif (len(cmd) < 3):
                    print("** attribute name missing **")
                elif (len(cmd) < 4):
                    print("** value missing **")
                else:
                    obj = storage.all()
                    new = str(cmd[0]) + "." + str(cmd[1])
                    print(new)
                    for key in obj.keys():
                        print(key)
                        if (new == key):
                            temp = obj[key]
                            print("---------")
                            print("temp: {}", format(temp))
                            temp[cmd[2]] = cmd[3]
                            #temp.update(cmd[2]: cmd[3])
                            storage.save()
                            print("----------")
                            print("obj[key]: {}".format(obj[key]))
                        else:
                            print("nope")
                    storage.save()

if __name__ == '__main__':
    classes = {"BaseModel": BaseModel}
    HBNBCommand().cmdloop()
