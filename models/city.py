#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, ForeignKey


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if HBNB_TYPE_STORAGE == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship(
            "Place",
            cascade="all",
            backref=backref("cities", cascade="all"),
            passive_deletes=True
        )
    else:
        state_id = ""
        name = ""
