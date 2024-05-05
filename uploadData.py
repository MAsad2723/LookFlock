import firebase_admin
from firebase_admin import credentials, firestore, db
import json
cred = credentials.Certificate('/home/k213458/Documents/WebProjects/Lookflock/lookflockbackend/drf/certificate.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://lookflock-asad-default-rtdb.asia-southeast1.firebasedatabase.app"})
db = firestore.client()
batch = db.batch()
with open('data.json', 'r') as file:
    data = json.load(file)

# Write data to Firestore with incremental IDs
for idx, doc_data in enumerate(data, start=1):
    doc_ref = db.collection('lookflock').document(str(idx))
    doc_ref.set(doc_data)
    print("done", idx)