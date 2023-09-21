#!/usr/bin/python3
"""Amenity sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
# from models.place import place_amenities


class Amenity(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    if (models.storage_type == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place", secondary=place_amenities)
    else:
        name = ""
