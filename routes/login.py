from auth.auth import Auth
from config.database import db
from auth.jwt import JSONWebToken
from models.token import TokenModel
from schemas.user import userEntity
from passlib.hash import sha256_crypt
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm, OAuth2PasswordBearer

authorization = Auth()
login = APIRouter()
jsonwebtoken = JSONWebToken()

# El parametro tokenUrl es la ruta relativa de la que se obtendrá el token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

@login.post("/login", response_model = TokenModel, tags = ["Auth"])
async def handle_login(user: OAuth2PasswordRequestForm = Depends()):
    
    userDB = db.fastapi.users.find_one({"email": user.username})
    
    if not userDB:
        raise HTTPException(headers = {"WWW-Authenticate": "Bearer"}, status_code= status.HTTP_401_UNAUTHORIZED, detail = "Credenciales no válidas")
    else:
        if not authorization.verify_password(user.password, userDB["password"]):
             raise HTTPException(headers = {"WWW-Authenticate": "Bearer"}, status_code= status.HTTP_401_UNAUTHORIZED, detail = "Password no válida")
    
    access_token = jsonwebtoken.create_access_token(user.username)

    return {"access_token": access_token, "token_type": "Bearer"}
