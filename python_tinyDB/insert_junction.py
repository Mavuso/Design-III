import pandas as pd
from todate_fun import to_date
from tinydb import TinyDB, where
from df_to_db import df_to_db
#function converts string type to datetime type

#path to file which mush be added to dB
building = {}
building['building_name']='Shosholoza'
building['location']='Wits_The_Junction'
building['used_for']='Residential'

print('***Extracting data from csv****')
directory = "../Data_files/TEST/WITS_The_Junction_MSS_1_Kiosk_Shosholoza_kVarh.csv"

columns = ['Date_time','Reading']
df = pd.read_csv(directory)
number_of_readings = len(df)
df.columns = columns

for i in range(number_of_readings):
     df['Date_time'][i] = to_date(df['Date_time'][i]) 

print(type(df['Date_time'][4]))
df['Reading']=df['Reading'].astype('float') #changing type to json serializable formate

df_to_db(building,df,)
#schema of document
#the document is imbedded, campus <- building <- consumption
