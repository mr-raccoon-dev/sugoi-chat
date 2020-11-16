from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from auth.models import User

User_Pydantic = pydantic_model_creator(User, name="User", include=('id', 'username',))
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", include=('username', 'password'))


class AuthUser(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
