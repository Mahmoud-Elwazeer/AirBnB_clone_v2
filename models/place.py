#!/usr/bin/python3
"""Place sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
# from models.amenity import Amenity   # gives ERROR
import os

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(
        "cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey(
        "users.id"), nullable=False)
    name = Column(String(120), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place",
                           cascade="all, delete, save-update")
    amenities = relationship(
        "Amenity", secondary=place_amenity, viewonly=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.amenity_ids = []

    @property
    def reviews(self):
        """
        Getter attribute that returns the list of Review instances
        with place_id equals to the current Place.id
        """
        from models import storage
        lst = []

        for review in list(storage.all(Review).values()):
            if self.id == review.place_id:
                lst.append(review)
        return lst

    @property
    def amenities(self):
        """returns the list of Amenity instances based on
        the attribute amenity_ids
        """
        from models import storage
        lst = []
        for amenity in list(storage.all(Amenity).values()):
            if amenity.id in self.amenity_ids:
                lst.append(amenity)
        return lst

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
