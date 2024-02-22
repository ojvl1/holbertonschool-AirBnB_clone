#!/usr/bin/python3

import json
import models


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        dic = {}
        for id, objs in self.__objects.items():
            dic[id] = objs.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dic, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
              data = json.load(file)
              for key, value in data.items():
                    class_name = models.allclasses[value['__class__']](**value)
                    self.__objects[key] = class_name
        except FileNotFoundError:
            pass
