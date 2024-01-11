#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    
    def do_quit(self, arg):
        """
        Quit the console.

        Usage:
            quit
            q
            exit
        """
        return True
    
    do_q = do_quit
    do_exit = do_quit
    
    def do_EOF(self, arg):
        """
        Quit the console.

        Usage:
            EOF
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
        
        Usage: create <class_name>
        
        Args:
            arg (str): The argument should contain the <class_name>.
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
    
    def do_show(self, arg):
        """
        Displays the string representation of an instance.
        
        Usage: create <class_name> <instance_id>
        
        Args:
            arg (str): The argument should contain <class_name> and <instance_id>.
        """
        
        split_args = arg.split(" ")
        class_name = split_args[0] if len(split_args) > 0 else None
        obj_id = split_args[1] if len(split_args) > 1 else None
        
        if not class_name:
            print("** class name missing **")
        elif class_name not in models.classes:
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{obj_id}"
            if key in models.loaded_objects:
                print(models.loaded_objects[key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        
        Usage: destroy <class_name> <instance_id>
        
        Args:
            arg (str): The argument should contain <class_name> and <instance_id>.
        """
        
        split_args = arg.split(" ")
        class_name = split_args[0] if len(split_args) > 0 else None
        obj_id = split_args[1] if len(split_args) > 1 else None
        
        if not class_name:
            print("** class name missing **")
        elif class_name not in models.classes:
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{obj_id}"
            if key in models.loaded_objects:
                del models.loaded_objects[key]
                models.storage.save()
            else:
                print("** no instance found **")
    
    do_delete = do_destroy
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()