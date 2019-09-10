#!/usr/bin/env python 3
#module to set up database and config database
import sys

from sqlalchemy import Column, ForeignKey, Integer, String # these are classes
from sqlalchemy.ext.delcarative import delcarative_base #use in configuration class code
from sqlalchemy.orm import relationship #use to create foreign key
from sqlalchemy import create_engine #use config code at tne end of file

Base = delcarative_base() # let sqlalchemy know that our classes are special sqlalchemy classes that corresponde to table in our code

class User(Base): #create classes
    """class to create the table user"""

    __tablename__ = "user" #let sqlalchemy know that variable to use refer to ourdatabase

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Catergory(Base):
    """class to create the table category"""

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
            """returns object data in serialized format"""

            return {
                'id': self.id,
                'name': self.name,
                'user.id': self.user_id
            }

class Item(Base):
    """to create table items"""

    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    catergory_id = Column(Integer, ForeignKey('catergory.id'))
    category = relationship(Catergory)
    user_id = Column(Integer, ForeignKey('user_id'))
    user = relationship(User)

    @property:
    def serialize(self):
        """return object data in serialized format"""

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'catergory_id': self.category_id
        }

engine - create_engine('sqlite:///itemcatalog.db') #creaes instance of out create engine and points  to the database we will use
Base.metadata.create_all(engine) # goes into the database and adds classes
