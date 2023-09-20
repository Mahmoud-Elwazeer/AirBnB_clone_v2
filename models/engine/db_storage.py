#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from models.all_models import our_models


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.user = os.getenv("HBNB_MYSQL_USER")
        self.passwd = os.getenv("HBNB_MYSQL_PWD")
        self.host = os.getenv("HBNB_MYSQL_HOST")
        self.db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql://{}:{}@{}/{}".
            format(self.user, self.passwd, self.host, self.db),
            pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        metadata = MetaData(bind=self.__engine)

        if os.getenv("HBNB_ENV") == "test":
            metadata.drop_all()
            self.__session.commit()
