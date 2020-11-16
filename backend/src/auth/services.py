import bcrypt
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from auth.models import User


class AuthService:
    def __init__(self):
        pass

    async def login(self, username, password):
        try:
            user = await User.get(username=username)
        except DoesNotExist:
            return {"status": "error", "message": "username/password incorrect"}

        pwbytes = password.encode('utf-8')
        saltbytes = user.password.encode('utf-8')
        if bcrypt.hashpw(pwbytes, saltbytes) == saltbytes:
            token = b'new_token'

            return {"status": "success", "token": token.decode('utf-8')}
        return {"status": "error", "message": "username/password incorrect"}

    def validate(self, token):
        try:
            data = jwt.decode(token, self.key)
        except Exception as e:
            if "expired" in str(e):
                raise HTTPException(status_code=400, detail={"status": "error",
                                                             "message": "Token expired"})
            else:
                raise HTTPException(status_code=400, detail={"status": "error",
                                                             "message": "Exception: " + str(
                                                                 e)})
        return data


def generate_password_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
