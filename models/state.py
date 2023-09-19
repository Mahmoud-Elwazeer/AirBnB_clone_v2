#!/usr/bin/python3
"""State sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """sub class that inherit from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
