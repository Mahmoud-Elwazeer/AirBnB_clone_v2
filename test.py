#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os


print(1)
engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")))

print(2)
Base = declarative_base()
print(3)
Base.metadata.create_all(engine)
print(4)
# session_factory = sessionmaker(
#         bind=engine, expire_on_commit=False)
# session = scoped_session(session_factory)

# Session = sessionmaker(bind=engine)
# session = Session()
# metadata = MetaData(bind=engine)

# if os.getenv("HBNB_ENV") == "test":
#     metadata.drop_all()
#     session.commit()

# obj = session.query(City).all()
# for i in obj:
#     print(i)