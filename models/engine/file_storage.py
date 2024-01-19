#!/usr/bin/python3
"""
Storage in JSON format
"""
import json
import os.path


class FileStorage:
    # path to the JSON file
    __file_path = "file.json"
    # store all objects by <class name>.id
    # (ex: to store a BaseModel object with id=12121212:
    # the key will be BaseModel.12121212)
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj
        with the key: <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {}

        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the
        JSON file exists; otherwise, do nothing. No exception should be raised
        """
        from models import classNames
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objs = json.load(file)

            for key, value in objs.items():
                class_name, obj_id = key.split('.')
                if class_name in classNames:
                    obj = classNames[class_name](**value)
                    self.__objects[key] = obj
