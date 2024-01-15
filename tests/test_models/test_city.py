#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class test_City(test_basemodel):
    """ """

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_city = City()
        cls.new_city.state_id = "California"
        cls.new_city.name_id = "San Francisco"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_city
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_City_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_city.__tablename__, "cities")

    def test_City_inheritance(self):
        '''
            Tests that the City class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_city, BaseModel)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
