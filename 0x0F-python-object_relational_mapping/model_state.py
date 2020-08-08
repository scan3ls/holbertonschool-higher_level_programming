#!/usr/bin/python3
""" module """

# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# creates the engine
# format("user", "passwd", "db_name")
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    "root", "", "hbtn_0d_usa"
), pool_pre_ping=True)

# creates the session
Session = sessionmaker(bind=engine)

# creates declarative base
Base = declarative_base()


# use base to create relation with db_table
class State(Base):
    """ class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

# connect to the db

# perform the quarry
