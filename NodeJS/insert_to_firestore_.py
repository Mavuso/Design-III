from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from todate_fun import to_date
from create_uniqueID import create_docID

#get Admin credentials ceritificate
cred = credentials.Certificate('credi.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://wits-energy-visualization.firebaseio.com'
})

#consumption df is a df containing all the energy consumption values
#from .csv . Building is a dictionery with building infor.
database = firestore.client()

doc_ref = database.collection(u'people').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

users_ref = database.collection('people')
docs = users_ref.get()

# for doc in docs:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))

def insert_to_firestore(consumption_df,collection,building):
    #initialize firestore
    database = firestore.client()
    
    number_of_readings = len(consumption_df)
    print(consumption_df.head)
    print("**inserting to firestore**")
    
    for i in range(number_of_readings):
        doc = database.collection(collection).document(
            create_docID(consumption_df['Date_time'][i],building["building_id"]))
        doc.set({
            u'campus_id' : collection+building["campus_id"],
            u'building_id' : collection+building["building_id"],
            u'Date_time': to_date(consumption_df['Date_time'][i]),
            u'consumption': consumption_df['Reading'][i]
        })
    
