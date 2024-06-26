#!/usr/bin/python3
"""This is the  user class """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
import hashlib
from os import getenv


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for your login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade='all, delete, delete-orphan',
                               backref="user")
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                                backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            encrypt = kwargs.pop('password', None)
            User.set_password(self, encrypt)
        super().__init__(*args, **kwargs)

    def set_password(self, _password):
        encrypt = hashlib.md5()
        encrypt.update(_password.encode("utf-8"))
        encrypt = encrypt.hexdigest()
        setattr(self, "password", encrypt)
