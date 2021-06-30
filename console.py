#!/usr/bin/python3
"""Console Command processor module to control Airbnb Console
"""
import cmd
import json
import models
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Console Command processor class to control Airbnb Console
    """

    prompt = '(hbnb) '

    """ Classes """
    classes = {"BaseModel": BaseModel, "User": User,
           "City": City, "Place": Place, "Review": Review,
           "State": State, "Amenity": Amenity}

    def do_EOF(self, args):
        """ EOF command to exit the program """
        print()
        return True

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_create(self, args):
        """ Create a new instance of a class """
        if not args:
            print("** class name missing **")
            return None
        try:
            new_instance = eval(args + "()")
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """show command prints the string representation of \
            an instance based on the class name and id
        """
        list_args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if list_args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(list_args) < 2:
            print("** instance id missing **")
            return
        else:
            dic = models.storage.all()
            key = list_args[0] + '.' + str(list_args[1])
            if key in dic:
                print(dic[key])
            else:
                print("** no instance found **")
            return

    def emptyline(self):
        """empty line
        """
        pass

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            list_args = arg.split()
            if list_args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(list_args) < 2:
                print("** instance id missing **")
            else:
                to_delete = "{}.{}".format(list_args[0], list_args[1])
                if to_delete not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[to_delete]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances \
            based or not on the class name
        """
        data = []
        if arg:
            words = arg.split()
            if words[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        dic = storage.all()
        for key, value in dic.items():
            data.append(str(value))
        print(data)

if __name__ == '__main__':
    hb = HBNBCommand
    HBNBCommand().cmdloop()
