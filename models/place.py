#!/usr/bin/python3
"""Place sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(
        "cities.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    user_id = Column(String(60), ForeignKey(
        "users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    name = Column(String(String(120)), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place", cascade="all, delete")

    # cites = relationship("City", back_populates="places")

    # city_id = ""
    # user_id = ""
    # name = ""
    # description = ""
    # number_rooms = 0
    # number_bathrooms = 0
    # max_guest = 0
    # price_by_night = 0
    # latitude = 0.0
    # longitude = 0.0
    # amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
