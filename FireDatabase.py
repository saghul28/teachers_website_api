import pyrebase
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials
load_dotenv(".env")

config = {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    # "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPnOJwKvdeC0/T\nG9pq3lkSQuXrm8YwKpWdrkXSgqycV+qJqiObQCwtRut5/VqAzx9T3zfVZFb3BMyT\nL6FY/8Mkc+Ns381XhgVA+bMzbHbp0wzRRJY/1EM5/QuGTuEBnE3d1O+OhQM0T1ql\nG/ELap95H3ff56k5dm+VbDpqihIppFNvA344MHoPMxdxqQBvYWAJo1vQ5aorNX7C\npw7+FNnCSg/0XUrSMfWQva9hJMm/F9JWgueHI0KN2VYLz72vEVGe+fsjAjSiKT65\nBmkDbRMfSNJjDSx0nlKrMUFNPTiDm9fywmshqnTQuAq7XAbdAfPVyQXx6yZUn1lu\n64UDU4uFAgMBAAECggEAA6VivmtuwEaAY4Oh6/CVcCNzbzPFz57amky2iNpL6Slf\njzZS9fM8xdZm83Yr6NCfTZaGLsjfWUOjXqRvtWdcn6VSEL/wIJ4UDkXaf9RKfGek\nd7uuVg0N7UOby/4/Dyj4WfQl72ffLY3ANjgiurQnyykzkPNejDEL/fcBLCpQd9et\nnw2dFvzNGAwIU4mxHcjSm0wCX9H2QRaTCjlMLDHhpT+lo3EfSTmMPv/MFCmxedZm\nx18aXv2+zBNdZXV+i6s+BVxeOJCKVkyetuGx/3EiUb2d/Q5/Ya9pMJVRqHIqVfI0\nvkvzo+pCWJiJi/6N6eFV9ED7Jw9AO3Y9gUFsGrzCKQKBgQD07kst0iYR2/w8Gi0T\nBh+bB6AQz49/BgDVT73uJXcOdyclSsrDLLPoqhNdDF87klRgUyg4cobSm16Pc2FW\nOc9n0E3/AWfFroa9NEULm9mjuJ14OYTe+e/ElrtXTpUdUpBQtiMrqYbO11rcDR1r\nA2KOPDTrfzA+T5WBpSx9EBB+TQKBgQDY/tfo2oxE00PG8+JjjyAwtnBoCjS3Hg7I\nTMDtJpuLpF3y7ZF+0Djt5ox7ZRKG3c7WAXs5VyIr1JZLYEwUvS2n66Vq/vHqePe0\nfgwJgafxZPbFsCrtXyoL7XLPgW1V9/h0sYuHuBVjoQ+b/NZDo2o2w3THc+KVQWCz\nBBOeU4sOGQKBgGCZ+5y+3bT9hqZNzKlMKPsELuVyd64pt/pp0Qc0T5is9guHTCFe\naDbDnY99abIdLJoxMhPRV8uI6+q4HxPbCSpwxdJlw3/8LbhB/VluxpAEKFdamEU5\nXo+yw4DTxYwjHDg5HfYCjuDVn0hbA9dJJn3i0RxwtZ5d1SGk+773rwmhAoGBALR2\nJEuDzdnDNP+1fdY8hpHcd9kee766YaLUqjHPxNY6SOOqDTFAq8e1z6kjYmgE+Wni\n637BZyq6bo+bM0qgFeMrx3MXOUs9dQuHNC2HxYqs48l+fATS+t3WiH/n7Gztf5RU\nv2yMfEVSAfBBMlQoCEIpBOqHBq4IJApc3o/yfJepAoGBAOhaKFzsOXsio5lfx+Mp\nWmCLgYBASokFCjuWRlGIMF2bcMIG0B0u3R6Ne510+L4YQofniN1bwyAfa0RMLvDq\nYnDY/WSRWRZVi8xGBrLgstmGDIOXChmJFc2uztse/5EAEP7KmdX7ITqX3CZDk94j\nxy4uj2Nk/XYzUGASbR8Xj8OH\n-----END PRIVATE KEY-----",
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN")
}

cred = credentials.Certificate(config)
print(config)
firebase_admin.initialize_app(cred)

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
}
firebase = pyrebase.initialize_app(firebase_config)
authPyre = firebase.auth()

