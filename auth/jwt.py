import os
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import status, HTTPException

from dotenv import load_dotenv
load_dotenv()

class JSONWebToken:

    # __ Para hacer una propiedad privada
    __ALGORITHM = os.environ["ALGORITHM"]
    __SECRET_KEY = os.environ["SECRET_KEY"]
    __ACCESS_TOKEN_EXPIRE_MINUTES = os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]

    def create_access_token(self, username: str):

        expire = datetime.utcnow() + timedelta(minutes = int(self.__ACCESS_TOKEN_EXPIRE_MINUTES))

        payload = {
            "sub": username,
            "exp": expire
        }

        # Retorna el JWT
        return jwt.encode(payload, self.__SECRET_KEY, algorithm = self.__ALGORITHM)

    def validate_access_token(self, token: str):
        
        try:
            payload = jwt.decode(token, self.__SECRET_KEY, algorithms = [self.__ALGORITHM])
            username = payload.get("sub")
        except JWTError:
            raise HTTPException(headers = {"WWW-Authenticate": "Bearer"}, status_code= status.HTTP_401_UNAUTHORIZED, detail = "No se pudieron validar las credenciales")
        
        return username
