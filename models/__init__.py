#!/usr/bin/python3
"""the __init__ module
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_type = os.getenv("HBNB_TYPE_STORAGE")
if (storage_type == "db"):
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
