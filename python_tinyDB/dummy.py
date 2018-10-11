from tinydb import TinyDB
from tinydb_serialization import SerializationMiddleware
from tinydb import Query
from datetime import datetime


from datetime import datetime
from tinydb_serialization import Serializer
from serializer import DateTimeSerializer

serialization = SerializationMiddleware()
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')

db = TinyDB('db.json', storage=serialization)
db.insert({'date': datetime(2000, 1, 1, 12, 0, 0)})

print(db.all())