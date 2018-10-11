let admin = require('firebase-admin');
let serviceAccount = {
    "type": "service_account",
    "project_id": "wits-energy-visualization",
    "private_key_id": "3ca60f9d09de90c98807c0a2bea83dd4ae03eb73",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCbxX+28OWhlmmX\nmDHVUqFS4az0e5/WYRQuEVoPqCQ5PhLHwMdBC1p/xXDeRSJLvz2rbbqq9uTu277M\nymeor6KR2QKNTUfn/1yGGmQfCQWqMEUKrGwcTPjNaJq+L2rb3Tn9m+PMLaeJtGmi\nnlPehBsIKzWQOHgwKqJkvzXDr3A9LpqnpxjKWc4zzRSQ4iZhNE+JBh1E9IKaUdy+\nSOXHBwoFgmWWQHtKHl9B/u8IDA40BrKvDeD5eTh3S1IdzCkZ293zEQAGYr5YolES\najwwVRJk+pmJTY+qmOAoQALnKZjK0TP9GtQ7uFi6bKwtklErymL+etJ0wVpZdd/q\n3jXHCtf/AgMBAAECggEACHysvJg7pd+uyVJcZYQjtpyfUnZWQZU3E8F6d8yDi+9G\nKt/MG2hvQFnodq74M0qF2IxZQmcpFwIeNas4SNHbWJK+l4zkqsIlIntXbCd1Yw3p\nNq+Pqyt4cAlpSozSOvNyBuk48pvXYa9uN/l9yVH6S3bxnqkTYOoM859FYlZX/Hh/\nsRWbOiIo8uvQzLVC4K9mFhD1ZzZf9wvs1LLLlSrtMaJ4ww7X7CHx77yRC0iYiHO3\nvqxrmAhcye4lyrYHtWBLoHhwkaHVEIM9umFIAHEo1hgYWdlvFAAfwMdHtd/vU2RJ\nroDRwKOebw9rJFTdo7C910zPJtX39iTupCJp1rz+LQKBgQDO4SoGc0rxkVDZFYp0\ncJzeBewBmzeTboWrbuYA/YlR6eY6R2R2ODeO6J57LqF6we75oWnBC9qT1J2MssK1\nWqWzbzRhGyG+YlO3pL0aEVevRhLZ2TCC1riumVvsg4TbSUX9/rOYq3XOwdP2MLuq\npMCXtqI2732u8uDzQvXzlMjrgwKBgQDAwdBv9MBWA9s2PxQwPawSbucDdC8H3HYI\nGS0WlrzgsmwRyjArUEVnHfhq+ErV5zWZJll+MhdYvXRBkxzWQxYeTP8NieKmZAyx\n2JnbHO9YARP7K3cVDkOCIN+JIBjFU3Ufqy/uPJZQ6SvXqov9Y4AnCE6G8OQOykCG\nzT3tq/xM1QKBgEUVgdAnngYvLZ1giRy7IlcuCRK8P4HXLYIDBYGdKMcW4Y/imVS1\nDzCE06908e2pZ2ErGsKhb7tgC8CZTVX8UEssPoSS5+DIuwYfWBqlYe+g6difo4h9\npayAf+bqQGpt/JaGAHliAHQr29lhirnATKQdE+xea00JxD7XxIQz0ih7AoGAJcta\nxTjmJXdoGgDQQo01GgAox6KWPiJZ+kiFcLJpol0Zl3tfan64vPlBZif89Gf7OGYu\nkfHcZgfvrZPcyZ4pzhMmx07L4/gmDRD9SdsoisbbVho1pSlAz1kGu2pRsQ8mHemA\n4mN6za6KbCUCgdJqpDyauRaugL/jWwsPI3TfaWkCgYEAoxS/Oqyk8dtBkGj1SgUi\nNZHpMtxsQgMmHjQzMAAi/DWTiTLRbg6BCfWaV4RH5BjOA5hV8xZyUq7PC5nHhYbA\n2M7/8AX9eWzvbEkbXA1yYcccLP/1pgrBBaAKhMuMpCPmgOH4usTdrMMwctxwiCgy\nZ/thquJ3W8L9ac/rHeVNQyg=\n-----END PRIVATE KEY-----\n",
    "client_email": "admin-account@wits-energy-visualization.iam.gserviceaccount.com",
    "client_id": "101221781769315104346",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/admin-account%40wits-energy-visualization.iam.gserviceaccount.com"
  };

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'https://wits-energy-visualization.firebaseio.com'
});

let database = admin.firestore();



let campus = "wits_junction";
let building = "Amagumbi";
let utility = "energy";

let collection_name = utility+"_"+building+"_"+campus

function get_firestore_data(res){
    let y = []//Consumption array
    let x = []//dates array
  
    let doc_ref = database.collection(collection_name);
    var query = doc_ref.where('month', '==', '06').get()
    .then(snapshot => {
      snapshot.forEach(doc => {
        y=doc.data().consumptions;
        x =doc.data().timestamps;
        res.json({'x':x,'y':y});
    });
      
    })
    .catch(err => {
      console.log('Error getting documents', err);
    });
    
}

module.exports = get_firestore_data;