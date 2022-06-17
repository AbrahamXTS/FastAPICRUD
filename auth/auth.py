from passlib.context import CryptContext

class Auth:

    __pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

    def get_password_hash(self, password):
        return self.__pwd_context.hash(password)

    def verify_password(self, password, hashed_password):
        return self.__pwd_context.verify(password, hashed_password)
