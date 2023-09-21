#!/usr/bin/python3
"""New engine for database
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
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
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".
            format(user, passwd, host, db),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create the current database session with expire_on_commit=False
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()
        # metadata = MetaData(bind=self.__engine)

        # if os.getenv("HBNB_ENV") == "test":
        #     metadata.drop_all()
        #     self.__session.commit()

    # def all(self, cls=None):
    #     """query on the current database session (self.__session)
    #         all objects depending of the class name """
    #     if cls is None:
    #         objects = []
    #         out_dict = {}
    #         for i in our_models.values():
    #             if (i == BaseModel):
    #                 continue
    #             objects.extend(self.__session.query(i).all())
    #             # obj = self.__session.query(i).all()
    #             # objects.append(obj)
    #     else:
    #         objects = self.__session.query(cls).all()

    #     for obj in objects:
    #         key = obj.__class__.__name__ + '.' + obj.id
    #         out_dict[key] = obj
    #     return out_dict

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

        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)

        Session = scoped_session(self.__session)
        self.__session = Session()
