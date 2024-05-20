#!/usr/bin/env python3
"""
Defines the HBNBCommand class.
"""
import cmd
import re
import json
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
            elif method_name == "count":
                return f"count {class_name}"
            elif method_name == "show":
                method_args = method_args.strip('\"')
                return f"show {class_name} {method_args}"
            elif method_name == "destroy":
                method_args = method_args.strip('\"')
                return f"destroy {class_name} {method_args}"
            elif method_name == "update":
                params = method_args.split(", ")
                if len(params) == 3:
                    instance_id = params[0].strip('\"')
                    attr_name = params[1].strip('\"')
                    attr_value = params[2].strip('\"')
                    # attr_name_or_dict = params[1].strip()
                    # if (attr_name_or_dict.startswith("{") and
                    #         attr_name_or_dict.endswith("}")):
                    #     return (
                    #         f"update {class_name} {instance_id} "
                    #         f"{attr_name_or_dict}"
                    #     )
                    # else:
                    #     attr_name, attr_value = attr_name_or_dict.split(", ")
                    #     attr_name = attr_name.strip('\"')
                    #     attr_value = attr_value.strip('\"')
                    return (
                        f"update {class_name} {instance_id} "
                        f"{attr_name} {attr_value}"
                    )
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

    def do_count(self, args):
        """
        Retrieves the number of instance of a class.
        Usage: count <class name>
        """
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        count = sum(1 for key in objs if key.startswith(args + '.'))
        print(count)

    def do_update(self, args):
        """
        Update an instance based on class name and id by
        adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        or <class name>.update(<id>, <attribute name>, <attribute value>)
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
        if len(tokens) < 3:
            print("** attribute name missing **")
            return
        if len(tokens) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = tokens[2]
        attr_value = tokens[3]
        # attr_name_or_dict = tokens[2]

        # checks if the third argument is a dictionary
        # if (attr_name_or_dict.startswith("{") and
        #         attr_name_or_dict.endswith("}")):
        #     try:
        #         attr_dict = json.loads(attr_name_or_dict)
        #     except json.JSONDecodeError:
        #         print("** invalid dictionary format **")
        #         return
        #     for attr_name, attr_value in attr_dict.items():
        #         if isinstance(attr_value, str):
        #             attr_value = attr_value.strip('"')
        #         setattr(obj, attr_name, attr_value)
        # else:
        #     attr_tokens = attr_name_or_dict.split(", ")
        #     if len(attr_tokens) < 2:
        #         print("** value missing **")
        #         return
        #     attr_name = attr_tokens[0]
        #     attr_value = attr_tokens[1]

        # convert the attribute value to the correct type
        if attr_value.isdigit():
            attr_value = int(attr_value)
        elif (attr_value.replace('.', '', 1).isdigit() and
                attr_value.count('.') < 2):
            attr_value = float(attr_value)
        else:
            attr_value = attr_value.strip('"')

        setattr(obj, attr_name, attr_value)
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
