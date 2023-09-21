#!/usr/bin/python3
"""the __init__ module
"""

# from models.engine.file_storage import FileStorage
# from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os

# storage_type = os.getenv("HBNB_TYPE_STORAGE")
# if (storage_type == "db"):
#     storage = DBStorage()
#     storage.reload()
# else:
#     storage = FileStorage()
#     storage.reload()

# storage_type = os.getenv('HBNB_TYPE_STORAGE')


# if storage_type == "db":
#     from models.engine.db_storage import DBStorage
#     storage = DBStorage()
# else:
#     from models.engine.file_storage import FileStorage
#     storage = FileStorage()
# storage.reload()


#!/usr/bin/python3
"""the __init__ module
"""


storage = FileStorage()
storage.reload()
