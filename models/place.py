#!/usr/bin/python3
""" Place Module for HBNB project """
from email.policy import default
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float


class Place(BaseModel):
    """ A place to stay """
    city_id = Column(String(60), nullable=False)
    user_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    __tablename__ = "places"
