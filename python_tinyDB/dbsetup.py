"""
@Authour : Lindokuhle Magudulela

The scripts sets up database and all relavant tables
"""
from tinydb import TinyDB


data_base = TinyDB('WitsEnergyDb.json')

# Creating tables, tinyDB tables act the same as mongoDB collections
data_base.table('energy')
data_base.table('water')
data_base.table('solarHeating')
