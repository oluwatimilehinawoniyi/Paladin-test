#!/usr/bin/python3
"""paladin console"""

import cmd

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class PaladinCommand(cmd.Cmd):

    prompt = "Paladin--> "

    models = ["BaseModel", "User", "Place", "City", "Amenity", "Review",
              "State"]

    classMissing = "** class name missing **"
    classNotExisting = "** class doesn't exist **"
    noInstance = "** no instance found **"
    noInstanceID = "** instance id missing **"

    def do_create(self, model):
        """creates a new instance of model, saves it
        to the JSON file and prints the id"""
        # print(type(model))
        if model:
            if model in self.models:
                instance = BaseModel()
                instance.save()
                print(instance.id)
            else:
                print(self.classNotExisting)
        else:
            print(self.classMissing)

    def do_show(self, arg):
        """prints the string representation of an instance
        based on the class name and id.
        Example: show BaseModel 1111-2222-3333-4444"""
        args = arg.split()
        if len(args) > 0:
            model = args[0]
            if model in self.models:
                if len(args) == 2:
                    id = args[1]
                    key = f"{model}.{id}"
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print(self.noInstance)
                    # ALTERNATIVE BUT LONG VERSION
                    # if os.path.exists("file.json"):
                    #     with open("file.json", 'r') as file:
                    #         objs = json.load(file)
                    #     for key, value in objs.items():
                    #         obj_cls, obj_id = key.split('.')
                    #         if obj_id == id:
                    #             print(classNames[model](**value))
                    #             return
                    #     print(self.noInstance)
                else:
                    print(self.noInstanceID)
            else:
                print(self.classNotExisting)
        else:
            print(self.classMissing)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file"""
        args = arg.split()
        if len(args) > 0:
            model = args[0]
            if model in self.models:
                if len(args) == 2:
                    id = args[1]
                    key = f"{model}.{id}"
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print(self.noInstance)
                else:
                    print(self.noInstanceID)
            else:
                print(self.classNotExisting)
        else:
            print(self.classMissing)

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        Example: $ all BaseModel or $ all
        :param arg:
        """
        if not arg or arg in models.classNames:
            print([str(value) for key, value in storage.all().items()])
        else:
            print(self.classNotExisting)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).
        Ex:
        update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        if len(args) > 0:
            model = args[0]
            if model in self.models:
                if len(args) > 2:
                    id = args[1]
                    key = f"{model}.{id}"
                    if key in storage.all():
                        if args[2]:
                            if args[3]:
                                setattr(storage.all()[key], args[2],
                                        args[3].strip('"'))
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print(self.noInstance)
                else:
                    print(self.noInstanceID)
            else:
                print(self.classNotExisting)
        else:
            print(self.classMissing)

    def do_EOF(self, line):
        """end of file"""
        return True

    def do_quit(self, line):
        """cmd to quit the program"""
        return True

    def emptyline(self):
        """command to do nothing when the line is empty
        and enter key is pressed"""
        return


if __name__ == "__main__":
    PaladinCommand().cmdloop()
