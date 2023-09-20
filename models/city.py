#!/usr/bin/python3
"""City sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    # state_id = ""
    # name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
