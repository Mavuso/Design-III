'''
Module for database extraction. This module will be used by modules on the logic layer
@Author: L Magudulela
'''
from tinydb import TinyDB, where
from tinydb import TinyDB
from todate_fun import to_date
import datetime, json
from tinydb_serialization import SerializationMiddleware
from tinydb_serialization import SerializationMiddleware
from datetime import datetime
from tinydb_serialization import Serializer
from serializer import DateTimeSerializer


serialization = SerializationMiddleware()
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')






#def get_year(date,collection = 'energy'):
db = TinyDB('testdb.json',storage=serialization)
collection = db.table('energy')
print(collection.search(where("consumption")['date']== to_date('2013-01-01 17:00')))
#print(collection.search(where("campus_name") == "Wits_The_Junction"))
print("END")

