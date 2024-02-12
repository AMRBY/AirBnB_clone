#!/usr/bin/python3
"""
Command Line Interpreter
"""
from models.engine.file_storage import FileStorage
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class to manage the CLI
    args:
        prompt: "(hbnb) " display in loop
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """do nothing when emptyline
        """
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

    def do_all(self, arg):
        'Show all instances based on class name.'
        my_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_key = key.split(".")
                if my_key[0] == my_arg[0]:
                    my_list.append(str(values))
            print(my_list)


    def quoted(self, string):
        """detect and delete quotes
        """
        new_string = string
        if(string[0] == '"' and string[-1] == '"'):
            new_string = string[1:-1]
        elif(string[0] == '"'):
            new_string = string[1:]
        elif(string[-1] == '"'):
            new_string = string[:-1]
        return new_string

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
                        x_value = HBNBCommand.quoted(self, args.split()[3])
                        setattr(objs[key_id], x_key, x_value)
                        storage.save()

                except Exception as e:
                    print("** no instance found **")
                    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
