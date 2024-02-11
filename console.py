#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
import shlex


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """

    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User", "Amenity", "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.

        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>

        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>

        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()

        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            result = []
            for key, value in objects.items():
                result.append(str(value))
                print(result)
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            result = []
            for key, value in objects.items():
                if key.split(".")[0] == commands[0]:
                    result.append(str(value))
                    print(result)

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        commands = shlex.split(arg)

        if len(commands) < 4:
            print(
                "** Not enough arguments. Usage: update <class_name> <id> <attribute_name> '<attribute_value>' **"
            )
            return

        class_name = commands[0]
        if not class_name:
            print("** class name missing **")
            return

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instance_id = commands[1]
        if not instance_id:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in objects:
            print("** no instance found **")
            return

        instance = objects[key]

        attribute_name = commands[2]
        if not attribute_name:
            print("** attribute name missing **")
            return

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** Cannot update id, created_at, or updated_at **")
            return

        attribute_value = " ".join(commands[3:])
        if not attribute_value:
            print("** value missing **")
            return

        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
