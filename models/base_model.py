#!/usr/bin/python3
"""module has BaseModule"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """init magic method

        Args:
            args: is a Tuple that contains all arguments (unused)
            kwargs:  is a dictionary that contains all arguments by key/value
        """
        id = Column(String(60), unique=True, primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        # if len(kwargs) == 0:
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    # convert string format into datetime object
                    # datetime.strptime(string_format, datetime_fromat)
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], dt_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], dt_format)
                else:
                    setattr(self, key, value)

    def __str__(self):
        """string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of the instance
        """
        class_name = self.__class__.__name__
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["__class__"] = class_name
        return self.__dict__

    def delete(self):
        """delete the current instance from the storage
        """
        models.storage.delete(self)
