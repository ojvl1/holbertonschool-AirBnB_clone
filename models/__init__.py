#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

allclasses = {"BaseModel": BaseModel,
              "User": User,
              "City": City,
              "State": State,
              "Place": Place,
              "Amenity": Amenity,
              "Review": Review}

storage = FileStorage()
storage.reload()
