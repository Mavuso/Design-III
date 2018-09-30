import pandas as pd
from todate_fun import to_date

#function converts string type to datetime type

#path to file which mush be added to dB
directory = "../Data_files/WITS_The_Junction_MSS_1_Kiosk_Shosholoza_kVarh/WITS_The_Junction_MSS_1_Kiosk_Shosholoza_kVarh.csv"

columns = ['Date_time','Reading']
df = pd.read_csv(directory,header = None,skiprows = 1)
number_of_readings = len(df)
df.columns = columns

for i in range(1):
    df['Date_time'][i] = to_date(df['Date_time'][i]) 
    print(type(df['Date_time'][i]))