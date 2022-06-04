from passlib.hash import sha256_crypt
from models.user import UserModel, UserEditedModel

def handle_edit_user(userActual: UserModel, userEditado: UserEditedModel):

    usuario_actual = userActual
    usuario_editado = dict(userEditado)

    # Si los valores vienen vacios asignamos los ya existentes.
    usuario_editado["id"] = usuario_actual["id"]

    usuario_editado["name"] = usuario_actual["name"] if usuario_editado["name"] == None else usuario_editado["name"]

    usuario_editado["email"] = usuario_actual["email"] if usuario_editado["email"] == None else usuario_editado["email"]
    
    usuario_editado["password"] = usuario_actual["password"] if usuario_editado["password"] == None else sha256_crypt.encrypt(usuario_editado["password"])

    return usuario_editado
