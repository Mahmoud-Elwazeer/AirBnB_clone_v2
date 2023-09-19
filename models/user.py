#!/usr/bin/python3
"""user sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """sub class that inherit from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """the __init__ special method"""
        super().__init__(*args, **kwargs)

    # def to_dict(self):
    #     """method to return dict representation for the class"""
    #     return super().to_dict()
