#!/usr/bin/python3
"""
entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ command interpreter
    """
    prompt = "(hbnb) "
    classname = ['BaseModel']

    def do_quit(self, line):
        """ quit command """
        return True

    def do_EOF(self, line):
        """ EOF command """
        return True

    def emptyline(self):
        """ do nothing """
        pass

    def do_create(self, arg):
        """ creates a new instance of BaseModel """

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classname:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel}
            my_model = dct[arg]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ show string representation of an instance """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classname:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, value in objs.items():
                obj_name = value.__class.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strp('"'):
                    print(value)
                    return
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
