#!/usr/bin/python3
"""New engine for database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.all_models import our_models
from models.base_model import BaseModel, Base


class DBStorage:
    """database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """init special method
        """
        self.user = os.getenv("HBNB_MYSQL_USER")
        self.passwd = os.getenv("HBNB_MYSQL_PWD")
        self.host = os.getenv("HBNB_MYSQL_HOST")
        self.db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".
            format(self.user, self.passwd, self.host, self.db),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create the current database session with expire_on_commit=False
        # session_factory = sessionmaker(
        #     bind=self.__engine, expire_on_commit=False)
        # self.__session = scoped_session(session_factory)

        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()
        # metadata = MetaData(bind=self.__engine)

        # if os.getenv("HBNB_ENV") == "test":
        #     metadata.drop_all()
        #     self.__session.commit()

    def all(self, cls=None):
        """query on the current database session (self.__session)
            all objects depending of the class name """
        # if cls is None:
        #     # query all objects
        #     self.objs = self.__session.query(
        #         our_models["City"]
        #         # our_models["City"],
        #         # our_models["State"],
        #         # our_models["Place"],
        #         # our_models["Review"],
        #         # our_models["Amenity"]
        #     ).all()
        # else:
        if cls is None:
            objects = []
            for i in our_models.values():
                if (i == BaseModel):
                    continue
                # print(i)
                objects.extend(self.__session.query(i).all())
                # obj = self.__session.query(i).all()
                # objects.append(obj)
        else:
            objects = self.__session.query(cls).all()
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objects}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        # Create a session with the specified options
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        self.__session.remove()
