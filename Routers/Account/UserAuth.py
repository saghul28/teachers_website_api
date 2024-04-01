from fastapi import APIRouter, Depends, Header, Response

from pydantic import BaseModel, EmailStr
from FireDatabase import authPyre
from firebase_admin import auth
from fastapi import Header, HTTPException
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer

router = APIRouter()
security = HTTPBearer()

class Register(BaseModel):
    username: str
    password: str
    email: EmailStr
    phone_number: int


@router.post("/signup")
async def signup(register: Register):
    display_name = register.username
    email = register.email
    phone_number = register.phone_number
    password = register.password
    try:
        auth.create_user(email=email, password=password, display_name=display_name)
        return {"message": email}
    except Exception as e:
        return {"message": str(e)}


class Login(BaseModel):
    email: EmailStr
    password: str


@router.post("/login")
async def login(userlogin: Login):
    email = userlogin.email
    password = userlogin.password
    try:
        user = authPyre.sign_in_with_email_and_password(email=email, password=password)
        response = Response()
        # Set the token in the response headers
        user1 = response.headers["Authorization"] = f"Bearer {user['idToken']}"
        print(response.headers)
        return {"token": user["idToken"],"localId": user["localId"]}
    except Exception as e:
        return {"message": str(e)}



def validate_token(token: str):
    try:
        user = auth.verify_id_token(token)
        return user
    except Exception as e:
        raise Exception(status_code=401, detail="Invalid token")


def authenticate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        if credentials is None:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        token = credentials.credentials
        coded_token = auth.verify_id_token(token)
        user = auth.get_user(coded_token["uid"])
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid authorization header")

@router.get("/protected")
def protected(token: str = Depends(authenticate_token)):
    return {"message": token}
