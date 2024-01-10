#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""


import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    ruler = "="
    
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
        An empty line + ENTER shouldn't execute anything
        """
        pass
    
    def do_create(self, arg):
        """
        Creates a new inst of BaseModel, saves it (to the JSON file) and prints the id.
        """
        
        class_name = arg.split(" ")[0]
        
        if not class_name:
            print("** class name missing **")
        elif class_name not in models.classes:
            print("** class doesn't exist **")
        else:
            instance = models.classes[class_name]()
            instance.save()
            print(instance.id)
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()