#!/usr/bin/env python 3
# module to set up database and config database
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String # these are classes
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship  # use to create foreign key
from sqlalchemy import create_engine  # use config code at tne end of file

# let sqlalchemy know that our classes are special sqlalchemy classes that corresponde to table in our code
Base = declarative_base()


class User(Base):  # create classes
    """class to create the table user"""

    __tablename__ = "user" # let sqlalchemy know that variable to use refer to ourdatabase

    id = Column(Integer, primary_key=True)# nullable false column entry
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))  # 250 setting length of string


class Category(Base):
    """class to create the table category"""

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)# ref row in different table
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

    @property
    def serialize(self):
        """return object data in serialized format"""

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'catergory_id': self.category_id
        }


# creaes instance of out create engine points  to the database we will use
engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)  # goes into the database and adds classes
