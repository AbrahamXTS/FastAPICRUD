from models.user import UserModel
from passlib.hash import sha256_crypt

def handle_new_user(user: UserModel):
    
    nuevo_usuario = dict(user)
    
    # Eliminamos la propiedad id del modelo recibido para que se autoasigne y evite el null
    del nuevo_usuario["id"]

    # Ciframos la contraseña del usuario
    nuevo_usuario["password"] = sha256_crypt.encrypt(nuevo_usuario["password"])

    return nuevo_usuario