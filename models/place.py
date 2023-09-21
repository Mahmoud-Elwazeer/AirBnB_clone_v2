from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import os

place_amenities = Table(
    'place_amenity', Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(
        "cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey(
        "users.id"), nullable=False)
    name = Column(String(120), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.amenity_ids = []

    reviews = relationship("Review", backref="place",
                           cascade="all, delete, save-update")

    amenities = relationship(
        "Amenity", secondary=place_amenities, viewonly=False)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            from models import storage
            lst = []
            for review in storage.all(Review).values():
                if self.id == review.place_id:
                    lst.append(review)
            return lst

        @property
        def amenities(self):
            from models import storage
            lst = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    lst.append(amenity)
            return lst

        @amenities.setter
        def amenities(self, obj=None):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
