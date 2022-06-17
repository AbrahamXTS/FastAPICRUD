from bson import ObjectId
from config.database import db
from models.user import UserModel
from routes.login import oauth2_scheme
from starlette.status import HTTP_204_NO_CONTENT
from schemas.user import userEntity, usersEntity
from utilities.handle_new_user import handle_new_user
from fastapi import APIRouter, Response, status, Depends

user = APIRouter()

# De la base de datos "fastapi" de mongoDB hay una colección llamada users: db.fastapi.users

@user.get("/users", response_model = list[UserModel], tags = ["Users"]) 
def get_all_users(token: str = Depends(oauth2_scheme)):
    # find busca todos los datos de la colección
    return usersEntity(db.fastapi.users.find())

@user.get("/users/{id}", response_model = UserModel, tags = ["Users"])
def find_user(id: str, token: str = Depends(oauth2_scheme)):
    # Convertimos el id de string a ObjectId de MongoDB
    return userEntity(db.fastapi.users.find_one({"_id": ObjectId(id)}))

@user.post("/users", response_model = str, tags = ["Users"])
def create_user(user: UserModel, token: str = Depends(oauth2_scheme)):

    nuevo_usuario = handle_new_user(user)

    id_nuevo_usuario = db.fastapi.users.insert_one(nuevo_usuario).inserted_id

    return f"Usuario creado correctamente: {id_nuevo_usuario}"

@user.put("/users/{id}", response_model = UserModel, tags = ["Users"])
def update_user(id: str, user: UserModel, token: str = Depends(oauth2_scheme)):

    # Con $set establecemos el objeto con el que vamos a actualizar
    db.fastapi.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": handle_new_user(user)})
    
    # Retornamos el usuario modificado
    return userEntity(db.fastapi.users.find_one({"_id": ObjectId(id)}))

@user.delete("/users/{id}", status_code = status.HTTP_204_NO_CONTENT, tags = ["Users"])
def delete_user(id: str, token: str = Depends(oauth2_scheme)):
    # Ejecuta el borrado
    userEntity(db.fastapi.users.find_one_and_delete({"_id": ObjectId(id)}))

    return Response(status_code=HTTP_204_NO_CONTENT)