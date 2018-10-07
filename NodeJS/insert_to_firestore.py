from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from todate_fun import to_date
from create_uniqueID import create_docID


file = 'credi.json'
#get Admin credentials ceritificate
cred = credentials.Certificate(file)
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://wits-energy-visualization.firebaseio.com'
})

#consumption df is a df containing all the energy consumption values
#from .csv . Building is a dictionery with building infor.

dataB = firestore.client()

data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}

# Add a new doc in collection 'cities' with ID 'LA'
dataB.collection(u'cities').document(u'LA44').set(data)


def insert_to_firestore(consumption_df,collection = "energy",
building={"building_id":"shosholoza_jun","campus_id":"wits_junction",}):
    #initialize firestore
    database = firestore.client()
    
    #number_of_readings = len(consumption_df)
    number_of_readings = 1
    print(consumption_df.head)
    print("**inserting to firestore**")
    for i in range(number_of_readings):
        
        doc = database.collection(u'energy_2').document(
            create_docID(consumption_df['Date_time'][i],building["building_id"]))
        doc.set({
            u'campus_id' : building["campus_id"],
            u'building_id' :building["building_id"],
            u'Date_time': to_date(consumption_df['Date_time'][i]),
            u'consumption': consumption_df['Reading'][i]
        })