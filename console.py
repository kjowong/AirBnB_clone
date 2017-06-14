#!/usr/bin/python3
""" Entry point to command line interpretor """
import cmd
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ entry point to hbnb"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ End of the file """
        print()
        return True

    def emptyline(self):
        """Empty Line"""
        pass

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
        """ print string rep of an instance based on class name/id """
        if not line:
            print("** class name missing **")
        else:
            cmd = line.split()
            flag = 0
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
                            flag = 1
                    if (flag == 0):
                        print("** no instance found **")
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
            obj = storage.all()
            if (len(storage.all()) == 0):
                print("[]")
            for key in obj.keys():
                print(obj[key])
        else:
            cmd = line.split()
            if (cmd[0] in classes):
                obj = storage.all()
                if (len(storage.all()) == 0):
                    print("[]")
                for key in obj.keys():
                    if obj[key].__class__.__name__ == cmd[0]:
                        print(obj[key])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ updates an instance based on the class and id """
        if not line:
            print("** class name missing **")
        else:
            cmd = line.split()
            if (cmd[0] in classes):
                if (len(cmd) < 2):
                    print("** instance id missing **")
                    return
                elif ((str(cmd[0]) + "." + str(cmd[1]))
                      not in storage.all().keys()):
                    print("** no instance found **")
                    return
                elif (len(cmd) < 3):
                    print("** attribute name missing **")
                    return
                elif (len(cmd) < 4):
                    print("** value missing **")
                    return
                else:
                    obj = storage.all()
                    new = str(cmd[0]) + "." + str(cmd[1])
                    for key in obj.keys():
                        if (new == key):
                            temp = obj[key]
                            try:
                                cmd[3] = cmd[3].strip('"')
                                cmd[3] = int(cmd[3])
                            except:
                                pass
                            setattr(temp, cmd[2], cmd[3])
                            storage.save()
                            flag = 1
                    if (flag == 0):
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_BaseModel(self, line):
        """ doing functions on BaseModel """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("BaseModel")

    def do_Amenity(self, line):
        """ for functions on Amenity"""
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("Amenity")

    def do_City(self, line):
        """ for functions on City"""
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("City")

    def do_Place(self, line):
        """ for functions on Place """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("Place")

    def do_Review(self, line):
        """for functions on Review """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("Review")

    def do_State(self, line):
        """for functions on State """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("State")

    def do_User(self, line):
        """for functions on User """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("User")

if __name__ == '__main__':
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review}
    HBNBCommand().cmdloop()
