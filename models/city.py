#!/usr/bin/python3
"""City sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """sub class that inherit from BaseModel
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
