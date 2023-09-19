#!/usr/bin/python3
"""Storage module for storing the date as JSON format
"""

from models.all_models import our_models
import json


class FileStorage:
    """class sued for serialization and deserialization

    Attrs:
        file_path: path to the JSON file
        objects: dictionary to store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """sets in objects attribute the obj
        with calssName.<id> as key
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """method used for converting python object into
        JSON string
        """
        # convert_to_dict = {key: obj.to_dict() for key, obj
        # in self.__objects.items()}
        convert_to_dict = {}
        for key, value in self.__objects.items():
            convert_to_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as fp:
            json.dump(convert_to_dict, fp, indent=4)

    def reload(self):
        """method used for converting JSON strign into
        python obect
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as fp:
                data = json.load(fp)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = our_models[class_name](**value)
                    self.__objects[key] = obj
                    # self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
