#!/usr/bin/python3
"""
Command Line Interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class to manage the CLI"""
    prompt = "(hbnb) "

    def emptyline(self):
        """do nothing when emptyline"""
        pass

    def do_quit(self, args):
        """exit the CLI
        """
        return True

    def do_EOF(selfi, args):
        """exit the CLI
        """
        return True

    def do_create(self, args):
        """create an object, saves it and print its id
        """
        if (args == ""):
            print("** class name missing **")
        elif (args != "BaseModel"):
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """show a string representation of an object
        """
        if (args == ""):
            print("** class name missing **")
        else:
            if (args.split()[0] != "BaseModel"):
                print("** class doesn't exist **")
            elif (len(args.split()) == 1):
                print("** instance id missing **")
            else:
                objs = storage.all()
                key_id = "BaseModel." + args.split()[1]
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
            if (args.split()[0] != "BaseModel"):
                print("** class doesn't exist **")
            elif (len(args.split()) == 1):
                print("** instance id missing **")
            else:
                objs = storage.all()
                key_id = "BaseModel." + args.split()[1]
                try:
                    del(objs[key_id])
                    objs.save()
                except Exception:
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
        elif (args != "BaseModel"):
            print("** class doesn't exist **")
        else:
            for k, v in objs.items():
                if (k.split('.')[0] == "BaseModel"):
                    lista.append(str(v))
            print(lista[:])

    def do_update(self, args):
        """update an object from a class
        """
        if (args == ""):
            print("** class name missing **")
        else:
            if (args.split()[0] != "BaseModel"):
                print("** class doesn't exist **")
            elif (len(args.split()) == 1):
                print("** instance id missing **")
            else:
                objs = storage.all()
                key_id = "BaseModel." + args.split()[1]
                try:
                    objs[key_id]
                    if (len(args.split()) == 2):
                        print("** attribute name missing **")
                    elif (len(args.split()) == 3):
                        print("** value missing **")
                    else:
                        x_key = args.split()[2]
                        #objs[key_id].__dict__[x_key] = args.split()[3]
                        setattr(objs[key_id], x_key, args.split()[3])
                        storage.save()

                except Exception as e:
                    print("** no instance found **")
                    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
