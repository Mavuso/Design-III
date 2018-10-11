'''
Module for database extraction. This module will be used by modules on the logic layer
@Author: L Magudulela
'''
from tinydb import TinyDB, where, Query
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

def get_dates(start =to_date("2013-01-01 00:00") ,end=to_date("2013-01-01 00:00"),collection = 'energy'):
    query  = Query()
    db = TinyDB('testdb.json',storage=serialization)
    collection = db.table(collection)
    return (collection.search((query.consumption['date']>= start) & (query.consumption['date']<= end)))

#
def get_yearly(year = '2013',collection = 'energy'
    ,building = {"location":"Wits_The_Junction","name":"Shosholoza"}):
    start = to_date(year + '-01-01 00:00')
    end = to_date(year + '-01-01 00:00')
    print(get_dates(start,end,'energy'))


def get_monthly(year = 2013,month = '01',collection = 'energy'
            ,building = {"location":"Wits_The_Junction","name":"Shosholoza"}):
    start = to_date(str(year) +"-"+str(month)+'-01 00:00')
    end = to_date(str(year) +"-"+str(month)+'-01 00:00')
    print(get_dates(start,end,collection))

def get_daily(year = 2013,month = '01',day=1,collection = 'energy'
            ,building = {"location":"Wits_The_Junction","name":"Shosholoza"}):
    start = to_date(str(year) +"-"+str(month)+'-'+str(day)+' 00:01')
    end = to_date(str(year) +"-"+str(month)+'-'+str(day)+' 23:59')
    print(get_dates(start,end,collection))

print(get_daily())
