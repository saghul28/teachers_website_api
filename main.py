import firebase_admin
from firebase_admin import credentials
from FireDatabase import config

def initialize_firebase():
    cred = credentials.Certificate(config)
    firebase_admin.initialize_app(cred)

initialize_firebase()

from fastapi import FastAPI
from Routers.Account import UserAuth
from Routers.Blog import blog, comments
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(UserAuth.router, prefix="/user", tags=["User"])
app.include_router(blog.router, prefix="/blog", tags=["blog"])
app.include_router(comments.router, prefix="/blog", tags=["comments"])



# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello World"}
