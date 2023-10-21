#!/usr/bin/python3
"""City sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    if (models.storage_type == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        # state_id = Column(String(60), ForeignKey(
        #     "states.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
        # state = relationship("State", back_populates="cities")

        # places = relationship("Place", backref="cities",
        #                     cascade="all, delete, save-update")
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
