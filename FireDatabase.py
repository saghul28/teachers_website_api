# pyrebase
import pyrebase
firebase_config = {
    "apiKey": "AIzaSyAXO3nXS6mvWNmMMQzBDc1w5GpgEqaVZf0",
    "authDomain": "teacherapi-6b000.firebaseapp.com",
    "databaseURL": "https://teacherapi-6b000-default-rtdb.firebaseio.com",
    "projectId": "teacherapi-6b000",
    "storageBucket": "teacherapi-6b000.appspot.com",
    "messagingSenderId": "850831879102",
    "appId": "1:850831879102:web:770410ce0bcdd7fa50e7ef",
    "measurementId": "G-J4Y7FS6SRC",
    "serviceAccount": "Teacher.json"
}
firebase = pyrebase.initialize_app(firebase_config)

authPyre = firebase.auth()
