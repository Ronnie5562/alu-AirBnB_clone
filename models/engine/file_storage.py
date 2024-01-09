#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        
    def save(self):
        
        obj_dict = {}
        
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        
        try:
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file)
        except FileNotFoundError:
            pass
    
    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                
                for key, value in obj_dict.items():
                    self.__objects[key] = eval(f"{value['__class__']}(**{value})")
                
        except FileNotFoundError:
            pass