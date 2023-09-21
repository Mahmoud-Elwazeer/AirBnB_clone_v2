#!/usr/bin/python3
"""Amenity sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity model"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
