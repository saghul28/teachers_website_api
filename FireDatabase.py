# # pyrebase
# import pyrebase
# import os
# firebase_config = {
#     "apiKey": "AIzaSyAXO3nXS6mvWNmMMQzBDc1w5GpgEqaVZf0",
#     "authDomain": "teacherapi-6b000.firebaseapp.com",
#     "databaseURL": "https://teacherapi-6b000-default-rtdb.firebaseio.com",
#     "projectId": "teacherapi-6b000",
#     "storageBucket": "teacherapi-6b000.appspot.com",
#     "messagingSenderId": "850831879102",
#     "appId": "1:850831879102:web:770410ce0bcdd7fa50e7ef",
#     "measurementId": "G-J4Y7FS6SRC",
#     "serviceAccount": "Teacher.json"
# }
# firebase = pyrebase.initialize_app(firebase_config)
#
# authPyre = firebase.auth()
import pyrebase
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
    "serviceAccount":"Teacher.json"
}

print("environmern  :"+os.getenv("FIREBASE_API_KEY"))

firebase = pyrebase.initialize_app(firebase_config)
authPyre = firebase.auth()
