#!/usr/bin/env python3
"""
Defines the HBNBCommand class.
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Defines the Command interpreter for the HBNB project.
    """
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def parse_method_call(self, args):
        """
        Parses method calls in the form of <class name>.<method>(<params>)
        """
        match = re.fullmatch(r"(\w+)\.(\w+)\((.*)\)", args)
        if match:
            class_name, method_name, method_args = match.groups()
            return class_name, method_name, method_args
        return None, None, None

    def precmd(self, line):
        """
        Pre-processes the command line input.
        """
        class_name, method_name, method_args = self.parse_method_call(line)
        if class_name and method_name:
            if method_name == "all":
                return f"all {class_name}"
        return line

    def do_create(self, args):
        """
        Create a new instance of BaseModel or User,
        saves it (to the JSON file) and print the Id.
        Usage: create <class_name>
        """
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name id.
        Usage: show <class_name> <id>
        """
        tokens = args.split()
        if not args:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Usage: destroy <class_name> <id>
        """
        tokens = args.split()
        if not args:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        Usage: all or all <class_name>
        """
        if args and args not in self.classes:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        obj_list = []
        for key in objs:
            if not args or key.startswith(args + '.'):
                obj_list.append(str(objs[key]))
        print(obj_list)

    def do_update(self, args):
        """Update an instance based on class name and id by
        adding or updating attribute."""
        tokens = args.split()
        if not args:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(tokens) < 3:
            print("** attribute name missing **")
            return
        if len(tokens) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, tokens[2], tokens[3])
        obj.save()

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print("")  # Ensure a new line after EOF is entered
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
