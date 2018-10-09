import pandas as pd
from todate_fun import to_date
from insert_to_firestore import insert_to_firestore

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

df.drop(axis = 1,columns = "Unnamed: 0",inplace = True)



df.columns = columns

df['Reading']=df['Reading'].astype('float') #changing type to json serializable formate

print("***Sending to 'to firestore module'***")
    
insert_to_firestore(df,utility = "energy",
building={"building_name":"Amagumbi","campus_name":"wits_junction","type":"Residential"})




#schema of document
#the document is imbedded, campus <- building <- consumption

