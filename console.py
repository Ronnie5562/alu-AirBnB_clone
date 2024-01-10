#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """
        Quit the console.

        This method is called when the user enters the 'quit' command in the console.
        """
        return True

    def do_EOF(self, arg):
        """
        Quit the console.

        This method is called when the user enters the 'EOF' command in the console.
        """        
        return True
    
    def emptyline(self):
        """
        Empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()