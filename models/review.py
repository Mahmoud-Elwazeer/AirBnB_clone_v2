#!/usr/bin/python3
"""Review sub-class that inherit from BaseModel
"""
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """sub class that inherit from BaseModel
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60),ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id",
        ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    user = relationship("User", back_populates="reviews")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
