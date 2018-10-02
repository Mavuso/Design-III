'''
Function takes in campuse, builidng name and a dataframe of consumption(an puts it in te correct collection) 
the dataframe is the inserted into the database.
'''
from tinydb import TinyDB
import datetime, json
from tinydb_serialization import SerializationMiddleware
from tinydb_serialization import SerializationMiddleware
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









db = TinyDB('testdb.json',storage=serialization) #First open the document stor which is on the working dir

def df_to_db(building,consumption_df,table = 'energy'):
    number_of_readings = len(consumption_df)

    # existing_tables = db.tables()
    # if((existing_tables.find(collection) == False)):
    #     sys.exit("Tables not found. Try: energy,water,solarHeating")
    # else:
    collection = db.table(table)

    for i in range(number_of_readings):
        
        collection.insert(
        {
             'campus_name': building['location']
                ,
            #     #embedded documents
             'building':{
                        'building_name' : building['building_name'],
                        'used_for': building['used_for']
                },
            # #one dataframe has consumtion values of one building
            # #there we only iterate through the dataframe
            'consumption':{
                'date': consumption_df['Date_time'][i],
                'consumption':consumption_df['Reading'][i]
            }
        })



