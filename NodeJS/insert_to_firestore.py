from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from todate_fun import to_date
from create_uniqueID import create_docID

#these are the chosen months in the dataset
months = ["2017-05","2017-06","2017-07"]
# 2017-08","2017-09"
#         ,"2017-10","2017-11","2017-12","2018-01","2018-02","2018-03"
#         ,"2018-04","2018-05","2018-06"]

#get Admin credentials ceritificate
cred = credentials.Certificate('credi.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://wits-energy-visualization.firebaseio.com'
})

#consumption df is a df containing all the energy consumption values
#from .csv . Building is a dictionery with building infor.

def insert_to_firestore(consumption_df,utility,building):
    database = firestore.client()
    
    consumption_df.sort_values('Date_time',inplace = True)
    
    print("**Insert to firestore function**")
    collection_name = utility + "_" + building["building_name"] + "_" + building["campus_name"]

    for x in months:
        print(x)
        monthly_readings = []
        timestamps = []
        for i in range(len(consumption_df)):
            if(consumption_df['Date_time'][i][:7] == x):          
                monthly_readings.append((consumption_df['Reading'][i]))
                timestamps.append(to_date(consumption_df['Date_time'][i]))                       
                consumption_df = consumption_df[consumption_df['Date_time']!=consumption_df['Date_time'][i]]   

            else:
                consumption_df = consumption_df.reset_index(drop = True)
                print("Writting document")
                doc = database.collection(collection_name).document(create_docID(x,building["building_name"],building["campus_name"]))
                monthly_doc = {
            "month" :x[5:],
            "year" :x[:4],
            "campus":building["campus_name"],
            "building":building["building_name"],
            "type":building["type"],
            "consumptions":monthly_readings,
            "timestamps":timestamps,
            }
                doc.set(monthly_doc)
                break
                    

                #monthly_readings = monthly_readings.append((['Reading'][i]))
                #date_time = date_time.append(to_date(['Date_time'][i]))
                
                
            #    print(monthly_doc)
        # doc = database.collection(collection).document(
        #     create_docID(consumption_df['Date_time'][i],building["building_id"]))
        # doc.set({
        #     u'campus_id' : collection+building["campus_id"],
        #     u'building_id' : collection+building["building_id"],
        #     u'Date_time': to_date(consumption_df['Date_time'][i]),
        #     u'consumption': consumption_df['Reading'][i]
        # })
    
