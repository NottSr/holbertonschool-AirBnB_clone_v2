#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(
        BaseModel, Base if getenv('HBNB_TYPE_STORAGE') == 'db' else object):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ''

        @property
        def cities(self):
            """
            Getter attribute that returns the list of City
            instances with state_id equals to the current State.id
            """
            from models import storage
            result = []
            cities = storage.all(City).values()
            for city in cities:
                if self.id == city.state_id:
                    result.append(city)
            return (result)
