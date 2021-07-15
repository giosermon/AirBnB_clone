#!/usr/bin/python3
"""Console Command processor module to control Airbnb Console
"""
import cmd
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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

    classes =\
        ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

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
            list_args = arg.split()
            if list_args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        dic = storage.all()
        for key, value in dic.items():
            data.append(str(value))
        print(data)

    def do_update(self, arg):
        '''
            Update an instance based on the class name and id
            sent as args.
        '''
        self.non_interactive_mode()
        list_args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        elif list_args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif list_args[0] in HBNBCommand.classes and len(list_args) == 1:
            print("** instance id missing **")
            return
        elif len(list_args) == 2:
            key = "{}.{}".format(list_args[0], list_args[1])
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return
            elif len(list_args) == 2 and key in objects:
                print("** attribute name missing **")
                return
        elif len(list_args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(list_args[0], list_args[1])
        objects = storage.all()
        setattr(objects[key], list_args[2], list_args[3])
        storage.save()
        
    def exect(self, line):
        """Method to run same commands as class.method"""
        # Make a copy of line
        cp = line[:]
        cp2 = line.split('.', 1)
        if len(cp2) < 2:
            return cp
        else:
            count1, count2 = cp.count(')'), cp.count('(')
            endp_p = len(cp)-1

            if count1 != 1 or count2 != 1 or ')' != cp[endp_p]:
                return cp

            idx = cp.index('(')
            if cp[idx-1].isalpha() is False:
                return cp

            mycls = cp2[0]

            cp2[1] = cp2[1].replace('(', ', ')

            cp2[1] = cp2[1].replace(')', '')


            mycmd = cp2[1].split(', ', 1)[0]
            count1, count2 = cp2[1].count('}'), cp2[1].count('{')
            endp_p = len(cp2[1])-1
            if mycmd == "update":
                myargs = cp2[1].split(', ', 1)[1]
                if count1 == 1 and count2 == 1 and '}' == cp2[1][endp_p]:

                    myargs = myargs.split(', ', 1)

                    myid = myargs[0]
                    mydict = eval(myargs[1])
                    for key, value in mydict.items():
                        ucmd = mycls+' '+myid+' '+key+' '+'\"'+str(value)+'\"'
                        self.do_update(ucmd)
                    return " "

            mycmd += ' '+mycls+' '+cp2[1].split(', ', 1)[1]
            mycmd = mycmd.replace(',', '')

            return mycmd


if __name__ == '__main__':
    hb = HBNBCommand
    HBNBCommand().cmdloop()
