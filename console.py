#!/usr/bin/python3
""" Entry point to command line interpretor """
import cmd


class HBNBCommand(cmd.Cmd):
    """ entry point to hbnb"""
#    intro = "Simple command line interpretor"
    prompt = '(hbnb) '

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        "End of the file"
        return True

    def emptyline(self):
        return False

    def help_quit(self):
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
