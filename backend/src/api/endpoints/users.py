from typing import List

from fastapi import APIRouter, HTTPException

from api.schemas.users import (
    AuthUser, Token, User_Pydantic, User, UserIn_Pydantic
)
from auth.services import AuthService, generate_password_hash

router = APIRouter()
auth = AuthService()


@router.get("/", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


@router.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user.password = generate_password_hash(user.password)
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)
