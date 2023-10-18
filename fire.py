import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Specify the path to the service account JSON file
sa_json_file = os.environ.get("FIREBASE_CONFIG")
tag_data = os.environ.get("TAG_DATA")

try:
    # Use a service account.
    cred = credentials.Certificate(sa_json_file)

    app = firebase_admin.initialize_app(cred)

    db = firestore.client()

    data = {"tag": tag_data}

    # Add a new doc in collection 'tags' with ID 'data'
    db.collection("tags").document("data").set(data)

    print("Updated Firestore")
except Exception as e:
    print(f"Failed to update Firestore: {str(e)}")
