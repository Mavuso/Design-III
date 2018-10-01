"""
@Authour : Lindokuhle Magudulela
The scripts sets up database and all relavant tables
"""
from tinydb import TinyDB
from tinydb_serialization import SerializationMiddleware
from tinydb import Query
from datetime import datetime
from tinydb_serialization import Serializer

class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime  # The class this serializer handles

    def encode(self, obj):
        return obj.strftime("%Y-%m-%d %H:%M")

    def decode(self, s):
        return datetime.strptime(s, "%Y-%m-%d %H:%M")


serialization = SerializationMiddleware()
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')




data_base = TinyDB('WitsEnergyDb.json',storage=serialization)

# Creating tables, tinyDB tables act the same as mongoDB collections
data_base.table('energy')
data_base.table('water')
data_base.table('solarHeating')
