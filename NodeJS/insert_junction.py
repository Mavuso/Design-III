import pandas as pd
from todate_fun import to_date
from insert_to_firestore_ import insert_to_firestore

#function converts string type to datetime type

#path to file which mush be added to dB
building = {}
building['building_name']='Shosholoza'
building['location']='Wits_The_Junction'
building['used_for']='Residential'

print('***Extracting data from csv****')

directory = "../clean_data/junction_amagumbi.csv"

columns = ['Date_time','Reading']
df = pd.read_csv(directory)
number_of_readings = 1#len(df)
df.columns = columns

df['Reading']=df['Reading'].astype('float') #changing type to json serializable formate

insert_to_firestore(df,collection = "energy",
building={"building_id":"amagumbi_jun","campus_id":"wits_junction",})

#schema of document
#the document is imbedded, campus <- building <- consumption

