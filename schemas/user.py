# Estas funciones sirven para modelar lo que provenga de la BD

def userEntity(user) -> dict:
    return {
        # Convertimos el ID del usuario de ObjectID a string
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }


def usersEntity(usersList) -> list:
    # Por cada usuario en la lista de usuarios, me vas a crear una entidad con la función ⬆️
    return [userEntity(user) for user in usersList]
