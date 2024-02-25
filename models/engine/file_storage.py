#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as myfile:
                jsondict = json.load(myfile)
                for key in jsondict:
                    classname = jsondict[key]["__class__"]
                    self.__objects[key] = classes[classname](**jsondict[key])
        except FileNotFoundError:
            pass
