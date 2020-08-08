#!/usr/bin/python3
""" module """

# imports
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


# use base to create relation with db_table
class City(Base):
    """ class """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

# connect to the db

# perform the quarry
