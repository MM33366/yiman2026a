import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "陳沂蔓",
  "mail": "emma65454@gmail.com",
  "lab": 333
}

doc_ref = db.collection("靜宜資管2026a").document("yiman")
doc_ref.set(doc)
