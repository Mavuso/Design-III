import pandas as pd
from datetime import datetime
import numpy as np

file = "../Data_files/WITS_The_Junction_MSS_3_Kiosk_Amagumbi_kWh/WITS_The_Junction_MSS_3_Kiosk_Amagumbi_kWh.csv"
df = pd.read_csv(file)
columns = ['Date_time','Reading']
number_of_readings = 1#len(df)
df.columns = columns

#cutting from 04-30 improve data correctness, there almost no missing values after this date
#Casting to date format is time consuming
clean_data = df[df['Date_time'] >"2017-04-30 23:30"]
clean_data = clean_data[clean_data['Date_time'] <"2018-06-30 23:30"]
clean_data.replace(-1,value = np.nan,inplace = True)
clean_data['Reading'] = clean_data['Reading'].interpolate('values') 
print("********CLEAN**********")
print(pd.value_counts(clean_data['Reading'].values,sort=True,dropna = False))

clean_data.to_csv('clean_Amagumbi.csv')

