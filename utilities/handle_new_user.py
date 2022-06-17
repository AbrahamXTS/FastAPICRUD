from models.user import UserModel
from auth.auth import Auth

authorization = Auth()

def handle_new_user(user: UserModel):
    
    nuevo_usuario = dict(user)
    
    # Eliminamos la propiedad id del modelo recibido para que se autoasigne y evite el null
    del nuevo_usuario["id"]

    nuevo_usuario["email"] = nuevo_usuario["email"].lower()

    # Ciframos la contraseña del usuario
    nuevo_usuario["password"] = authorization.get_password_hash(nuevo_usuario["password"])

    return nuevo_usuario