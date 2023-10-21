#!/usr/bin/python3
"""State sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    if (models.storage_type == "db"):
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        # relationsip is one (State) to many (City)
        cities = relationship('City', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # if (models.storage_type == "db"):
    #     @property
    #     def cities(self):
    #         """
    #         Getter attribute that returns a list of City instances
    #         with state_id equal to the current State.id
    #         """

    #         from models import storage
    #         lst = []

    #         for city in storage.all(City).values():
    #             if self.id == city.state_id:
    #                 lst.append(city)
    #         return lst
    if models.storage_type != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
