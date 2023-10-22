#!/usr/bin/python3
"""module has BaseModule"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

if (models.storage_type == "db"):
    Base = declarative_base()
else:
    Base = object


time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel that defines all common attributes/methods
    for other classes
    """
    if (models.storage_type == "db"):
        id = Column(String(60), unique=True, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """init magic method

        Args:
            args: is a Tuple that contains all arguments (unused)
            kwargs:  is a dictionary that contains all arguments by key/value
        """

        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        # if len(kwargs) == 0:
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """string representation of instance
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

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
        # class_name = self.__class__.__name__
        # self.created_at = self.created_at.strftime(time)
        # self.updated_at = self.updated_at.strftime(time)
        # self.__dict__["__class__"] = class_name

        # if "_sa_instance_state" in self.__dict__.keys():
        #     del self.__dict__["_sa_instance_state"]
        # return self.__dict__
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage
        """
        models.storage.delete(self)
