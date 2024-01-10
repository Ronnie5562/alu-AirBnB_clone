#!/usr/bin/python3
"""
This module serves as the initialization file for the models package.
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


classes = {
    "BaseModel": BaseModel,
}