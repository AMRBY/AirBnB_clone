#!/usr/bin/python3
"""
Command Line Interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class to manage the CLI
    args:
        prompt: "(hbnb) " display in loop
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Amenity",
               "Place", "Review", "State", "City"]

    def emptyline(self):
        """do nothing when emptyline
        """
        pass

    def do_quit(self, args):
        """exit the CLI
        """
        return True

    def do_EOF(self, args):
        """exit the CLI
        """
        return True

    def do_create(self, args):
        """create an object, saves it and print its id
        """
        if (args == ""):
            print("** class name missing **")
        elif (args.split()[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
        else:
            obj = eval(args.split()[0]+"()")
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """show a string representation of an object
        """
        if (args == ""):
            print("** class name missing **")
        else:
            if (args.split()[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
            elif (len(args.split()) == 1):
                print("** instance id missing **")
            else:
                objs = storage.all()
                key_id = args.split()[0] + "." + args.split()[1]
                try:
                    print(objs[key_id])
                except Exception:
                    print("** no instance found **")
                    pass

    def do_destroy(self, args):
        """destroy an object
         """
        if (args == ""):
            print("** class name missing **")
        else:
            class_name, instance_id = args.split()
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif (len(args.split()) == 1):
                print("** instance id missing **")
            else:
                objs = storage.all()
                key_id = class_name + "." + instance_id
                try:
                    del(objs[key_id])
                    storage.save()
                except KeyError:
                    print("** no instance found **")
                    pass

    def do_all(self, args):
        """display all objects based on class
        """
        lista = []
        objs = storage.all()
        if (args == ""):
            for v in objs.values():
                lista.append(str(v))
            print(lista[:])
        elif (args.split()[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
        else:
            for k, v in objs.items():
                if (k.split('.')[0] == args.split()[0]):
                    lista.append(str(v))
            print(lista[:])

    def quoted(self, args):
        """detect and delete quotes
        """
        i = 3
        string = args.split()[i]
        new_string = args.split()[i]
        if(string[0] == '"' and string[-1] == '"'):
            new_string = string[1:-1]
        elif(string[0] == '"'):
            while(string[-1] != '"'):
                string = string + " " + args.split()[i + 1]
                i = i + 1
            new_string = string[1:-1]
        """
            elif(string[-1] == '"'):
            new_string = string[:-1]
        """
        return new_string

    def do_update(self, args):
        """update an object from a class
        """
        if (args == ""):
            print("** class name missing **")
        else:
            if (args.split()[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
            elif (len(args.split()) == 1):
                print("** instance id missing **")
            else:
                objs = storage.all()
                key_id = args.split()[0] + "." + args.split()[1]
                try:
                    objs[key_id]
                    if (len(args.split()) == 2):
                        print("** attribute name missing **")
                    elif (len(args.split()) == 3):
                        print("** value missing **")
                    else:
                        x_key = args.split()[2]
                        x_value = HBNBCommand.quoted(self, args)
                        setattr(objs[key_id], x_key, x_value)
                        storage.save()

                except Exception as e:
                    print("** no instance found **")
                    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
