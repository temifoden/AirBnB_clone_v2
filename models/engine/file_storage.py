"""
Defines the FileStorage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        if cls is specified, returns a dictionary of objects of that type"""

        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __object to the JSON file (path: __file_path).
        """
        json_objects = {
            key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delet obj from __object if it's inside
        If obj is equal to None, the method should not do anything
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
            self.save()
        
