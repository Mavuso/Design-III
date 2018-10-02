"""
@Authour : Lindokuhle Magudulela
The scripts sets up database and all relavant tables
"""
from tinydb import TinyDB
from serializer import DateTimeSerializer
from tinydb_serialization import SerializationMiddleware
from tinydb_serialization import Serializer




serialization = SerializationMiddleware()
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')






data_base = TinyDB('testdb.json',storage=serialization)

# Creating tables, tinyDB tables act the same as mongoDB collections
data_base.table('energy')
data_base.table('water')
data_base.table('solarHeating')
