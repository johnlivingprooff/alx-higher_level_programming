#!/usr/bin/python3
"""Class: State defines an instance of Base = declarative_base():"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """the State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
