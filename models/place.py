#!/usr/bin/python3
"""Place sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
import os
import models

if (models.storage_type == "db"):
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
    if (models.storage_type == "db"):
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

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """
            Getter attribute that returns the list of Review instances 
            with place_id equals to the current Place.id
            """
            from models import storage
            lst = []

            for review in storage.all(Review).values():
                if self.id == Review.state_id:
                    lst.append(review)
            return lst

        @property
        def amenities(self):
            """returns the list of Amenity instances based on
            the attribute amenity_ids
            """
            from models.amenity import Amenity
            from models import storage
            lst = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    lst.append(amenity)
            return lst

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
