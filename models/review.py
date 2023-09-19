#!/usr/bin/python3
"""Review sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """sub class that inherit from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
