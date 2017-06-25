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

    def counter(self, line):
        """ method to count number of class instances"""
        cmd = line.split()
        if (cmd[0] in classes):
            obj = storage.all()
            count = 0
            for key in obj.keys():
                if obj[key].__class__.__name__ == cmd[0]:
                    count += 1
            print("{:d}".format(count))
        else:
            print("** class doesn't exist **")

    def do_BaseModel(self, line):
        """ doing functions on BaseModel """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("BaseModel")
        elif (cmd[1] == "count()"):
            self.counter("BaseModel")
        try:
            cmd1 = cmd[1].split('(')
            getid = cmd1[1].split(')')
            last = getid[0].split(', ')
        except:
            pass
        if (cmd1[0] == "show"):
            self.do_show("BaseModel {}".format(getid[0]))
        elif(cmd1[0] == "destroy"):
            self.do_destroy("BaseModel {}".format(getid[0]))
        elif(cmd1[0] == "update"):
            self.do_update("BaseModel {} {} {}".
                           format(last[0], last[1], last[2]))

    def do_Amenity(self, line):
        """ for functions on Amenity"""
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("Amenity")
        elif (cmd[1] == "count()"):
            self.counter("Amenity")
        try:
            cmd1 = cmd[1].split('(')
            getid = cmd1[1].split(')')
            last = getid[0].split(', ')
        except:
            pass
        if (cmd1[0] == "show"):
            self.do_show("Amenity {}".format(getid[0]))
        elif(cmd1[0] == "destroy"):
            self.do_destroy("Amenity {}".format(getid[0]))
        elif(cmd1[0] == "update"):
            self.do_update("Amenity {} {} {}".
                           format(last[0], last[1], last[2]))

    def do_City(self, line):
        """ for functions on City"""
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("City")
        elif (cmd[1] == "count()"):
            self.counter("City")
        try:
            cmd1 = cmd[1].split('(')
            getid = cmd1[1].split(')')
            last = getid[0].split(', ')
        except:
            pass
        if (cmd1[0] == "show"):
            self.do_show("City {}".format(getid[0]))
        elif(cmd1[0] == "destroy"):
            self.do_destroy("City {}".format(getid[0]))
        elif(cmd1[0] == "update"):
            self.do_update("City {} {} {}".
                           format(last[0], last[1], last[2]))

    def do_Place(self, line):
        """ for functions on Place """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("Place")
        elif (cmd[1] == "count()"):
            self.counter("Place")
        try:
            cmd1 = cmd[1].split('(')
            getid = cmd1[1].split(')')
            last = getid[0].split(', ')
        except:
            pass
        if (cmd1[0] == "show"):
            self.do_show("Place {}".format(getid[0]))
        elif(cmd1[0] == "destroy"):
            self.do_destroy("Place {}".format(getid[0]))
        elif(cmd1[0] == "update"):
            self.do_update("Place {} {} {}".
                           format(last[0], last[1], last[2]))

    def do_Review(self, line):
        """for functions on Review """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("Review")
        elif (cmd[1] == "count()"):
            self.counter("Review")
        try:
            cmd1 = cmd[1].split('(')
            getid = cmd1[1].split(')')
            last = getid[0].split(', ')
        except:
            pass
        if (cmd1[0] == "show"):
            self.do_show("Review {}".format(getid[0]))
        elif(cmd1[0] == "destroy"):
            self.do_destroy("Review {}".format(getid[0]))
        elif(cmd1[0] == "update"):
            self.do_update("Review {} {} {}".
                           format(last[0], last[1], last[2]))

    def do_State(self, line):
        """for functions on State """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("State")
        elif (cmd[1] == "count()"):
            self.counter("State")
        try:
            cmd1 = cmd[1].split('(')
            getid = cmd1[1].split(')')
            last = getid[0].split(', ')
        except:
            pass
        if (cmd1[0] == "show"):
            self.do_show("State {}".format(getid[0]))
        elif(cmd1[0] == "destroy"):
            self.do_destroy("State {}".format(getid[0]))
        elif(cmd1[0] == "update"):
            self.do_update("State {} {} {}".
                           format(last[0], last[1], last[2]))

    def do_User(self, line):
        """for functions on User """
        cmd = line.split('.')
        if (cmd[1] == "all()"):
            self.do_all("User")
        elif (cmd[1] == "count()"):
            self.counter("User")
        try:
            cmd1 = cmd[1].split('(')
            getid = cmd1[1].split(')')
            last = getid[0].split(', ')
        except:
            pass
        if (cmd1[0] == "show"):
            self.do_show("User {}".format(getid[0]))
        elif(cmd1[0] == "destroy"):
            self.do_destroy("User {}".format(getid[0]))
        elif(cmd1[0] == "update"):
            self.do_update("User {} {} {}".
                           format(last[0], last[1], last[2]))

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
