#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Ensure a new line after EOF is entered
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return

        if arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Show all instances of a class,
        or all instances if no class is specified."""
        if not arg:
            print([str(v) for v in storage.all().values()])
        elif arg == "BaseModel":
            print(
                [
                    str(v) for v in storage.all().values()
                    if isinstance(v, BaseModel)
                ]
            )
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id by
        adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attribute_name = args[2]
        attribute_value = args[3].strip('"')
        # Cast attribute_value to correct type (string, integer, float)
        if attribute_value.isdigit():
            attribute_value = int(attribute_value)
        elif attribute_value.replace('.', '', 1).isdigit():
            attribute_value = float(attribute_value)
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
